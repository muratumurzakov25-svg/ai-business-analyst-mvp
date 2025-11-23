from datetime import datetime
import textwrap

def generate_brd_text(answers: dict) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    header = f"BRD: Онлайн-кредитование\nДата: {now}\n\n"

    def section(title, body):
        return f"## {title}\n{body}\n\n"

    desc = answers.get("Опишите вашу задачу:", "")
    goal = answers.get("Какая основная цель проекта?", "")
    users = answers.get("Кто пользователи процесса?", "")
    problem = answers.get("Какая проблема должна быть решена?", "")
    constraints = answers.get("Какие ограничения существуют?", "")
    kpi = answers.get("Какие ключевые KPI важны?", "")
    rules = answers.get("Какие бизнес-правила должны соблюдаться?", "")
    result = answers.get("Как выглядит желаемый результат?", "")

    scope_in = (
        "- Сбор требований через чат\n"
        "- Генерация BRD\n"
        "- Создание Use Case\n"
        "- Создание User Stories\n"
        "- Генерация Mermaid-диаграммы"
    )

    scope_out = (
        "- Интеграция с CoreBanking (вне MVP)\n"
        "- Полная автоматизация кредитного решения\n"
        "- Юридическая экспертиза"
    )

    user_stories = "\n".join([
        "- As a client, I want to apply online so that I avoid visiting a branch.",
        "- As a system, I must validate identity to prevent fraud.",
        "- As a risk manager, I want complete data for analysis.",
        "- As a PO, I want consistent BRD for dev team.",
        "- As a client, I want instant decision.",
        "- As a system, I must log all actions."
    ])

    use_case = textwrap.dedent("""
    Use Case: Онлайн-оформление кредита

    Actors: Клиент, Скоринговая система, CRM

    Preconditions:
    - Клиент имеет доступ в интернет.
    - Система аутентификации работает.

    Main Flow:
    1. Клиент заполняет заявку.
    2. Система проверяет корректность данных.
    3. Система отправляет данные в скоринг.
    4. Скоринг возвращает рейтинг.
    5. Система принимает решение.
    6. Клиент подписывает договор онлайн.
    7. Система активирует кредит.

    Alternative Flows:
    - A1: Ошибка в данных → запрос на исправление.
    - A2: Низкий скоринг → отказ или лимит ниже.

    Postconditions:
    - Заявка сохранена в CRM.
    - Логи записаны.
    """)

    mermaid = textwrap.dedent("""
    flowchart TD
        A[Клиент] --> B[Заполнение заявки]
        B --> C[Проверка данных]
        C -->|OK| D[Скоринг]
        C -->|Ошибка| E[Сообщение клиенту]
        D --> F{Одобрено?}
        F -->|Да| G[Формирование договора]
        F -->|Нет| H[Отказ]
        G --> I[Подписание]
        I --> J[Активация кредита]
    """)

    doc = header
    doc += section("Краткое описание", desc or "Автоматизация сбора требований для кредитования.")
    doc += section("Цель проекта", goal or "Сократить время подготовки BRD до 5 минут.")
    doc += section("Проблема", problem or "Ручной сбор требований медленный и ошибочный.")
    doc += section("Пользователи", users or "BA, PO, Risk, Dev, Support")
    doc += section("Scope (входит)", scope_in)
    doc += section("Scope (не входит)", scope_out)
    doc += section("Ограничения", constraints or "Ограничения по времени и данных.")
    doc += section("KPI", kpi or "Время подготовки <= 5 минут, полнота требований >= 85%.")
    doc += section("Бизнес-правила", rules or "KYC, валидация, логирование.")
    doc += section("Желаемый результат", result or "Готовый BRD, stories, use case, диаграмма.")
    doc += section("User Stories", user_stories)
    doc += section("Use Case", use_case)
    doc += section("Mermaid", mermaid)

    return doc


def save_docx(text: str, path="BRD_DOCUMENT.docx"):
    from docx import Document
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)
    return path
