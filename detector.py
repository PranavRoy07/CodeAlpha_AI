

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import cv2
import numpy as np

try:
    from ultralytics import YOLO
    _YOLO_OK = True
except ImportError:
    _YOLO_OK = False

# ─────────────────────────────────────────────
#   CONSTANTS & THEME
# ─────────────────────────────────────────────

APP_NAME   = "TITAN"
SUBTITLE   = "Object Detection & Tracking"

BG      = "#1e1e2e"
SURFACE = "#313244"
TEXT    = "#cdd6f4"
SUBTEXT = "#a6adc8"
ACCENT  = "#89b4fa"
GREEN   = "#a6e3a1"
YELLOW  = "#f9e2af"
RED     = "#f38ba8"
TEAL    = "#94e2d5"
PURPLE  = "#cba6f7"

MODELS = {
    "YOLOv8 Nano  (fastest)":  "yolov8n.pt",
    "YOLOv8 Small (balanced)": "yolov8s.pt",
    "YOLOv8 Medium (accurate)":"yolov8m.pt",
}


_CLASS_COLORS: dict[int, tuple[int, int, int]] = {}

def class_color(class_id: int) -> tuple[int, int, int]:
    """Return a stable BGR color for a given class ID."""
    if class_id not in _CLASS_COLORS:
        np.random.seed(class_id * 37 + 13)
        r, g, b = np.random.randint(80, 230, 3).tolist()
        _CLASS_COLORS[class_id] = (b, g, r)   # OpenCV is BGR
    return _CLASS_COLORS[class_id]



def draw_box(
    frame: np.ndarray,
    x1: int, y1: int, x2: int, y2: int,
    label: str,
    color: tuple[int, int, int],
    track_id: int | None = None,
) -> None:
    """Draw a rounded-corner bounding box with label badge."""
    thickness = 2
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

    corner = 14
    cv2.line(frame, (x1, y1), (x1 + corner, y1), color, thickness + 1)
    cv2.line(frame, (x1, y1), (x1, y1 + corner), color, thickness + 1)
    cv2.line(frame, (x2, y1), (x2 - corner, y1), color, thickness + 1)
    cv2.line(frame, (x2, y1), (x2, y1 + corner), color, thickness + 1)
    cv2.line(frame, (x1, y2), (x1 + corner, y2), color, thickness + 1)
    cv2.line(frame, (x1, y2), (x1, y2 - corner), color, thickness + 1)
    cv2.line(frame, (x2, y2), (x2 - corner, y2), color, thickness + 1)
    cv2.line(frame, (x2, y2), (x2, y2 - corner), color, thickness + 1)

    display = f" #{track_id}  {label}" if track_id is not None else f" {label}"
    font       = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 0.50
    font_thick = 1
    (tw, th), _ = cv2.getTextSize(display, font, font_scale, font_thick)
    pad = 4
    badge_y1 = max(y1 - th - pad * 2, 0)
    badge_y2 = max(y1, th + pad * 2)
    cv2.rectangle(frame, (x1, badge_y1), (x1 + tw + pad * 2, badge_y2), color, -1)
    cv2.putText(
        frame, display,
        (x1 + pad, badge_y2 - pad),
        font, font_scale, (255, 255, 255), font_thick, cv2.LINE_AA
    )


def draw_overlay(
    frame: np.ndarray,
    fps: float,
    obj_count: int,
    model_name: str,
    paused: bool,
) -> None:
    """Draw semi-transparent HUD in the top-right corner."""
    h, w = frame.shape[:2]
    lines = [
        f"FPS   : {fps:5.1f}",
        f"Objects: {obj_count:3d}",
        f"Model  : {model_name}",
        "[ P ] Pause   [ Q ] Quit",
        "PAUSED" if paused else "",
    ]
    font       = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.45
    font_thick = 1
    pad        = 8
    line_h     = 20

    max_w = max(cv2.getTextSize(l, font, font_scale, font_thick)[0][0] for l in lines if l) + pad * 2
    box_h = len([l for l in lines if l]) * line_h + pad * 2
    x0    = w - max_w - 10
    y0    = 10

    overlay = frame.copy()
    cv2.rectangle(overlay, (x0, y0), (x0 + max_w, y0 + box_h), (30, 30, 46), -1)
    cv2.addWeighted(overlay, 0.65, frame, 0.35, 0, frame)

    row = y0 + pad + line_h - 4
    for line in lines:
        if not line:
            continue
        color = (0, 80, 255) if line == "PAUSED" else (200, 220, 255)
        cv2.putText(frame, line, (x0 + pad, row), font, font_scale, color, font_thick, cv2.LINE_AA)
        row += line_h



