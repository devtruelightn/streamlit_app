
"""
🧭 MBTI 진로 탐험소 (MBTI Career Explorer)
------------------------------------------
진로 교육용 Streamlit 웹앱
실행: streamlit run mbti_career_app.py
"""

import random
import streamlit as st

# ============================================================
# 0. 페이지 설정
# ============================================================
st.set_page_config(
    page_title="🧭 MBTI 진로 탐험소",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# 1. 스타일 (네온 우주 테마)
# ============================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gothic+A1:wght@300;500;700;900&display=swap');

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(124,58,237,.35) 0%, transparent 45%),
        radial-gradient(circle at 85% 15%, rgba(236,72,153,.30) 0%, transparent 45%),
        radial-gradient(circle at 50% 90%, rgba(34,211,238,.28) 0%, transparent 50%),
        linear-gradient(160deg, #06061a 0%, #0d0b2b 45%, #120a24 100%);
    background-attachment: fixed;
    color: #E9E6FF;
    font-family: 'Gothic A1', sans-serif;
}
h1, h2, h3, h4 { font-family: 'Jua', sans-serif !important; letter-spacing: .5px; }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(18,14,45,.96), rgba(10,8,28,.96));
    border-right: 1px solid rgba(167,139,250,.35);
}
section[data-testid="stSidebar"] * { color: #EDE9FE !important; }

/* ---------- 히어로 ---------- */
.hero {
    text-align: center; padding: 42px 18px 30px;
    border-radius: 32px; margin-bottom: 26px;
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(167,139,250,.35);
    box-shadow: 0 0 60px rgba(124,58,237,.35), inset 0 0 60px rgba(236,72,153,.08);
    position: relative; overflow: hidden;
}
.hero-title {
    font-family: 'Jua', sans-serif; font-size: 3.4rem; line-height: 1.15; margin: 0;
    background: linear-gradient(90deg,#FDE68A,#F472B6,#818CF8,#22D3EE,#FDE68A);
    background-size: 300% 100%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: flow 7s linear infinite;
    filter: drop-shadow(0 0 22px rgba(236,72,153,.55));
}
.hero-sub { font-size: 1.05rem; color: #C4B5FD; margin-top: 12px; font-weight: 500; }
.hero-emojis { font-size: 2rem; letter-spacing: 10px; margin-top: 14px; animation: bob 3.2s ease-in-out infinite; }
@keyframes flow { to { background-position: 300% 0; } }
@keyframes bob { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }

/* ---------- 유형 카드 ---------- */
.type-card {
    border-radius: 30px; padding: 34px 30px; margin-bottom: 22px;
    color: #fff; position: relative; overflow: hidden;
    box-shadow: 0 18px 55px rgba(0,0,0,.55);
    border: 1px solid rgba(255,255,255,.28);
}
.type-card::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(115deg, rgba(255,255,255,.30) 0%, transparent 42%);
    pointer-events: none;
}
.type-code { font-family:'Jua',sans-serif; font-size: 4.2rem; line-height: 1; margin: 0; text-shadow: 0 6px 22px rgba(0,0,0,.45); }
.type-nick { font-size: 1.5rem; font-weight: 900; margin-top: 6px; }
.type-tag { font-size: 1.05rem; opacity: .95; margin-top: 12px; line-height: 1.6; }
.type-face { font-size: 4.6rem; float: right; animation: bob 3.5s ease-in-out infinite; }
.chip {
    display: inline-block; padding: 7px 16px; margin: 6px 6px 0 0; border-radius: 999px;
    background: rgba(255,255,255,.22); border: 1px solid rgba(255,255,255,.4);
    font-size: .92rem; font-weight: 700; backdrop-filter: blur(6px);
}

/* ---------- 직업 카드 ---------- */
.job-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap: 16px; }
.job-card {
    background: rgba(255,255,255,.06); border: 1px solid rgba(167,139,250,.3);
    border-radius: 22px; padding: 20px 22px; transition: .25s ease; backdrop-filter: blur(8px);
}
.job-card:hover {
    transform: translateY(-7px) scale(1.02);
    border-color: rgba(244,114,182,.75);
    box-shadow: 0 16px 40px rgba(236,72,153,.35);
}
.job-top { display:flex; align-items:center; justify-content:space-between; }
.job-name { font-family:'Jua',sans-serif; font-size: 1.3rem; color:#fff; }
.job-emoji { font-size: 2.1rem; }
.job-score { font-family:'Jua',sans-serif; font-size:1.15rem; color:#FDE68A; }
.job-desc { font-size:.93rem; color:#CBC3F0; margin-top:10px; line-height:1.6; }
.bar { height: 11px; border-radius: 999px; background: rgba(255,255,255,.12); margin-top:12px; overflow:hidden; }
.bar-fill {
    height:100%; border-radius:999px;
    background: linear-gradient(90deg,#22D3EE,#818CF8,#F472B6,#FDE68A);
    background-size: 250% 100%; animation: flow 3.5s linear infinite, grow 1.1s ease-out;
    box-shadow: 0 0 16px rgba(244,114,182,.7);
}
@keyframes grow { from { width: 0 !important; } }

/* ---------- 정보 박스 ---------- */
.box {
    background: rgba(255,255,255,.05); border-radius: 22px; padding: 22px 24px;
    border: 1px solid rgba(167,139,250,.28); height: 100%;
}
.box h4 { margin: 0 0 12px 0; color:#FDE68A; font-size:1.2rem; }
.box ul { margin: 0; padding-left: 20px; }
.box li { margin: 8px 0; color:#DDD6FE; line-height:1.6; }

.step {
    display:flex; gap:16px; align-items:flex-start; padding:18px 20px; margin-bottom:12px;
    background: rgba(255,255,255,.05); border-left: 5px solid #F472B6; border-radius: 0 18px 18px 0;
}
.step-num { font-family:'Jua',sans-serif; font-size:1.8rem; color:#F472B6; min-width:46px; }
.step-body b { color:#FDE68A; font-size:1.05rem; }
.step-body p { margin:6px 0 0; color:#CBC3F0; line-height:1.6; }

.caution {
    margin-top: 34px; padding: 20px 24px; border-radius: 20px;
    background: rgba(253,230,138,.08); border: 1px dashed rgba(253,230,138,.55);
    color:#FDE68A; font-size:.93rem; line-height:1.75; text-align:center;
}

/* ---------- 위젯 ---------- */
.stButton > button {
    width: 100%; border-radius: 999px; border: none; padding: 12px 0;
    font-family:'Jua',sans-serif; font-size: 1.05rem; color:#1B0B2E;
    background: linear-gradient(90deg,#FDE68A,#F472B6,#818CF8);
    background-size: 200% 100%; transition:.3s;
    box-shadow: 0 8px 26px rgba(244,114,182,.45);
}
.stButton > button:hover { background-position: 100% 0; transform: translateY(-2px); color:#1B0B2E; }
.stTabs [data-baseweb="tab"] { font-family:'Jua',sans-serif; font-size:1.02rem; color:#C4B5FD; }
.stTabs [aria-selected="true"] { color:#FDE68A !important; }
div[data-testid="stMetricValue"] { font-family:'Jua',sans-serif; color:#FDE68A; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ============================================================
# 2. MBTI 데이터
# ============================================================
MBTI = {
    "INTJ": {
        "emoji": "🧠", "nick": "설계도를 품은 전략가", "grad": ("#7C3AED", "#2563EB"),
        "tag": "머릿속에 이미 10년 뒤 지도가 그려져 있는 사람. 큰 그림을 보고 조용히 실행합니다.",
        "keys": ["🎯 장기 비전", "🧩 구조적 사고", "🔒 독립성", "📐 높은 기준"],
        "strong": ["복잡한 문제를 구조로 정리해요", "혼자서도 끝까지 파고드는 집중력", "데이터로 미래를 예측하는 전략적 판단"],
        "watch": ["완벽하게 준비하려다 시작이 늦어질 수 있어요", "팀원의 감정을 살피는 연습이 필요해요"],
        "jobs": [
            ("🔭", "데이터 사이언티스트", 97, "데이터 속 패턴을 찾아 전략으로 바꾸는 일"),
            ("🧪", "연구원 · 과학자", 94, "가설을 세우고 오래 검증하는 몰입형 연구"),
            ("🏗️", "소프트웨어 아키텍트", 92, "거대한 시스템의 뼈대를 설계하는 역할"),
            ("📈", "전략기획 · 컨설턴트", 89, "기업의 방향을 숫자와 논리로 제안"),
            ("🎓", "대학교수 · 연구교수", 86, "자기 분야를 깊게 파고 후학을 기르는 길"),
        ],
        "majors": ["컴퓨터공학", "산업공학", "통계학", "물리학", "경영학"],
        "tip": "관심 분야 하나를 정해 6개월짜리 개인 프로젝트를 완주해보세요. 포트폴리오가 곧 무기가 됩니다.",
        "buddy": "ENFP",
    },
    "INTP": {
        "emoji": "🔬", "nick": "질문이 멈추지 않는 논리술사", "grad": ("#6D28D9", "#0EA5E9"),
        "tag": "\"왜 그렇지?\"가 입버릇인 사람. 원리를 이해할 때 가장 행복합니다.",
        "keys": ["❓ 호기심", "🧮 논리력", "🌀 아이디어", "🕰️ 몰입"],
        "strong": ["남들이 지나치는 허점을 발견해요", "새로운 개념을 빠르게 흡수해요", "규칙보다 원리를 이해하려 해요"],
        "watch": ["관심이 자주 바뀌어 마무리가 어려울 수 있어요", "생각을 말로 옮기는 연습이 필요해요"],
        "jobs": [
            ("💻", "소프트웨어 개발자", 96, "논리를 코드로 옮겨 세상을 움직이는 일"),
            ("🛡️", "정보보안 분석가", 93, "허점을 찾아내는 감각이 그대로 무기가 됨"),
            ("🧬", "기초과학 연구원", 91, "아무도 모르는 답을 처음 찾아내는 재미"),
            ("🎮", "게임 시스템 기획자", 88, "규칙과 밸런스를 설계하는 논리 게임"),
            ("📊", "AI · 머신러닝 엔지니어", 87, "모델의 원리를 파고들어 성능을 끌어올림"),
        ],
        "majors": ["컴퓨터공학", "수학", "물리학", "인공지능학과", "철학"],
        "tip": "아이디어를 노트에만 두지 말고 작게라도 '완성'해 보세요. 완성 경험이 실력을 증명합니다.",
        "buddy": "ENTJ",
    },
    "ENTJ": {
        "emoji": "👑", "nick": "판을 짜는 통솔자", "grad": ("#B91C1C", "#7C3AED"),
        "tag": "목표가 보이면 사람과 자원을 모아 길을 뚫는 사람. 리더 자리가 어색하지 않습니다.",
        "keys": ["🚩 리더십", "⚡ 추진력", "🗺️ 큰 그림", "🎤 설득력"],
        "strong": ["목표를 정하고 팀을 끌고 가요", "결정을 미루지 않아요", "비효율을 빠르게 잡아내요"],
        "watch": ["속도를 못 따라오는 사람을 기다려 주세요", "결과만큼 과정도 인정해 주면 좋아요"],
        "jobs": [
            ("🏢", "경영자 · 창업가", 96, "조직을 만들고 방향을 정하는 자리"),
            ("💼", "경영 컨설턴트", 94, "문제 기업을 진단하고 해법을 설계"),
            ("⚖️", "변호사 · 법조인", 91, "논리와 설득으로 승부하는 무대"),
            ("📉", "투자 · 금융 애널리스트", 89, "숫자로 미래를 판단하고 베팅하는 일"),
            ("🧭", "프로덕트 매니저", 87, "제품의 목표와 우선순위를 결정"),
        ],
        "majors": ["경영학", "경제학", "법학", "정치외교학", "산업공학"],
        "tip": "학급·동아리에서 '기획부터 마무리까지' 책임지는 경험을 한 번은 꼭 해보세요.",
        "buddy": "INTP",
    },
    "ENTP": {
        "emoji": "💡", "nick": "아이디어 폭죽 발명가", "grad": ("#EA580C", "#DB2777"),
        "tag": "가능성을 보면 일단 던져보는 사람. 토론과 실험에서 에너지를 얻습니다.",
        "keys": ["🎆 창의성", "🗣️ 순발력", "🔁 도전", "🤹 다재다능"],
        "strong": ["새로운 조합을 잘 떠올려요", "낯선 상황에서도 당황하지 않아요", "사람을 설득하는 말솜씨가 있어요"],
        "watch": ["시작한 일을 끝내는 습관이 필요해요", "반박이 습관이 되지 않게 조심해요"],
        "jobs": [
            ("🚀", "스타트업 창업가", 96, "없던 시장을 만들어 내는 모험"),
            ("📣", "브랜드 · 광고 기획자", 93, "사람 마음을 흔드는 메시지 설계"),
            ("🎬", "방송 PD · 콘텐츠 기획", 91, "매번 새로운 기획으로 승부"),
            ("🧑‍🚀", "신사업 개발 담당", 88, "회사 안에서 새 아이템을 발굴"),
            ("🎙️", "크리에이터 · 강연자", 86, "말과 아이디어가 곧 자산이 되는 일"),
        ],
        "majors": ["경영학", "미디어커뮤니케이션", "광고홍보학", "융합공학", "심리학"],
        "tip": "아이디어 3개보다 완성한 결과물 1개가 강합니다. 마감일을 스스로 정해보세요.",
        "buddy": "INFJ",
    },
    "INFJ": {
        "emoji": "🕊️", "nick": "마음을 읽는 통찰가", "grad": ("#0D9488", "#4F46E5"),
        "tag": "말하지 않은 것까지 알아채는 사람. 의미 있는 일에 조용히 헌신합니다.",
        "keys": ["🌌 통찰", "💗 공감", "✍️ 표현력", "🧘 신념"],
        "strong": ["사람의 감정 변화를 잘 알아차려요", "깊이 있는 글과 말로 표현해요", "가치 있는 일에 오래 헌신해요"],
        "watch": ["혼자 감정을 떠안지 말고 나눠요", "완벽한 이상과 현실의 거리를 인정해요"],
        "jobs": [
            ("🛋️", "상담심리사", 96, "사람의 마음을 함께 정리해 주는 일"),
            ("📖", "작가 · 에디터", 93, "생각을 문장으로 오래 남기는 직업"),
            ("🏫", "교사 · 교육 기획자", 91, "학생의 성장을 설계하는 역할"),
            ("🤲", "사회복지사 · NGO 활동가", 88, "제도 밖 사람들을 살피는 일"),
            ("🎨", "전시 · 콘텐츠 큐레이터", 85, "메시지를 경험으로 번역하는 작업"),
        ],
        "majors": ["심리학", "교육학", "국어국문학", "사회복지학", "문화콘텐츠학"],
        "tip": "생각을 기록하는 습관을 만드세요. 당신의 글은 그 자체로 진로 포트폴리오가 됩니다.",
        "buddy": "ENTP",
    },
    "INFP": {
        "emoji": "🌈", "nick": "마음속 세계를 짓는 중재자", "grad": ("#7C3AED", "#EC4899"),
        "tag": "상상과 가치를 중요하게 여기는 사람. 진심이 담긴 일에서 힘이 납니다.",
        "keys": ["🌱 진정성", "🎨 상상력", "🫂 배려", "📚 몰입"],
        "strong": ["남다른 감수성과 표현력이 있어요", "타인의 입장을 잘 헤아려요", "좋아하는 일엔 놀랄 만큼 몰두해요"],
        "watch": ["비판을 개인 공격으로 받아들이지 않기", "완벽한 조건을 기다리다 놓치지 않기"],
        "jobs": [
            ("✒️", "시나리오 · 웹툰 스토리 작가", 95, "감정을 이야기로 만드는 창작 직업"),
            ("🖌️", "일러스트레이터 · 디자이너", 93, "세계관을 시각으로 표현하는 일"),
            ("💬", "심리상담 · 예술치료사", 90, "예술과 대화로 마음을 돌보는 직업"),
            ("🌏", "번역가 · 통번역 작가", 87, "언어 사이의 결을 옮기는 섬세한 작업"),
            ("🎼", "음악 · 사운드 크리에이터", 85, "감정을 소리로 설계하는 일"),
        ],
        "majors": ["문예창작학", "심리학", "시각디자인", "영어영문학", "예술치료학"],
        "tip": "완성작을 온라인에 꾸준히 올려보세요. 취향이 쌓이면 그게 브랜드가 됩니다.",
        "buddy": "ENFJ",
    },
    "ENFJ": {
        "emoji": "🌟", "nick": "사람을 키우는 선도자", "grad": ("#059669", "#0EA5E9"),
        "tag": "다른 사람의 가능성을 먼저 알아보는 사람. 함께 성장할 때 가장 빛납니다.",
        "keys": ["🤗 친화력", "🎤 전달력", "🧭 이끔", "❤️ 책임감"],
        "strong": ["분위기를 부드럽게 이끌어요", "말로 사람을 움직여요", "약속과 역할을 끝까지 지켜요"],
        "watch": ["남을 챙기다 자기 일정을 놓치지 않기", "모두를 만족시킬 순 없다는 걸 기억하기"],
        "jobs": [
            ("👩‍🏫", "교사 · 진로진학 상담교사", 97, "학생의 방향을 함께 찾아주는 직업"),
            ("🎤", "강사 · 교육 콘텐츠 기획자", 94, "배움을 재미있게 전달하는 일"),
            ("🧑‍💼", "인사(HR) · 조직문화 담당", 91, "사람이 잘 일하도록 판을 만드는 역할"),
            ("📢", "홍보 · 커뮤니케이션 매니저", 88, "조직의 이야기를 세상에 전하는 일"),
            ("📺", "아나운서 · 진행자", 86, "목소리와 태도로 신뢰를 주는 직업"),
        ],
        "majors": ["교육학", "심리학", "미디어커뮤니케이션", "경영학(인사)", "사회학"],
        "tip": "가르쳐 본 경험이 최고의 스펙입니다. 또래 멘토링이나 스터디 리더를 맡아보세요.",
        "buddy": "INFP",
    },
    "ENFP": {
        "emoji": "🎉", "nick": "가능성을 퍼뜨리는 활동가", "grad": ("#F59E0B", "#EC4899"),
        "tag": "사람과 아이디어를 연결하는 사람. 새로운 자극이 곧 연료입니다.",
        "keys": ["✨ 에너지", "🌐 연결력", "🎈 유연함", "💞 공감"],
        "strong": ["처음 보는 사람과도 금방 친해져요", "아이디어를 신나게 확산시켜요", "변화를 두려워하지 않아요"],
        "watch": ["반복 업무에서 쉽게 지칠 수 있어요", "일정 관리 도구의 도움을 받아보세요"],
        "jobs": [
            ("📱", "콘텐츠 크리에이터 · 마케터", 96, "취향과 트렌드를 콘텐츠로 만드는 일"),
            ("🎪", "이벤트 · 페스티벌 기획자", 93, "사람을 모으고 경험을 설계하는 직업"),
            ("✈️", "여행 · 관광 상품 기획자", 90, "새로운 장소와 이야기를 파는 일"),
            ("🎭", "배우 · 방송인", 87, "표현력과 순발력이 곧 실력인 무대"),
            ("🤝", "브랜드 매니저 · 홍보 담당", 86, "브랜드의 목소리를 만드는 역할"),
        ],
        "majors": ["미디어커뮤니케이션", "광고홍보학", "관광경영학", "연극영화학", "경영학"],
        "tip": "관심사가 많은 건 단점이 아니에요. 세 가지를 섞은 나만의 조합을 콘텐츠로 만들어보세요.",
        "buddy": "INTJ",
    },
    "ISTJ": {
        "emoji": "📋", "nick": "약속을 지키는 현실주의자", "grad": ("#1D4ED8", "#334155"),
        "tag": "맡은 일은 정확하게 끝내는 사람. 신뢰가 가장 큰 자산입니다.",
        "keys": ["✅ 성실함", "🔎 정확성", "📏 원칙", "🗂️ 정리력"],
        "strong": ["디테일을 놓치지 않아요", "계획을 세우고 그대로 실행해요", "책임감이 매우 강해요"],
        "watch": ["갑작스러운 변화에 유연해지는 연습", "새로운 방식도 한 번쯤 시도해보기"],
        "jobs": [
            ("🧾", "회계사 · 세무사", 96, "숫자의 정확성이 곧 실력인 전문직"),
            ("🏛️", "공무원 · 행정직", 93, "제도와 절차를 정확히 운영하는 일"),
            ("🔍", "품질관리(QA) 엔지니어", 91, "기준에 맞는지 끝까지 검증하는 역할"),
            ("🗄️", "데이터 · 정보 관리자", 88, "자료를 안전하고 정확하게 지키는 일"),
            ("⚖️", "법무 · 노무 전문가", 86, "규정을 해석하고 적용하는 직업"),
        ],
        "majors": ["회계학", "행정학", "법학", "경영학", "산업공학"],
        "tip": "꾸준함이 가장 큰 무기예요. 자격증 로드맵을 학년별로 나눠 계획해보세요.",
        "buddy": "ESFP",
    },
    "ISFJ": {
        "emoji": "🛡️", "nick": "곁을 지키는 수호자", "grad": ("#0891B2", "#14B8A6"),
        "tag": "티 내지 않고 챙기는 사람. 누군가에게 꼭 필요한 존재가 됩니다.",
        "keys": ["🤍 배려", "🧷 꼼꼼함", "🕯️ 헌신", "🧺 실용성"],
        "strong": ["사람의 필요를 먼저 알아채요", "맡은 일을 세심하게 마무리해요", "오래 신뢰를 쌓아요"],
        "watch": ["거절하는 연습도 필요해요", "자기 성과를 표현해도 괜찮아요"],
        "jobs": [
            ("🩺", "간호사 · 의료기사", 96, "가까이에서 사람을 돌보는 전문직"),
            ("🧒", "초등교사 · 유아교육", 93, "아이의 하루를 세심하게 살피는 일"),
            ("🥗", "영양사 · 식품영양 전문가", 90, "건강을 설계하고 관리하는 직업"),
            ("📚", "사서 · 기록물 관리사", 87, "지식을 정리하고 지키는 역할"),
            ("🦵", "물리치료사 · 재활 전문가", 86, "회복 과정을 함께 걷는 직업"),
        ],
        "majors": ["간호학", "초등교육", "식품영양학", "문헌정보학", "물리치료학"],
        "tip": "봉사·돌봄 활동 기록을 꼼꼼히 남겨두세요. 진정성이 그대로 드러납니다.",
        "buddy": "ESTP",
    },
    "ESTJ": {
        "emoji": "🏛️", "nick": "질서를 세우는 관리자", "grad": ("#B45309", "#1E40AF"),
        "tag": "해야 할 일을 정리하고 굴러가게 만드는 사람. 조직이 필요로 하는 중심축입니다.",
        "keys": ["📊 조직력", "⏱️ 실행력", "🧱 원칙", "🗣️ 직설적"],
        "strong": ["일의 순서를 명확히 정해요", "책임을 회피하지 않아요", "성과를 눈에 보이게 만들어요"],
        "watch": ["표현을 조금 부드럽게 다듬기", "다른 방식도 있다는 걸 인정하기"],
        "jobs": [
            ("🏭", "생산 · 운영 관리자", 95, "사람과 공정을 효율적으로 굴리는 일"),
            ("🚓", "경찰 · 소방 간부", 92, "규율과 판단이 필요한 현장 리더"),
            ("🏦", "은행 · 금융 관리직", 90, "규정과 성과를 함께 관리하는 직무"),
            ("📐", "프로젝트 관리자(PM)", 88, "일정·예산·인력을 통제하는 역할"),
            ("🎖️", "군 장교 · 공공 관리직", 86, "명확한 체계 안에서 성장하는 길"),
        ],
        "majors": ["경영학", "행정학", "산업공학", "경찰행정학", "물류학"],
        "tip": "리더 경험을 숫자로 기록해두세요. '몇 명, 얼마 기간, 어떤 결과'가 설득력을 만듭니다.",
        "buddy": "ISFP",
    },
    "ESFJ": {
        "emoji": "🤝", "nick": "분위기를 살리는 조력자", "grad": ("#DB2777", "#F97316"),
        "tag": "사람들 사이의 온도를 맞추는 사람. 함께 있을 때 가장 잘합니다.",
        "keys": ["😊 친절함", "🎀 협동", "📞 소통", "🎁 센스"],
        "strong": ["팀 분위기를 좋게 만들어요", "필요한 걸 미리 챙겨요", "사람을 기억하고 관계를 이어가요"],
        "watch": ["모두에게 좋은 사람이 되려 애쓰지 않기", "비판에 너무 오래 흔들리지 않기"],
        "jobs": [
            ("🛫", "승무원 · 서비스 매니저", 95, "사람을 편안하게 만드는 전문 서비스"),
            ("🏥", "간호사 · 보건 교사", 93, "돌봄과 소통이 함께 필요한 직업"),
            ("🎊", "이벤트 · 웨딩 코디네이터", 90, "사람의 특별한 날을 완성하는 일"),
            ("🛍️", "영업 · 고객경험(CX) 담당", 88, "관계로 성과를 만드는 직무"),
            ("🧸", "유아교사 · 아동 지도사", 86, "따뜻함이 곧 전문성이 되는 현장"),
        ],
        "majors": ["간호학", "관광경영학", "아동학", "경영학(마케팅)", "호텔외식경영"],
        "tip": "사람을 상대하는 아르바이트·봉사 경험이 큰 자산이 됩니다. 에피소드를 기록해두세요.",
        "buddy": "ISFP",
    },
    "ISTP": {
        "emoji": "🔧", "nick": "손으로 푸는 만능 장인", "grad": ("#475569", "#0EA5E9"),
        "tag": "설명서보다 직접 뜯어보는 사람. 고장 난 걸 고칠 때 눈이 반짝입니다.",
        "keys": ["🛠️ 손재주", "🧊 침착함", "🏍️ 실전형", "🎯 효율"],
        "strong": ["위기 상황에서 침착해요", "직접 해보며 빠르게 익혀요", "불필요한 절차를 줄여요"],
        "watch": ["장기 계획도 조금씩 세워보기", "생각을 말로 공유하는 습관"],
        "jobs": [
            ("🤖", "로봇 · 메카트로닉스 엔지니어", 95, "기계와 제어를 다루는 실전 공학"),
            ("✈️", "항공 정비사 · 파일럿", 93, "정밀함과 판단력이 필요한 현장"),
            ("🚒", "소방관 · 응급구조사", 91, "위기 상황에서 빛나는 직업"),
            ("🔌", "전기 · 자동차 정비 기술자", 89, "손끝의 기술이 곧 경쟁력"),
            ("🛰️", "드론 · 무인장비 운용 전문가", 86, "새로운 장비를 다루는 기술 직군"),
        ],
        "majors": ["기계공학", "전기전자공학", "항공정비학", "자동차공학", "응급구조학"],
        "tip": "만들고 고친 것을 사진·영상으로 남기세요. 기술 직군은 결과물이 곧 이력서입니다.",
        "buddy": "ESFJ",
    },
    "ISFP": {
        "emoji": "🎨", "nick": "감각으로 말하는 예술가", "grad": ("#DB2777", "#8B5CF6"),
        "tag": "말보다 결과물로 표현하는 사람. 색, 소리, 맛의 차이를 알아챕니다.",
        "keys": ["🌸 감각", "🕊️ 온화함", "🎧 몰입", "🧵 손끝"],
        "strong": ["미세한 차이를 구별하는 감각", "자기만의 스타일이 분명해요", "조용히 오래 몰입해요"],
        "watch": ["자기 작업을 알리는 것도 실력이에요", "마감 관리 도구를 활용해보세요"],
        "jobs": [
            ("🖼️", "그래픽 · 제품 디자이너", 95, "감각을 형태로 만드는 직업"),
            ("👨‍🍳", "요리사 · 파티시에", 93, "맛과 플레이팅으로 표현하는 예술"),
            ("📷", "사진작가 · 영상 감독", 91, "순간을 프레임에 담는 일"),
            ("💄", "메이크업 · 헤어 아티스트", 88, "사람을 캔버스로 삼는 감각 직업"),
            ("🌿", "플로리스트 · 공간 스타일리스트", 86, "공간의 분위기를 설계하는 일"),
        ],
        "majors": ["시각디자인", "조리외식경영", "사진영상학", "패션디자인", "원예학"],
        "tip": "작업물을 모아 포트폴리오 계정을 만들어보세요. 꾸준함이 실력을 증명합니다.",
        "buddy": "ESTJ",
    },
    "ESTP": {
        "emoji": "🏄", "nick": "지금을 사는 승부사", "grad": ("#DC2626", "#F59E0B"),
        "tag": "생각보다 몸이 먼저 움직이는 사람. 현장에서 실력이 폭발합니다.",
        "keys": ["⚡ 순발력", "🔥 도전", "🗣️ 대담함", "🏆 승부욕"],
        "strong": ["빠르게 판단하고 바로 실행해요", "낯선 사람 앞에서도 당당해요", "위기를 즐길 줄 알아요"],
        "watch": ["결정 전에 3초만 더 생각해보기", "꾸준히 반복하는 훈련도 중요해요"],
        "jobs": [
            ("🏋️", "스포츠 트레이너 · 감독", 95, "몸과 현장을 다루는 실전 직업"),
            ("🚑", "응급의료 · 구조 전문가", 92, "1초가 중요한 현장의 판단자"),
            ("🤝", "영업 · 비즈니스 개발", 90, "사람을 만나 성과를 만드는 일"),
            ("👮", "경찰관 · 특수직 공무원", 88, "현장 대응력이 곧 능력인 직군"),
            ("🎥", "현장 리포터 · 스포츠 캐스터", 85, "순발력과 표현력이 무기인 직업"),
        ],
        "majors": ["체육학", "경찰행정학", "응급구조학", "경영학(마케팅)", "미디어커뮤니케이션"],
        "tip": "대회·공모전처럼 결과가 바로 나오는 도전을 자주 해보세요. 경험이 곧 성장입니다.",
        "buddy": "ISFJ",
    },
    "ESFP": {
        "emoji": "🎤", "nick": "무대를 밝히는 분위기메이커", "grad": ("#F59E0B", "#EF4444"),
        "tag": "사람들 앞에서 더 살아나는 사람. 즐거움을 만드는 재능이 있습니다.",
        "keys": ["🎈 유쾌함", "🎬 표현력", "👐 친화력", "🌞 현재형"],
        "strong": ["처음 만난 사람도 편하게 해줘요", "표현과 리액션이 풍부해요", "분위기를 즉석에서 살려요"],
        "watch": ["장기 계획을 짧게라도 세워보기", "지루한 기본기도 실력이 돼요"],
        "jobs": [
            ("🎭", "배우 · 방송인 · 크리에이터", 95, "표현력이 그대로 직업이 되는 길"),
            ("🎙️", "행사 MC · 아나운서", 92, "무대 위에서 사람을 이끄는 일"),
            ("💇", "헤어 · 뷰티 디자이너", 90, "감각과 소통이 함께 필요한 직업"),
            ("🗺️", "여행 가이드 · 리조트 매니저", 88, "즐거운 경험을 설계하는 일"),
            ("🏃", "생활체육 지도자 · 댄서", 86, "몸으로 에너지를 전하는 직업"),
        ],
        "majors": ["연극영화학", "실용음악과", "미용예술학", "관광경영학", "체육학"],
        "tip": "무대·영상 경험을 아카이빙하세요. 짧은 영상 하나가 오디션 자료가 됩니다.",
        "buddy": "ISTJ",
    },
}

GROUP = {
    "분석형 NT 🧪": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "외교형 NF 💚": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "관리형 SJ 🛡️": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "탐험형 SP 🎨": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

QUESTIONS = [
    ("🎪 쉬는 시간, 나는?", "친구들과 어울리며 에너지 충전 🗣️", "혼자 조용히 쉬는 게 편함 🎧", "E", "I"),
    ("🌟 처음 간 모임에서 나는?", "먼저 말을 거는 편 👋", "누가 말 걸어주길 기다림 🙂", "E", "I"),
    ("📚 새로운 걸 배울 때 나는?", "실제 사례와 경험부터 확인 🔍", "전체 개념과 원리부터 이해 💭", "S", "N"),
    ("🗺️ 여행 계획을 짤 때 나는?", "구체적인 동선과 맛집 위주 📍", "어떤 느낌의 여행일지 상상 ✨", "S", "N"),
    ("⚖️ 친구가 고민을 말할 때 나는?", "해결책부터 정리해 줌 🧩", "먼저 공감하고 들어줌 🫂", "T", "F"),
    ("🤔 결정을 내릴 때 나는?", "논리와 근거가 우선 📊", "사람들의 마음이 우선 💗", "T", "F"),
    ("📅 과제를 할 때 나는?", "미리 계획 세워 차근차근 ✅", "마감 직전 몰아서 폭발 🔥", "J", "P"),
    ("🎒 내 방/가방 상태는?", "정해진 자리에 정리되어 있음 🗂️", "필요한 건 어딘가에 있음 🌀", "J", "P"),
]


# ============================================================
# 3. 렌더링 함수
# ============================================================
def hero():
    st.markdown(
        '<div class="hero">'
        '<h1 class="hero-title">🧭 MBTI 진로 탐험소 🚀</h1>'
        '<div class="hero-sub">16가지 성격 유형으로 떠나는 나의 미래 직업 탐험 ✨ 진로 수업용 웹앱</div>'
        '<div class="hero-emojis">🧠 🎨 🔧 🌟 💡 🛡️ 🎤 📋 🔬 🎉</div>'
        "</div>",
        unsafe_allow_html=True,
    )


def type_card(code):
    d = MBTI[code]
    c1, c2 = d["grad"]
    chips = "".join(f'<span class="chip">{k}</span>' for k in d["keys"])
    st.markdown(
        f'<div class="type-card" style="background:linear-gradient(135deg,{c1},{c2});">'
        f'<div class="type-face">{d["emoji"]}</div>'
        f'<div class="type-code">{code}</div>'
        f'<div class="type-nick">{d["emoji"]} {d["nick"]}</div>'
        f'<div class="type-tag">{d["tag"]}</div>'
        f"<div style='margin-top:16px'>{chips}</div>"
        "</div>",
        unsafe_allow_html=True,
    )


def job_grid(code):
    cards = []
    for emoji, name, score, desc in MBTI[code]["jobs"]:
        cards.append(
            '<div class="job-card">'
            '<div class="job-top">'
            f'<span class="job-emoji">{emoji}</span>'
            f'<span class="job-score">적합도 {score}%</span>'
            "</div>"
            f'<div class="job-name" style="margin-top:8px">{name}</div>'
            f'<div class="bar"><div class="bar-fill" style="width:{score}%"></div></div>'
            f'<div class="job-desc">{desc}</div>'
            "</div>"
        )
    st.markdown(f'<div class="job-grid">{"".join(cards)}</div>', unsafe_allow_html=True)


def info_box(title, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="box"><h4>{title}</h4><ul>{lis}</ul></div>'


def roadmap(code):
    d = MBTI[code]
    steps = [
        ("1", "🔎 탐색하기", f'추천 직업 중 끌리는 2개를 골라 하루 일과·필요 역량·연봉을 조사해 보세요. (워크넷 · 커리어넷 활용)'),
        ("2", "🧪 경험하기", f'관련 동아리, 봉사, 온라인 강의, 직업 체험을 한 학기에 하나씩 실행해 보세요.'),
        ("3", "📂 기록하기", f'{d["tip"]}'),
        ("4", "🎓 연결하기", f'관련 학과: {" · ".join(d["majors"])} — 대학 학과 소개와 교육과정을 직접 비교해 보세요.'),
    ]
    html = ""
    for n, t, b in steps:
        html += (
            '<div class="step">'
            f'<div class="step-num">{n}</div>'
            f'<div class="step-body"><b>{t}</b><p>{b}</p></div>'
            "</div>"
        )
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# 4. 사이드바 — 유형 선택
# ============================================================
if "code" not in st.session_state:
    st.session_state.code = "ENFP"

with st.sidebar:
    st.markdown("## 🎛️ 탐험 준비하기")
    mode = st.radio("어떻게 찾을까요? 🤔", ["🔤 내 MBTI 직접 고르기", "📝 간단 테스트로 찾기"])

    if mode == "🔤 내 MBTI 직접 고르기":
        group = st.selectbox("1️⃣ 성향 그룹 🌈", list(GROUP.keys()))
        picked = st.selectbox("2️⃣ 유형 선택 ✨", GROUP[group],
                              format_func=lambda c: f"{MBTI[c]['emoji']} {c} · {MBTI[c]['nick']}")
        if st.button("🚀 진로 추천 받기"):
            st.session_state.code = picked
            st.session_state.celebrate = True
        if st.button("🎲 랜덤 유형 구경하기"):
            st.session_state.code = random.choice(list(MBTI))
    else:
        st.caption("8개 질문에 답하면 유형이 나와요 ✏️")
        answers = []
        for i, (q, a, b, la, lb) in enumerate(QUESTIONS):
            pick = st.radio(f"**{i+1}. {q}**", [a, b], key=f"q{i}")
            answers.append(la if pick == a else lb)
        if st.button("✅ 결과 확인하기"):
            ei = "E" if answers[0:2].count("E") >= answers[0:2].count("I") else "I"
            sn = "S" if answers[2:4].count("S") >= answers[2:4].count("N") else "N"
            tf = "T" if answers[4:6].count("T") >= answers[4:6].count("F") else "F"
            jp = "J" if answers[6:8].count("J") >= answers[6:8].count("P") else "P"
            st.session_state.code = ei + sn + tf + jp
            st.session_state.celebrate = True

    st.markdown("---")
    st.markdown(
        "### 💌 선생님께\n"
        "- 수업 도입: 유형 맞히기 게임 🎮\n"
        "- 활동지: 추천 직업 2개 조사하기 📝\n"
        "- 마무리: 친구 유형과 협업 토론 🤝"
    )

# ============================================================
# 5. 메인 화면
# ============================================================
hero()

code = st.session_state.code
data = MBTI[code]

if st.session_state.pop("celebrate", False):
    st.balloons()

type_card(code)

m1, m2, m3, m4 = st.columns(4)
m1.metric("🏆 최고 적합 직업", data["jobs"][0][1])
m2.metric("📊 추천 직업 수", f'{len(data["jobs"])}개')
m3.metric("🤝 찰떡궁합 유형", f'{MBTI[data["buddy"]]["emoji"]} {data["buddy"]}')
m4.metric("🎓 추천 계열", data["majors"][0])

st.markdown("### ")

tab1, tab2, tab3, tab4 = st.tabs(
    ["💼 추천 직업 TOP 5", "💪 강점 & 보완점", "🗺️ 진로 로드맵", "🌍 16유형 전체 보기"]
)

with tab1:
    st.markdown(f"#### {data['emoji']} {code}에게 어울리는 직업들 ✨")
    job_grid(code)
    st.markdown(
        f'<div class="caution">💡 적합도는 성격 유형의 <b>일반적 경향</b>을 바탕으로 한 참고 수치예요. '
        "직업은 흥미 · 가치관 · 능력 · 환경을 함께 봐야 합니다! 🌱</div>",
        unsafe_allow_html=True,
    )

with tab2:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(info_box("💪 나의 강점", data["strong"]), unsafe_allow_html=True)
    with c2:
        st.markdown(info_box("🌱 더 키우면 좋은 점", data["watch"]), unsafe_allow_html=True)
    st.markdown("### ")
    b = data["buddy"]
    st.markdown(
        info_box(
            f"🤝 함께하면 시너지 나는 유형 — {MBTI[b]['emoji']} {b}",
            [
                f"{b}는 <b>{MBTI[b]['nick']}</b> 유형이에요.",
                f"{MBTI[b]['tag']}",
                "서로 다른 강점을 가진 친구와 팀을 이루면 결과물의 완성도가 올라갑니다! 🚀",
            ],
        ),
        unsafe_allow_html=True,
    )

with tab3:
    st.markdown(f"#### 🗺️ {code}를 위한 4단계 진로 로드맵")
    roadmap(code)
    st.markdown(
        info_box("🎓 관심 가져볼 학과", [f"{m}" for m in data["majors"]]),
        unsafe_allow_html=True,
    )

with tab4:
    st.markdown("#### 🌍 16가지 유형 한눈에 보기")
    for gname, codes in GROUP.items():
        st.markdown(f"##### {gname}")
        cols = st.columns(4)
        for col, c in zip(cols, codes):
            d = MBTI[c]
            g1, g2 = d["grad"]
            with col:
                st.markdown(
                    f'<div class="job-card" style="background:linear-gradient(135deg,{g1},{g2});border:none;text-align:center">'
                    f'<div style="font-size:2.4rem">{d["emoji"]}</div>'
                    f'<div class="job-name">{c}</div>'
                    f'<div style="font-size:.85rem;color:#fff;opacity:.9;margin-top:6px">{d["nick"]}</div>'
                    f'<div style="font-size:.85rem;color:#FDE68A;margin-top:10px">🏆 {d["jobs"][0][1]}</div>'
                    "</div>",
                    unsafe_allow_html=True,
                )
        st.markdown(" ")

st.markdown(
    '<div class="caution">'
    "🧭 <b>진로 교육 안내</b> — MBTI는 나를 이해하는 여러 도구 중 <b>하나</b>일 뿐이에요. "
    "유형이 진로를 정해주지 않습니다. 여기 없는 직업도, 다른 유형의 직업도 얼마든지 잘할 수 있어요! 🌟<br>"
    "더 정확한 진로 탐색은 <b>커리어넷 직업흥미검사</b>, <b>워크넷 직업적성검사</b>와 함께 해보세요 📚"
    "</div>",
    unsafe_allow_html=True,
)
