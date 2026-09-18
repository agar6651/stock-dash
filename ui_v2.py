from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  --bg:#071321; --surface:#0D1B2A; --surface-soft:#102338; --line:#1C3550;
  --text:#E8F0F8; --muted:#8FA6BC; --blue:#2196F3; --blue-soft:#102E4A;
  --green:#21C79A; --red:#FF5B6E; --orange:#FFB45C;
}
html,body,[class*="css"]{font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif}
.stApp{background:var(--bg);color:var(--text)}
.block-container{max-width:1480px;padding-top:1.4rem;padding-bottom:4rem}
header[data-testid="stHeader"]{background:rgba(7,19,33,.88);backdrop-filter:blur(12px)}
section[data-testid="stSidebar"]{background:#081827;border-right:1px solid var(--line)}
section[data-testid="stSidebar"]>div{padding-top:.9rem}
[data-testid="stSidebar"] .stRadio>label{display:none}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"]{gap:.18rem}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{border-radius:10px;padding:.55rem .65rem;color:#A9BCD0;transition:all .15s ease}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{background:#10283E}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){background:#123A5E;color:#5DB5FF;font-weight:700}
h1,h2,h3,h4{color:var(--text);letter-spacing:-.035em}
h1{font-weight:800} h2,h3{font-weight:760}
p,li{line-height:1.62}
[data-testid="stCaptionContainer"]{color:var(--muted)}
[data-testid="stMetric"]{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:0 10px 30px rgba(0,0,0,.16)}
[data-testid="stMetricLabel"]{color:var(--muted)}
[data-testid="stMetricValue"]{color:var(--text);font-weight:750}
[data-testid="stVerticalBlockBorderWrapper"]{border-color:var(--line)!important;border-radius:15px!important;background:var(--surface);box-shadow:0 10px 30px rgba(0,0,0,.14)}
.stButton>button,.stFormSubmitButton>button{border-radius:10px;min-height:2.7rem;font-weight:700}
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"]{background:var(--blue);border-color:var(--blue)}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div{border-radius:10px!important;background:#0A1A2A;color:var(--text)}
.stTabs [data-baseweb="tab-list"]{gap:8px}
.stTabs [data-baseweb="tab"]{border-radius:9px;padding:8px 12px;color:var(--muted)}
.stDataFrame{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.planx-brand{display:flex;align-items:center;gap:10px;margin:2px 0 18px}
.planx-brand-mark{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#1689E8,#55B6FF);color:white;font-size:18px;font-weight:800}
.planx-brand-title{font-size:18px;line-height:1.15;font-weight:800;letter-spacing:-.03em;color:#E8F0F8}
.planx-brand-sub{font-size:10px;color:#6F879E;margin-top:2px}
.planx-hero{background:linear-gradient(135deg,#0D1B2A 0%,#0D2135 60%,#0D2943 100%);border:1px solid var(--line);border-radius:20px;padding:26px 28px;margin-bottom:18px;box-shadow:0 16px 42px rgba(0,0,0,.18)}
.planx-eyebrow{color:#55B6FF;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px}
.planx-hero h1{margin:0;font-size:34px;line-height:1.18}
.planx-hero p{margin:9px 0 0;color:#9CB0C3;font-size:14px}
.planx-card{background:#0D1B2A;border:1px solid var(--line);border-radius:14px;padding:17px 18px;min-height:116px;box-shadow:0 10px 30px rgba(0,0,0,.14)}
.planx-card-title{font-size:12px;color:#8FA6BC;margin-bottom:8px;font-weight:700}
.planx-card-value{font-size:22px;color:#E8F0F8;font-weight:800;letter-spacing:-.03em}
.planx-card-note{margin-top:7px;font-size:11px;color:#6F879E}
.planx-empty{background:#0D1B2A;border:1px dashed #294661;border-radius:14px;padding:22px;color:#8FA6BC}
.planx-source{display:inline-flex;align-items:center;gap:5px;color:#8FA6BC;background:#0A1A2A;border:1px solid #294661;padding:4px 8px;border-radius:999px;font-size:10px}
.planx-status-ok{color:#51E0B7;background:#0B2B27;border-color:#145B4D}
.planx-status-wait{color:#FFD08A;background:#30240F;border-color:#654B1B}
.planx-status-bad{color:#FF8C9A;background:#32151B;border-color:#6A2732}
hr{border-color:var(--line)!important}
.stApp [data-testid="stDataFrame"] div{background:#0D1B2A}
@media(max-width:900px){.block-container{padding-left:1rem;padding-right:1rem}.planx-hero{padding:22px 20px}.planx-hero h1{font-size:28px}}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">StockDash</div>
    <div class="planx-brand-sub">Data to Insight.</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#334155">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