class DetectionSession:
    """Manages a single detection run in a background thread."""

    def __init__(
        self,
        source,           # 0 for webcam, str for file path
        model_path: str,
        conf: float,
        on_fps_update,    # callback(fps: float)
        on_count_update,  # callback(count: int)
        on_stop,          # callback()
    ):
        self.source         = source
        self.model_path     = model_path
        self.conf           = conf
        self.on_fps_update  = on_fps_update
        self.on_count_update= on_count_update
        self.on_stop        = on_stop

        self._running = False
        self._paused  = False
        self._thread  = None

    def start(self):
        self._running = True
        self._paused  = False
        self._thread  = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False

    def toggle_pause(self):
        self._paused = not self._paused

    def _run(self):
        model      = YOLO(self.model_path)
        model_name = self.model_path.replace(".pt", "").upper()

        cap = cv2.VideoCapture(self.source)
        if not cap.isOpened():
            messagebox.showerror(
                "Source Error",
                f"Cannot open source: {self.source}\n"
                "Check your webcam index or video file path."
            )
            self.on_stop()
            return

        WIN = f"{APP_NAME} — {SUBTITLE}"
        cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(WIN, 960, 540)

        fps_timer  = time.time()
        fps_frames = 0
        fps        = 0.0
        paused_frame = None

        while self._running:
            if self._paused:
                if paused_frame is not None:
                    display = paused_frame.copy()
                    draw_overlay(display, fps, 0, model_name, paused=True)
                    cv2.imshow(WIN, display)
                key = cv2.waitKey(30) & 0xFF
                if key == ord("q") or cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1:
                    break
                if key == ord("p"):
                    self._paused = False
                continue

            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            paused_frame = frame.copy()

            results = model.track(
                frame,
                conf      = self.conf,
                persist   = True,
                tracker   = "bytetrack.yaml",
                verbose   = False,
            )

            obj_count = 0
            if results and results[0].boxes is not None:
                boxes  = results[0].boxes
                names  = model.names

                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    cls_id   = int(box.cls[0])
                    conf_val = float(box.conf[0])
                    track_id = int(box.id[0]) if box.id is not None else None
                    label    = f"{names[cls_id]} {conf_val:.0%}"
                    color    = class_color(cls_id)
                    draw_box(frame, x1, y1, x2, y2, label, color, track_id)
                    obj_count += 1

            fps_frames += 1
            elapsed = time.time() - fps_timer
            if elapsed >= 0.5:
                fps        = fps_frames / elapsed
                fps_frames = 0
                fps_timer  = time.time()
                self.on_fps_update(fps)
                self.on_count_update(obj_count)

            draw_overlay(frame, fps, obj_count, model_name, paused=False)
            cv2.imshow(WIN, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1:
                break
            if key == ord("p"):
                self._paused = True

        cap.release()
        cv2.destroyAllWindows()
        self.on_stop()


class ControlPanel:

    def __init__(self, root: tk.Tk):
        self.root    = root
        self.session: DetectionSession | None = None

        root.title(f"{APP_NAME} — {SUBTITLE} | CodeAlpha AI Internship Task 4")
        root.geometry("480x560")
        root.resizable(False, False)
        root.configure(bg=BG)

        self._build_ui()


    def _build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg=BG)
        hdr.pack(fill="x", padx=20, pady=(18, 6))

        tk.Label(
            hdr,
            text=f"🎯  {APP_NAME}",
            font=("Segoe UI", 22, "bold"),
            bg=BG, fg=ACCENT
        ).pack(side="left")

        tk.Label(
            hdr,
            text="CodeAlpha AI Internship — Task 4",
            font=("Segoe UI", 9),
            bg=BG, fg=SUBTEXT
        ).pack(side="right", anchor="s", pady=6)

        tk.Frame(self.root, bg=SURFACE, height=1).pack(fill="x", padx=20, pady=(0, 16))

        # ── Source selection ───────────────────
        self._section("📹  Video Source")

        src_frame = tk.Frame(self.root, bg=BG)
        src_frame.pack(fill="x", padx=24, pady=(4, 10))

        self.source_var = tk.StringVar(value="webcam")

        tk.Radiobutton(
            src_frame, text="Webcam  (index 0)",
            variable=self.source_var, value="webcam",
            bg=BG, fg=TEXT, selectcolor=SURFACE,
            activebackground=BG, activeforeground=ACCENT,
            font=("Segoe UI", 11),
            command=self._on_source_change
        ).pack(anchor="w")

        tk.Radiobutton(
            src_frame, text="Video File",
            variable=self.source_var, value="file",
            bg=BG, fg=TEXT, selectcolor=SURFACE,
            activebackground=BG, activeforeground=ACCENT,
            font=("Segoe UI", 11),
            command=self._on_source_change
        ).pack(anchor="w", pady=(4, 0))

        # File picker row
        file_row = tk.Frame(self.root, bg=BG)
        file_row.pack(fill="x", padx=24, pady=(2, 10))

        self.file_path_var = tk.StringVar(value="No file selected")
        self.file_label = tk.Label(
            file_row,
            textvariable=self.file_path_var,
            font=("Segoe UI", 9),
            bg=BG, fg=SUBTEXT,
            width=36, anchor="w"
        )
        self.file_label.pack(side="left")

        self.browse_btn = tk.Button(
            file_row,
            text="Browse…",
            font=("Segoe UI", 9),
            bg=SURFACE, fg=ACCENT,
            bd=0, padx=10, pady=4,
            cursor="hand2",
            state="disabled",
            command=self._browse_file
        )
        self.browse_btn.pack(side="left", padx=(8, 0))

        self._file_path: str | None = None

        # ── Model selection ────────────────────
        self._section("🧠  YOLO Model")

        self.model_var = tk.StringVar(value=list(MODELS.keys())[0])
        model_menu = ttk.Combobox(
            self.root,
            textvariable=self.model_var,
            values=list(MODELS.keys()),
            state="readonly",
            font=("Segoe UI", 11),
            width=34,
        )
        model_menu.pack(padx=24, pady=(4, 12), anchor="w")
        self._style_combobox(model_menu)

        # ── Confidence threshold ───────────────
        self._section("🎚️  Confidence Threshold")

        slider_row = tk.Frame(self.root, bg=BG)
        slider_row.pack(fill="x", padx=24, pady=(4, 14))

        self.conf_var = tk.DoubleVar(value=0.45)
        self.conf_label = tk.Label(
            slider_row,
            text="0.45",
            font=("Segoe UI", 12, "bold"),
            bg=BG, fg=YELLOW, width=5
        )
        self.conf_label.pack(side="right")

        slider = tk.Scale(
            slider_row,
            from_=0.10, to=0.90,
            resolution=0.05,
            orient="horizontal",
            variable=self.conf_var,
            bg=BG, fg=TEXT,
            troughcolor=SURFACE,
            highlightthickness=0,
            showvalue=False,
            command=self._on_conf_change,
            length=300,
        )
        slider.pack(side="left", fill="x", expand=True)

        # ── Live stats ─────────────────────────
        self._section("📊  Live Stats")

        stats_frame = tk.Frame(self.root, bg=SURFACE)
        stats_frame.pack(fill="x", padx=24, pady=(4, 14), ipady=10)

        self._stat_col(stats_frame, "FPS",     "fps_val",   "—",   TEAL,   0)
        self._stat_col(stats_frame, "Objects", "count_val", "—",   GREEN,  1)
        self._stat_col(stats_frame, "Status",  "status_val","Idle", YELLOW, 2)

        # ── Buttons ────────────────────────────
        btn_row = tk.Frame(self.root, bg=BG)
        btn_row.pack(fill="x", padx=24, pady=(6, 0))

        self.start_btn = tk.Button(
            btn_row,
            text="▶  Start Detection",
            font=("Segoe UI", 12, "bold"),
            bg=GREEN, fg="#1e1e2e",
            bd=0, padx=20, pady=10,
            cursor="hand2",
            command=self._start
        )
        self.start_btn.pack(side="left", expand=True, fill="x")

        self.stop_btn = tk.Button(
            btn_row,
            text="■  Stop",
            font=("Segoe UI", 12, "bold"),
            bg=RED, fg="#1e1e2e",
            bd=0, padx=20, pady=10,
            cursor="hand2",
            state="disabled",
            command=self._stop
        )
        self.stop_btn.pack(side="left", padx=(10, 0), expand=True, fill="x")

        # Footer
        tk.Frame(self.root, bg=SURFACE, height=1).pack(fill="x", padx=20, pady=(16, 0))
        tk.Label(
            self.root,
            text="[ P ] Pause / Resume   [ Q ] Quit detection window",
            font=("Segoe UI", 8),
            bg=BG, fg=SUBTEXT
        ).pack(pady=(4, 8))

    # ── Helper builders ────────────────────────

    def _section(self, title: str):
        tk.Label(
            self.root,
            text=title,
            font=("Segoe UI", 10, "bold"),
            bg=BG, fg=ACCENT
        ).pack(anchor="w", padx=20, pady=(6, 0))

    def _stat_col(self, parent, label, attr, value, color, col):
        frame = tk.Frame(parent, bg=SURFACE)
        frame.grid(row=0, column=col, padx=10, pady=6, sticky="nsew")
        parent.columnconfigure(col, weight=1)

        tk.Label(frame, text=label, font=("Segoe UI", 8),
                 bg=SURFACE, fg=SUBTEXT).pack()
        lbl = tk.Label(frame, text=value, font=("Segoe UI", 16, "bold"),
                       bg=SURFACE, fg=color)
        lbl.pack()
        setattr(self, attr, lbl)

    def _style_combobox(self, cb):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "TCombobox",
            fieldbackground=SURFACE,
            background=SURFACE,
            foreground=TEXT,
            selectbackground=SURFACE,
            selectforeground=ACCENT,
            borderwidth=0,
        )

    # ── Event handlers ─────────────────────────

    def _on_source_change(self):
        is_file = self.source_var.get() == "file"
        self.browse_btn.config(state="normal" if is_file else "disabled")

    def _browse_file(self):
        path = filedialog.askopenfilename(
            title="Select a video file",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv"),
                ("All files", "*.*")
            ]
        )
        if path:
            self._file_path = path
            short = path.split("/")[-1] if "/" in path else path.split("\\")[-1]
            self.file_path_var.set(short)

    def _on_conf_change(self, val):
        self.conf_label.config(text=f"{float(val):.2f}")

    # ── Session control ────────────────────────

    def _start(self):
        if not _YOLO_OK:
            messagebox.showerror(
                "Missing dependency",
                "ultralytics is not installed.\n\nRun:\n  pip install ultralytics"
            )
            return

        if self.source_var.get() == "file":
            if not self._file_path:
                messagebox.showwarning("No file", "Please select a video file first.")
                return
            source = self._file_path
        else:
            source = 0   # webcam

        model_path = MODELS[self.model_var.get()]
        conf       = self.conf_var.get()

        self.session = DetectionSession(
            source        = source,
            model_path    = model_path,
            conf          = conf,
            on_fps_update = self._update_fps,
            on_count_update = self._update_count,
            on_stop       = self._on_stopped,
        )
        self.session.start()

        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_val.config(text="Running", fg=GREEN)

    def _stop(self):
        if self.session:
            self.session.stop()

    def _on_stopped(self):
        self.root.after(0, self._reset_ui)

    def _reset_ui(self):
        self.session = None
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.fps_val.config(text="—")
        self.count_val.config(text="—")
        self.status_val.config(text="Idle", fg=YELLOW)

    def _update_fps(self, fps: float):
        self.root.after(0, lambda: self.fps_val.config(text=f"{fps:.1f}"))

    def _update_count(self, count: int):
        self.root.after(0, lambda: self.count_val.config(text=str(count)))


# ─────────────────────────────────────────────
#   ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app  = ControlPanel(root)
    root.mainloop()