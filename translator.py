# ============================================================
#   Language Translation Tool
#   CodeAlpha AI Internship — Task 1
#   Built with: Python, Tkinter, deep-translator
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ─────────────────────────────────────────────
#   SUPPORTED LANGUAGES
# ─────────────────────────────────────────────
LANGUAGES = {
    "Auto Detect"        : "auto",
    "English"            : "en",
    "Hindi"              : "hi",
    "Telugu"             : "te",
    "Marathi"            : "mr",
    "Tamil"              : "ta",
    "Kannada"            : "kn",
    "Gujarati"           : "gu",
    "Bengali"            : "bn",
    "Punjabi"            : "pa",
    "Urdu"               : "ur",
    "French"             : "fr",
    "Spanish"            : "es",
    "German"             : "de",
    "Italian"            : "it",
    "Portuguese"         : "pt",
    "Russian"            : "ru",
    "Arabic"             : "ar",
    "Chinese (Simplified)": "zh-CN",
    "Japanese"           : "ja",
    "Korean"             : "ko",
}

LANG_NAMES = list(LANGUAGES.keys())

# ─────────────────────────────────────────────
#   CORE FUNCTIONS
# ─────────────────────────────────────────────

def translate_text():
    """Reads input, calls GoogleTranslator, displays output."""
    source_text = input_box.get("1.0", tk.END).strip()

    if not source_text:
        messagebox.showwarning("Empty Input", "Please enter some text to translate.")
        return

    src_code = LANGUAGES[source_var.get()]
    tgt_code = LANGUAGES[target_var.get()]

    if tgt_code == "auto":
        messagebox.showwarning("Invalid Target", "Please select a valid target language (not Auto Detect).")
        return

    if src_code == tgt_code:
        messagebox.showinfo("Same Language", "Source and target languages are the same.")
        return

    try:
        translate_btn.config(text="Translating...", state="disabled")
        root.update_idletasks()

        translator = GoogleTranslator(source=src_code, target=tgt_code)
        result = translator.translate(source_text)

        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state="disabled")

        status_label.config(text=f"✅  Translated: {source_var.get()}  →  {target_var.get()}", fg="#a6e3a1")

    except Exception as e:
        messagebox.showerror("Translation Failed", f"Error:\n{str(e)}\n\nCheck your internet connection.")
        status_label.config(text="❌  Translation failed.", fg="#f38ba8")

    finally:
        translate_btn.config(text="Translate ➜", state="normal")


def copy_output():
    """Copies translated text to clipboard."""
    text = output_box.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        status_label.config(text="📋  Copied to clipboard!", fg="#89b4fa")
    else:
        messagebox.showwarning("Nothing to Copy", "Translate something first.")


def clear_all():
    """Clears both input and output boxes."""
    input_box.delete("1.0", tk.END)
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")
    status_label.config(text="", fg="#cdd6f4")


def swap_languages():
    """Swaps source and target language selection."""
    src = source_var.get()
    tgt = target_var.get()
    if src == "Auto Detect":
        messagebox.showinfo("Swap", "Cannot swap when source is Auto Detect.")
        return
    source_var.set(tgt)
    target_var.set(src)


# ─────────────────────────────────────────────
#   UI SETUP
# ─────────────────────────────────────────────

# Colors (Catppuccin Mocha dark theme)
BG       = "#1e1e2e"
SURFACE  = "#313244"
TEXT     = "#cdd6f4"
SUBTEXT  = "#a6adc8"
ACCENT   = "#89b4fa"
GREEN    = "#a6e3a1"
RED      = "#f38ba8"
YELLOW   = "#f9e2af"

root = tk.Tk()
root.title("Language Translation Tool — CodeAlpha")
root.geometry("760x580")
root.resizable(False, False)
root.configure(bg=BG)

# ── Header ──────────────────────────────────
header_frame = tk.Frame(root, bg=BG)
header_frame.pack(fill="x", padx=24, pady=(20, 6))

tk.Label(
    header_frame,
    text="🌐  Language Translation Tool",
    font=("Segoe UI", 18, "bold"),
    bg=BG, fg=ACCENT
).pack(side="left")

tk.Label(
    header_frame,
    text="CodeAlpha AI Internship — Task 1",
    font=("Segoe UI", 9),
    bg=BG, fg=SUBTEXT
).pack(side="right", anchor="s", pady=4)

tk.Frame(root, bg=SURFACE, height=1).pack(fill="x", padx=24, pady=(0, 14))

# ── Language Selector Row ───────────────────
lang_frame = tk.Frame(root, bg=BG)
lang_frame.pack(fill="x", padx=24, pady=(0, 12))

