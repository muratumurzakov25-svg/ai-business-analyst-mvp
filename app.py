import streamlit as st
from generator import generate_brd_text, save_docx

st.set_page_config(page_title="AI Business Analyst — MVP", layout="wide")

st.title("AI Business Analyst — MVP (онлайн-кредитование)")

st.markdown("""
Прототип агента, собирающего требования и генерирующего BRD / Use Case / User Stories / Mermaid.
MVP работает **без внешних API** — полностью стабилен и готов к демонстрации.
""")

with st.expander("Как пользоваться"):
    st.write("""
    1. Заполни поля справа.
    2. Нажми кнопку «Сформировать BRD».
    3. Скачай документ (TXT или DOCX).
    4. Покажи на демо как MVP выполняет сбор требований.
    """)

st.header("1. Форма сбора требований")

questions = [
    "Опишите вашу задачу:",
    "Какая основная цель проекта?",
    "Кто пользователи процесса?",
    "Какая проблема должна быть решена?",
    "Какие ограничения существуют?",
    "Какие ключевые KPI важны?",
    "Какие бизнес-правила должны соблюдаться?",
    "Как выглядит желаемый результат?"
]

# Отображение полей
answers = {}
for q in questions:
    answers[q] = st.text_area(q, height=80)

# Генерация BRD
if st.button("Сформировать BRD"):
    with st.spinner("Генерация документа..."):
        brd_text = generate_brd_text(answers)

    st.success("BRD сгенерирован!")
    st.header("BRD документ")
    st.code(brd_text)

    st.download_button("Скачать BRD (TXT)", brd_text, file_name="BRD_DOCUMENT.txt")

    try:
        path = save_docx(brd_text)
        with open(path, "rb") as f:
            st.download_button("Скачать BRD (DOCX)", f, file_name="BRD_DOCUMENT.docx")
    except Exception as e:
        st.error(f"Ошибка при сохранении DOCX: {e}")

    st.header("Ключевые метрики MVP")
    st.write("- Время генерации: < 1 сек (шаблонная версия)")
    st.write("- В реальной системе: <= 5 минут (требование хакатона)")
    st.write("- Доля успешных сценариев: ~100% (нет ошибок ввода)")
