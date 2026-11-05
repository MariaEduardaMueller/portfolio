from pathlib import Path

import streamlit as st

# ----------------------------------------------------------------------------
# CONFIGURAÇÃO
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Maria Eduarda Mueller | Dados, QA e IA",
    page_icon="💻",
    layout="centered",
)

BASE = Path(__file__).parent
FOTO = BASE / "assets" / "foto.jpg"  # opcional: coloque sua foto aqui
CURRICULO = BASE / "assets" / "Maria_Mueller_Curriculo.pdf"

NOME = "Maria Eduarda Mueller"
EMAIL = "mariaeduardamueller1@gmail.com"
TELEFONE = "+55 51 99976-6840"
WHATSAPP = "https://wa.me/5551999766840"
LINKEDIN = "https://www.linkedin.com/in/maria-eduarda-mueller/"
GITHUB = ""  # ex.: "https://github.com/seu-usuario" (aparece só se preenchido)

# ----------------------------------------------------------------------------
# CONTEÚDO (edite aqui)
# ----------------------------------------------------------------------------
SOBRE = (
    "Estudante de Engenharia de Computação na UNISC, com experiência em análise e "
    "engenharia de dados, qualidade de software e inteligência artificial. "
    "Trabalho com Python, SQL, Power BI e serviços AWS, transformando dados em "
    "dashboards e soluções que apoiam decisões. Hoje também atuo em pesquisa "
    "científica com IA aplicada à saúde e crio testes e avaliações para chatbots "
    "baseados em LLMs."
)

EXPERIENCIAS = [
    {
        "cargo": "Bolsista de Iniciação Científica (PROBIC/FAPERGS)",
        "org": "Universidade de Santa Cruz do Sul (UNISC) · Presencial",
        "data": "10/2026 – atual",
        "itens": [
            "Pesquisa: “Diagnóstico de tuberculose utilizando imagens de emissão de "
            "plasma com Inteligência Artificial: estudo de validação”.",
            "Participação em pesquisa científica com IA aplicada à análise de imagens "
            "para apoio ao diagnóstico.",
            "Apoio ao desenvolvimento e uso de plataformas e ferramentas tecnológicas "
            "em outros projetos da universidade.",
        ],
    },
    {
        "cargo": "AI FDE Driven Quality Engineer (QA) – Estágio",
        "org": "AI/R · Remoto",
        "data": "08/2026 – 10/2026",
        "itens": [
            "Testes automatizados com Python e pytest; testes e validação de APIs REST "
            "com Postman, analisando resultados e apontando inconsistências.",
            "Uso de AWS Bedrock e Amazon Q Developer em práticas de Quality Engineering "
            "com apoio de IA.",
            "Criação de chatbots com LLMs e avaliação de modelos com LLM-as-a-Judge e "
            "DeepEval (qualidade, relevância, fidelidade e conformidade das respostas).",
        ],
    },
    {
        "cargo": "Analista de Dados – Estágio",
        "org": "Analítica 3M · Presencial",
        "data": "06/2025 – 10/2025",
        "itens": [
            "Análise e tratamento de dados vindos de APIs, ERPs, CRMs e bancos de "
            "dados, com SQL e Python.",
            "Dashboards interativos em Power BI para apoiar a tomada de decisão de "
            "clientes e casos reais.",
        ],
    },
    {
        "cargo": "AWS Cloud Data Engineer – Estágio",
        "org": "Compass UOL · Remoto",
        "data": "12/2024 – 05/2025",
        "itens": [
            "Processos de ingestão, transformação e processamento de dados na AWS.",
            "Soluções com Glue, Lambda, S3, Athena e QuickSight.",
            "Manipulação e transformação de dados com Python, SQL e Apache Spark.",
        ],
    },
]