# Source
tk.Label(lang_frame, text="From", font=("Segoe UI", 10, "bold"), bg=BG, fg=SUBTEXT).grid(row=0, column=0, sticky="w")
source_var = tk.StringVar(value="Auto Detect")
source_dropdown = ttk.Combobox(
    lang_frame, textvariable=source_var,
    values=LANG_NAMES, state="readonly",
    width=22, font=("Segoe UI", 10)
)
source_dropdown.grid(row=1, column=0, padx=(0, 10))

# Swap button
swap_btn = tk.Button(
    lang_frame, text="⇄", font=("Segoe UI", 13, "bold"),
    bg=SURFACE, fg=YELLOW, bd=0, cursor="hand2",
    activebackground=SURFACE, activeforeground=YELLOW,
    command=swap_languages
)
swap_btn.grid(row=1, column=1, padx=8)

# Target
tk.Label(lang_frame, text="To", font=("Segoe UI", 10, "bold"), bg=BG, fg=SUBTEXT).grid(row=0, column=2, sticky="w")
target_var = tk.StringVar(value="Hindi")
target_dropdown = ttk.Combobox(
    lang_frame, textvariable=target_var,
    values=LANG_NAMES[1:],  # exclude Auto Detect from target
    state="readonly", width=22, font=("Segoe UI", 10)
)
target_dropdown.grid(row=1, column=2, padx=(10, 0))

# ── Text Areas ──────────────────────────────
text_frame = tk.Frame(root, bg=BG)
text_frame.pack(fill="both", expand=True, padx=24, pady=(0, 8))

# Input
tk.Label(text_frame, text="Enter Text", font=("Segoe UI", 10, "bold"), bg=BG, fg=TEXT).grid(row=0, column=0, sticky="w", pady=(0, 4))
input_box = tk.Text(
    text_frame, width=40, height=10,
    font=("Segoe UI", 11), bg=SURFACE, fg=TEXT,
    insertbackground=TEXT, relief="flat",
    padx=10, pady=8, wrap="word",
    selectbackground=ACCENT, selectforeground=BG
)
input_box.grid(row=1, column=0, padx=(0, 10))

# Output
tk.Label(text_frame, text="Translated Text", font=("Segoe UI", 10, "bold"), bg=BG, fg=TEXT).grid(row=0, column=1, sticky="w", pady=(0, 4))
output_box = tk.Text(
    text_frame, width=40, height=10,
    font=("Segoe UI", 11), bg=SURFACE, fg=GREEN,
    insertbackground=GREEN, relief="flat",
    padx=10, pady=8, wrap="word",
    state="disabled",
    selectbackground=GREEN, selectforeground=BG
)
output_box.grid(row=1, column=1)

# ── Button Row ──────────────────────────────
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=10)

translate_btn = tk.Button(
    btn_frame, text="Translate ➜",
    font=("Segoe UI", 11, "bold"),
    bg=ACCENT, fg=BG, bd=0, padx=18, pady=8,
    cursor="hand2", activebackground="#74c7ec", activeforeground=BG,
    command=translate_text
)
translate_btn.pack(side="left", padx=8)

copy_btn = tk.Button(
    btn_frame, text="📋 Copy",
    font=("Segoe UI", 11),
    bg=SURFACE, fg=TEXT, bd=0, padx=14, pady=8,
    cursor="hand2", activebackground="#45475a", activeforeground=TEXT,
    command=copy_output
)
copy_btn.pack(side="left", padx=8)

clear_btn = tk.Button(
    btn_frame, text="🗑 Clear",
    font=("Segoe UI", 11),
    bg=SURFACE, fg=RED, bd=0, padx=14, pady=8,
    cursor="hand2", activebackground="#45475a", activeforeground=RED,
    command=clear_all
)
clear_btn.pack(side="left", padx=8)

# ── Status Bar ──────────────────────────────
tk.Frame(root, bg=SURFACE, height=1).pack(fill="x", padx=24, pady=(4, 0))
status_label = tk.Label(
    root, text="",
    font=("Segoe UI", 9), bg=BG, fg=TEXT
)
status_label.pack(pady=(4, 10))

# ── Style the dropdowns ─────────────────────
style = ttk.Style()
style.theme_use("default")
style.configure(
    "TCombobox",
    fieldbackground=SURFACE,
    background=SURFACE,
    foreground=TEXT,
    selectbackground=ACCENT,
    selectforeground=BG,
    arrowcolor=TEXT,
    borderwidth=0
)

# ── Run ─────────────────────────────────────
root.mainloop()