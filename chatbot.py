# ============================================================
#   ARIA — Advanced Technical FAQ Chatbot
#   CodeAlpha AI Internship — Task 2  (Upgraded)
#
#   Architecture:
#     Layer 1  →  TF-IDF + Cosine Similarity (offline FAQ bank)
#     Layer 2  →  Claude claude-sonnet-4-20250514 API (dynamic fallback)
#
#   Install dependencies:
#     pip install nltk scikit-learn anthropic
#
#   Set your API key once (terminal):
#     Windows:  set ANTHROPIC_API_KEY=sk-ant-...
#     Mac/Linux: export ANTHROPIC_API_KEY=sk-ant-...
#   OR paste it directly in the API_KEY variable below (dev only).
# ============================================================

import tkinter as tk
from tkinter import scrolledtext
import threading
import nltk
import string
import os

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── Optional: hard-code key here for local dev only ─────────
API_KEY = "sk-ant-api03-xxx"   # leave "" to force env var

try:
    import anthropic
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False

from faqs import FAQ_DATA

# ─────────────────────────────────────────────
#   NLTK bootstrap
# ─────────────────────────────────────────────
for pkg in ("stopwords", "punkt", "punkt_tab"):
    nltk.download(pkg, quiet=True)

# ─────────────────────────────────────────────
#   NLP ENGINE  — Layer 1
# ─────────────────────────────────────────────

stemmer    = PorterStemmer()
stop_words = set(stopwords.words("english"))

DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "🤖 AI / ML":          ["ai","ml","model","train","learn","neural","deep","predict"],
    "🐍 Python":           ["python","pip","list","dict","class","def","lambda","pandas","numpy"],
    "🗄️ Databases":        ["sql","database","query","table","join","index","nosql","mongo"],
    "🌐 Web Dev":          ["html","css","javascript","react","node","api","rest","http","dom"],
    "☕ Java":             ["java","jvm","class","oop","spring","jdk","thread","exception"],
    "🔗 Networking":       ["network","tcp","ip","dns","http","router","protocol","packet"],
    "🖥️ Operating Systems":["os","process","thread","memory","kernel","linux","unix","shell"],
    "☁️ Cloud":            ["cloud","aws","azure","gcp","docker","kubernetes","devops","ci"],
    "🔒 Cybersecurity":    ["security","encryption","hash","ssl","tls","firewall","xss","sql injection"],
    "📊 Data Science":     ["data","statistics","visualization","pandas","matplotlib","notebook"],
}

def detect_domain(text: str) -> str:
    lower = text.lower()
    scores: dict[str, int] = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for kw in keywords if kw in lower)
    best = max(scores, key=scores.get)  # type: ignore[arg-type]
    return best if scores[best] > 0 else "💬 General Tech"