# Troque "link" pelo endereço do repositório quando tiver um (deixe "" para ocultar)
PROJETOS = [
    {
        "titulo": "IA para apoio ao diagnóstico de tuberculose",
        "desc": "Pesquisa de iniciação científica que valida o uso de IA na análise de "
        "imagens de emissão de plasma.",
        "tags": ["IA", "Imagens", "Pesquisa"],
        "link": "",
    },
    {
        "titulo": "Chatbots com LLMs e avaliação automática",
        "desc": "Desenvolvimento de chatbots e avaliação das respostas com "
        "LLM-as-a-Judge e DeepEval.",
        "tags": ["LLMs", "DeepEval", "AWS Bedrock", "LangChain"],
        "link": "",
    },
    {
        "titulo": "Testes automatizados de APIs REST",
        "desc": "Automação com Python, pytest e requests, mais validação manual de "
        "endpoints no Postman.",
        "tags": ["Python", "pytest", "Postman"],
        "link": "",
    },
    {
        "titulo": "Dashboards e pipelines de dados",
        "desc": "Pipelines na AWS (Glue, Athena, S3) e painéis em Power BI e "
        "QuickSight.",
        "tags": ["SQL", "Spark", "Power BI", "AWS"],
        "link": "",
    },
]

HABILIDADES = {
    "Linguagens e dados": [
        "Python", "Java", "C", "SQL", "Pandas", "Apache Spark",
        "MySQL", "PostgreSQL", "NoSQL",
    ],
    "IA e qualidade": [
        "LLMs", "LangChain", "DeepEval", "LLM-as-a-Judge", "PyTorch",
        "TensorFlow", "Scikit-Learn", "Machine Learning", "pytest",
        "Testes de APIs", "Validação de dados",
    ],
    "Cloud e ferramentas": [
        "AWS S3", "AWS Glue", "AWS Athena", "AWS Lambda", "AWS QuickSight",
        "AWS Bedrock", "Amazon Q Developer", "Power BI", "Excel", "Postman",
        "Docker", "Git", "GitHub",
    ],
    "Interpessoais": [
        "Comunicação", "Trabalho em equipe", "Proatividade",
        "Inteligência emocional", "Pensamento lógico", "Resolução de problemas",
    ],
}

FORMACAO = {
    "curso": "Engenharia de Computação (Bacharelado)",
    "inst": "UNISC, Santa Cruz do Sul – RS",
    "data": "01/2023 – atual",
}

CERTIFICACOES = [
    ("AWS Certified Cloud Practitioner", "AWS", "2025"),
    ("GenAI, Dados & Cyber", "Bradesco (bootcamp)", "2026"),
]

IDIOMAS = [("Português", "Fluente"), ("Inglês", "Avançado"), ("Espanhol", "Básico")]

# ----------------------------------------------------------------------------
# ESTILO
# ----------------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Source+Sans+3:wght@400;600&display=swap');

:root {
  --ink: #16233B;
  --muted: #55627A;
  --bg: #F4F7F9;
  --surface: #FFFFFF;
  --line: #D5DFE5;
  --accent: #0E7C86;
  --tint: #DDEEF0;
}

html, body, [class*="css"], .stApp {
  font-family: 'Source Sans 3', sans-serif;
  color: var(--ink);
}
.stApp { background: var(--bg); }
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 860px; padding-top: 3rem; padding-bottom: 4rem; }

h1, h2, h3 { font-family: 'Bricolage Grotesque', sans-serif; color: var(--ink); }

.hero-name {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: clamp(2.6rem, 8vw, 4.6rem);
  line-height: 1.02;
  letter-spacing: -0.03em;
  margin: 0 0 0.6rem 0;
}
.hero-role {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--accent);
  margin-bottom: 1.1rem;
}
.hero-text { font-size: 1.12rem; line-height: 1.6; color: var(--muted); max-width: 62ch; }

.btn-row { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.4rem; }
.btn {
  display: inline-block; padding: 0.55rem 1.1rem; border-radius: 8px;
  border: 1.5px solid var(--ink); color: var(--ink) !important;
  text-decoration: none !important; font-weight: 600; font-size: 0.98rem;
  transition: background 0.15s, color 0.15s;
}
.btn:hover { background: var(--ink); color: #fff !important; }
.btn.primary { background: var(--accent); border-color: var(--accent); color: #fff !important; }
.btn.primary:hover { background: #0A5F67; border-color: #0A5F67; }

.sec-title {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.9rem; font-weight: 700; letter-spacing: -0.02em;
  margin: 3.2rem 0 1.2rem 0;
}

/* Experiência: é uma sequência no tempo, então usa linha do tempo */
.tl { border-left: 2px solid var(--line); margin-left: 6px; padding-left: 1.4rem; }
.tl-item { position: relative; padding-bottom: 1.8rem; }
.tl-item::before {
  content: ""; position: absolute; left: calc(-1.4rem - 7px); top: 0.45rem;
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--accent); border: 2px solid var(--bg);
}
.tl-head { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.2rem 1rem; }
.tl-role { font-family: 'Bricolage Grotesque', sans-serif; font-weight: 700; font-size: 1.15rem; }
.tl-date { color: var(--muted); font-size: 0.95rem; }
.tl-org { color: var(--accent); font-weight: 600; margin-bottom: 0.5rem; }
.tl-item ul { margin: 0; padding-left: 1.1rem; color: var(--muted); line-height: 1.55; }
.tl-item li { margin-bottom: 0.3rem; }

.card {
  background: var(--surface); border: 1px solid var(--line); border-radius: 10px;
  padding: 1.2rem 1.3rem; height: 100%;
}
.card-title { font-family: 'Bricolage Grotesque', sans-serif; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.4rem; }
.card-desc { color: var(--muted); line-height: 1.5; font-size: 0.98rem; margin-bottom: 0.8rem; }
.card a { color: var(--accent); font-weight: 600; text-decoration: none; }

.chip {
  display: inline-block; background: var(--tint); color: #0A4A51;
  border-radius: 6px; padding: 0.18rem 0.6rem; margin: 0 0.35rem 0.4rem 0;
  font-size: 0.88rem; font-weight: 600;
}
.chip.lg { background: var(--surface); border: 1px solid var(--line); color: var(--ink); font-size: 0.95rem; padding: 0.28rem 0.75rem; }
.skill-group { font-weight: 600; margin: 1.1rem 0 0.5rem 0; }

.row { display: flex; justify-content: space-between; gap: 1rem; padding: 0.7rem 0; border-bottom: 1px solid var(--line); }
.row:last-child { border-bottom: none; }
.row small { color: var(--muted); }

.contact a { color: var(--accent); font-weight: 600; text-decoration: none; }
.footer { margin-top: 4rem; color: var(--muted); font-size: 0.9rem; }

a:focus-visible, .btn:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
</style>
""",
    unsafe_allow_html=True,
)


def chips(items, large=False):
    cls = "chip lg" if large else "chip"
    return "".join(f'<span class="{cls}">{i}</span>' for i in items)


# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
botoes = [
    f'<a class="btn primary" href="mailto:{EMAIL}">Enviar e-mail</a>',
    f'<a class="btn" href="{LINKEDIN}" target="_blank">LinkedIn</a>',
]
if GITHUB:
    botoes.append(f'<a class="btn" href="{GITHUB}" target="_blank">GitHub</a>')
botoes_html = "".join(botoes)

hero_html = (
    f'<div class="hero-name">{NOME}</div>'
    '<div class="hero-role">Dados, qualidade de software e IA</div>'
    '<div class="hero-text">Estudante de Engenharia de Computação que transforma '
    "dados em decisões e testa sistemas de IA para que eles sejam confiáveis.</div>"
    f'<div class="btn-row">{botoes_html}</div>'
)

if FOTO.exists():
    c1, c2 = st.columns([1, 2.2], gap="large", vertical_alignment="center")
    with c1:
        st.image(str(FOTO), use_container_width=True)
    with c2:
        st.markdown(hero_html, unsafe_allow_html=True)
else:
    st.markdown(hero_html, unsafe_allow_html=True)

if CURRICULO.exists():
    st.write("")
    st.download_button(
        "Baixar currículo (PDF)",
        data=CURRICULO.read_bytes(),
        file_name="Maria_Eduarda_Mueller_Curriculo.pdf",
        mime="application/pdf",
    )

# ----------------------------------------------------------------------------
# SOBRE
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Sobre mim</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hero-text">{SOBRE}</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# EXPERIÊNCIA
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Experiência</div>', unsafe_allow_html=True)
itens_html = ""
for e in EXPERIENCIAS:
    lis = "".join(f"<li>{i}</li>" for i in e["itens"])
    itens_html += (
        '<div class="tl-item">'
        f'<div class="tl-head"><span class="tl-role">{e["cargo"]}</span>'
        f'<span class="tl-date">{e["data"]}</span></div>'
        f'<div class="tl-org">{e["org"]}</div>'
        f"<ul>{lis}</ul></div>"
    )
st.markdown(f'<div class="tl">{itens_html}</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# PROJETOS
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Projetos e frentes de trabalho</div>', unsafe_allow_html=True)
for i in range(0, len(PROJETOS), 2):
    cols = st.columns(2, gap="medium")
    for col, p in zip(cols, PROJETOS[i : i + 2]):
        link = (
            f'<a href="{p["link"]}" target="_blank">Ver no GitHub</a>' if p["link"] else ""
        )
        with col:
            st.markdown(
                '<div class="card">'
                f'<div class="card-title">{p["titulo"]}</div>'
                f'<div class="card-desc">{p["desc"]}</div>'
                f'{chips(p["tags"])}<div style="margin-top:0.4rem">{link}</div>'
                "</div>",
                unsafe_allow_html=True,
            )
    st.write("")

# ----------------------------------------------------------------------------
# HABILIDADES
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Habilidades</div>', unsafe_allow_html=True)
for grupo, lista in HABILIDADES.items():
    st.markdown(
        f'<div class="skill-group">{grupo}</div>{chips(lista, large=True)}',
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# FORMAÇÃO, CERTIFICAÇÕES E IDIOMAS
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Formação e certificações</div>', unsafe_allow_html=True)
certs = "".join(
    f'<div class="row"><div><b>{n}</b><br><small>{o}</small></div><small>{a}</small></div>'
    for n, o, a in CERTIFICACOES
)
st.markdown(
    '<div class="card">'
    f'<div class="row"><div><b>{FORMACAO["curso"]}</b><br><small>{FORMACAO["inst"]}</small></div>'
    f'<small>{FORMACAO["data"]}</small></div>'
    f"{certs}</div>",
    unsafe_allow_html=True,
)

st.markdown('<div class="sec-title">Idiomas</div>', unsafe_allow_html=True)
st.markdown(
    "".join(f'<span class="chip lg"><b>{i}</b> · {n}</span>' for i, n in IDIOMAS),
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# CONTATO
# ----------------------------------------------------------------------------
st.markdown('<div class="sec-title">Contato</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="contact hero-text">Aberta a oportunidades em dados, QA e IA. '
    "Fale comigo por:<br>"
    f'<a href="mailto:{EMAIL}">{EMAIL}</a><br>'
    f'<a href="{WHATSAPP}" target="_blank">WhatsApp: {TELEFONE}</a><br>'
    f'<a href="{LINKEDIN}" target="_blank">linkedin.com/in/maria-eduarda-mueller</a>'
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="footer">© 2026 {NOME} · Santa Cruz do Sul, RS</div>',
    unsafe_allow_html=True,
)