def preprocess(text: str) -> str:
    text   = text.lower()
    text   = text.translate(str.maketrans("", "", string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [stemmer.stem(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)


faq_questions  = [item["question"] for item in FAQ_DATA]
faq_answers    = [item["answer"]   for item in FAQ_DATA]
processed_faqs = [preprocess(q)    for q    in faq_questions]

# Bigram-aware TF-IDF for better phrase matching
vectorizer   = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(processed_faqs)

FAQ_THRESHOLD = 0.20    # above → answer from FAQ bank
API_THRESHOLD = 0.10    # below → definitely use Claude API


def faq_lookup(user_input: str) -> tuple[str | None, float]:
    """Return (answer, score) from FAQ bank, or (None, score) if below threshold."""
    processed   = preprocess(user_input)
    vec         = vectorizer.transform([processed])
    sims        = cosine_similarity(vec, tfidf_matrix).flatten()
    best_idx    = int(sims.argmax())
    best_score  = float(sims[best_idx])
    if best_score >= FAQ_THRESHOLD:
        return faq_answers[best_idx], best_score
    return None, best_score


# ─────────────────────────────────────────────
#   CLAUDE API  — Layer 2
# ─────────────────────────────────────────────

SYSTEM_PROMPT = (
    "You are ARIA (AI Research & Information Assistant), an expert technical chatbot. "
    "You answer questions about programming, software engineering, data science, "
    "machine learning, databases, networking, operating systems, cloud, and cybersecurity. "
    "Give clear, accurate, concise answers (3–6 sentences max unless a longer list is needed). "
    "Use simple language. If the question is completely unrelated to technology, "
    "politely say you specialise in technical topics only."
)


def ask_claude(user_input: str) -> str:
    """Call Claude API and return the answer string."""
    if not _ANTHROPIC_AVAILABLE:
        return (
            "⚠️  The `anthropic` package is not installed.\n"
            "Run:  pip install anthropic\n"
            "Then restart the chatbot."
        )
    key = API_KEY or os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        return (
            "⚠️  No API key found.\n"
            "Set your key:\n"
            "  Windows → set ANTHROPIC_API_KEY=sk-ant-...\n"
            "  Mac/Linux → export ANTHROPIC_API_KEY=sk-ant-...\n"
            "Or paste it in the API_KEY variable inside chatbot.py."
        )
    try:
        client = anthropic.Anthropic(api_key=key)
        msg    = client.messages.create(
            model      = "claude-sonnet-4-20250514",
            max_tokens = 512,
            system     = SYSTEM_PROMPT,
            messages   = [{"role": "user", "content": user_input}],
        )
        return msg.content[0].text.strip()
    except anthropic.AuthenticationError:
        return "⚠️  Invalid API key. Please check your ANTHROPIC_API_KEY."
    except anthropic.RateLimitError:
        return "⚠️  Rate limit hit. Please wait a moment and try again."
    except Exception as exc:
        return f"⚠️  API error: {exc}"


# ─────────────────────────────────────────────
#   ROUTING LOGIC
# ─────────────────────────────────────────────

GREETINGS = {"hi", "hello", "hey", "hii", "helo", "sup", "yo", "howdy"}
FAREWELLS = {"bye", "goodbye", "exit", "quit", "thanks", "thank you", "thankyou"}
BOT_NAME  = "ARIA"


def route(user_input: str) -> tuple[str, str, str]:
    """
    Returns (reply, source_label, domain).
    source_label: 'faq' | 'claude' | 'greeting' | 'farewell'
    """
    lower  = user_input.lower().strip("!?.")
    domain = detect_domain(user_input)

    if lower in GREETINGS:
        return (
            f"👋 Hello! I'm {BOT_NAME} — your Advanced Technical Assistant.\n\n"
            "I can answer anything about:\n"
            "  • AI, ML, Deep Learning, NLP\n"
            "  • Python, Java, Web Dev, Databases\n"
            "  • Networking, OS, Cloud, Cybersecurity\n\n"
            "Powered by TF-IDF FAQ matching + Claude AI for any question I haven't seen before. "
            "Ask away!",
            "greeting", "👋 Welcome"
        )

    if lower in FAREWELLS:
        return (
            f"👋 Thanks for chatting! Keep building cool things. — {BOT_NAME}",
            "farewell", "👋 Goodbye"
        )

    # Layer 1 — FAQ
    faq_answer, score = faq_lookup(user_input)
    if faq_answer:
        return faq_answer, "faq", domain

    # Layer 2 — Claude
    claude_answer = ask_claude(user_input)
    return claude_answer, "claude", domain


# ─────────────────────────────────────────────
#   UI CONSTANTS
# ─────────────────────────────────────────────

BG      = "#1e1e2e"
SURFACE = "#313244"
TEXT    = "#cdd6f4"
SUBTEXT = "#a6adc8"
ACCENT  = "#89b4fa"
GREEN   = "#a6e3a1"
YELLOW  = "#f9e2af"
RED     = "#f38ba8"
PURPLE  = "#cba6f7"
TEAL    = "#94e2d5"

TYPING_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


# ─────────────────────────────────────────────
#   UI LOGIC
# ─────────────────────────────────────────────

_typing_job = None
_typing_idx = 0
_typing_marker = None


def _animate_typing():
    global _typing_job, _typing_idx
    if _typing_marker is None:
        return
    chat_box.config(state="normal")
    # overwrite the typing line
    chat_box.delete(_typing_marker, f"{_typing_marker} lineend")
    frame = TYPING_FRAMES[_typing_idx % len(TYPING_FRAMES)]
    chat_box.insert(_typing_marker, f"  {frame}  ARIA is thinking…", "typing_tag")
    chat_box.config(state="disabled")
    _typing_idx += 1
    _typing_job = root.after(120, _animate_typing)


def _start_typing():
    global _typing_marker, _typing_idx
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "\n", "")
    _typing_marker = chat_box.index(tk.END)
    chat_box.insert(tk.END, "  ⠋  ARIA is thinking…\n", "typing_tag")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)
    _typing_idx = 0
    _animate_typing()


def _stop_typing():
    global _typing_job, _typing_marker
    if _typing_job:
        root.after_cancel(_typing_job)
        _typing_job = None
    if _typing_marker:
        chat_box.config(state="normal")
        # delete from marker to end of that line + newline
        chat_box.delete(f"{_typing_marker} -1c linestart", f"{_typing_marker} lineend +1c")
        chat_box.config(state="disabled")
        _typing_marker = None


def append_message(sender: str, message: str, color: str, badge: str = ""):
    chat_box.config(state="normal")
    header = f"\n{sender}"
    if badge:
        header += f"  {badge}"
    chat_box.insert(tk.END, header + "\n", f"sender_{color}")
    chat_box.insert(tk.END, f"{message}\n\n", f"msg_{color}")
    chat_box.tag_config(f"sender_{color}", foreground=color,
                        font=("Segoe UI", 9, "bold"))
    chat_box.tag_config(f"msg_{color}",    foreground=TEXT,
                        font=("Segoe UI", 11),
                        lmargin1=14, lmargin2=14, rmargin=14)
    chat_box.config(state="disabled")
    chat_box.see(tk.END)


def _do_route(user_text: str):
    """Runs in background thread — calls route(), then updates UI via root.after."""
    reply, source, domain = route(user_text)

    def update_ui():
        _stop_typing()
        if source == "faq":
            badge = f"[FAQ ✓]  {domain}"
            color = GREEN
        elif source == "claude":
            badge = f"[Claude AI ✨]  {domain}"
            color = TEAL
        else:
            badge = ""
            color = GREEN
        append_message(BOT_NAME, reply, color, badge)
        send_btn.config(state="normal")
        input_field.config(state="normal")
        input_field.focus()

    root.after(0, update_ui)


def send_message(event=None):
    user_text = input_field.get().strip()
    if not user_text:
        return

    input_field.delete(0, tk.END)
    input_field.config(state="disabled")
    send_btn.config(state="disabled")

    append_message("You", user_text, PURPLE)
    _start_typing()

    t = threading.Thread(target=_do_route, args=(user_text,), daemon=True)
    t.start()


def clear_chat():
    chat_box.config(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.config(state="disabled")
    show_welcome()


def show_welcome():
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "\n")
    chat_box.insert(
        tk.END,
        f"  {BOT_NAME} — Advanced Technical Assistant\n",
        "welcome_title"
    )
    chat_box.insert(
        tk.END,
        (
            f"  Powered by TF-IDF FAQ Bank ({len(FAQ_DATA)} Q&As) + Claude AI Fallback\n\n"
            "  Topics I cover:\n"
            "  🤖 AI / ML / Deep Learning / NLP\n"
            "  🐍 Python / Java / C++ / Web Dev\n"
            "  🗄️  SQL / NoSQL Databases\n"
            "  🌐 HTML / CSS / JavaScript / React\n"
            "  ☁️  Cloud / Docker / DevOps / CI-CD\n"
            "  🔒 Cybersecurity / Networking / OS\n\n"
            "  Type any technical question and press Enter!\n\n"
        ),
        "welcome_body"
    )
    chat_box.tag_config("welcome_title", foreground=ACCENT,
                        font=("Segoe UI", 14, "bold"), lmargin1=10)
    chat_box.tag_config("welcome_body",  foreground=SUBTEXT,
                        font=("Segoe UI", 10), lmargin1=10)
    chat_box.tag_config("typing_tag",    foreground=YELLOW,
                        font=("Segoe UI", 10, "italic"))
    chat_box.config(state="disabled")


# ─────────────────────────────────────────────
#   BUILD ROOT WINDOW
# ─────────────────────────────────────────────

root = tk.Tk()
root.title(f"{BOT_NAME} — Advanced Technical Chatbot | CodeAlpha AI Internship Task 2")
root.geometry("720x640")
root.resizable(False, False)
root.configure(bg=BG)

# ── Header ──────────────────────────────────
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=20, pady=(16, 6))

tk.Label(
    header,
    text=f"🤖  {BOT_NAME} — Advanced Technical Chatbot",
    font=("Segoe UI", 16, "bold"),
    bg=BG, fg=ACCENT
).pack(side="left")

tk.Label(
    header,
    text="CodeAlpha AI Internship — Task 2",
    font=("Segoe UI", 9),
    bg=BG, fg=SUBTEXT
).pack(side="right", anchor="s", pady=4)

tk.Frame(root, bg=SURFACE, height=1).pack(fill="x", padx=20, pady=(0, 8))

# ── Chat Window ─────────────────────────────
chat_box = scrolledtext.ScrolledText(
    root,
    font=("Segoe UI", 11),
    bg=SURFACE, fg=TEXT,
    bd=0, relief="flat",
    state="disabled",
    wrap="word",
    padx=10, pady=10,
    insertbackground=TEXT,
)
chat_box.pack(fill="both", expand=True, padx=20)

# ── Input Row ───────────────────────────────
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill="x", padx=20, pady=12)

input_field = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg=SURFACE, fg=TEXT,
    insertbackground=TEXT,
    relief="flat", bd=0
)
input_field.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
input_field.bind("<Return>", send_message)

send_btn = tk.Button(
    input_frame,
    text="Send ➜",
    font=("Segoe UI", 11, "bold"),
    bg=ACCENT, fg=BG,
    bd=0, padx=14, pady=6,
    cursor="hand2",
    activebackground="#74c7ec", activeforeground=BG,
    command=send_message
)
send_btn.pack(side="left")

clear_btn = tk.Button(
    input_frame,
    text="🗑",
    font=("Segoe UI", 12),
    bg=SURFACE, fg=RED,
    bd=0, padx=10, pady=6,
    cursor="hand2",
    activebackground="#45475a", activeforeground=RED,
    command=clear_chat
)
clear_btn.pack(side="left", padx=(6, 0))

# ── Status bar ──────────────────────────────
tk.Frame(root, bg=SURFACE, height=1).pack(fill="x", padx=20)

status_var = tk.StringVar()
api_status = (
    "✅ Claude AI ready"
    if (API_KEY or os.environ.get("ANTHROPIC_API_KEY")) and _ANTHROPIC_AVAILABLE
    else "⚠️  Set ANTHROPIC_API_KEY for AI fallback"
)
status_var.set(
    f"FAQ Bank: {len(FAQ_DATA)} Q&As  |  {api_status}  |  "
    "TF-IDF bigrams + Cosine Similarity"
)
tk.Label(
    root,
    textvariable=status_var,
    font=("Segoe UI", 8),
    bg=BG, fg=SUBTEXT
).pack(pady=(4, 8))

# ── Launch ──────────────────────────────────
show_welcome()
input_field.focus()
root.mainloop()