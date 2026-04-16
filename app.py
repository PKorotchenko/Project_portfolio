from flask import Flask, render_template, request, abort

app = Flask(__name__)

projects_data = [
    {
        'id': 'erp-integration',
        'title': 'ERP-интеграция 1С',
        'description': 'Разработка и внедрение ERP-решений на платформе 1С:Предприятие с интеграцией внешних систем и обменом данными.',
        'details': 'Проект включает доработку ERP-конфигурации, анализ функционала казначейства и автоматизацию бизнес-процессов для крупного нефтегазового клиента.',
        'features': [
            'Доработка модуля казначейства',
            'Оптимизация существующих процессов',
            'Сопровождение и тестирование изменений'
        ]
    },
    {
        'id': 'http-services',
        'title': 'HTTP-сервисы и API для 1С',
        'description': 'Создание и сопровождение HTTP-сервисов для интеграции мобильных приложений и внешних систем с 1С.',
        'details': 'В проекте реализовано несколько API для обмена данными о геолокации, состоянии грузов и складских операциях между 1С и мобильным приложением.',
        'features': [
            'Разработка HTTP-сервисов',
            'Интеграция с мобильными приложениями',
            'Обработка больших пакетов данных'
        ]
    },
    {
        'id': 'report-automation',
        'title': 'Автоматизация отчетности',
        'description': 'Разработка сложной отчетности и рефакторинг кода в 1С для повышения эффективности бизнес-процессов.',
        'details': 'Проект направлен на создание удобных отчетов для финансового и операционного контроля, с использованием СКД и сложных запросов.',
        'features': [
            'Создание отчетов на СКД',
            'Рефакторинг существующей отчетности',
            'Улучшение производительности запросов'
        ]
    },
    {
        'id': 'mentoring',
        'title': 'Наставничество и обучение',
        'description': 'Обучение сотрудников, ведение стажёров и консультирование по вопросам разработки на 1С:EDT и работе с Git.',
        'details': 'Оказание поддержки младшим разработчикам, проведение технических консультаций и сопровождение стажёров на проектах ERP.',
        'features': [
            'Наставничество стажёров',
            'Проведение обучающих сессий',
            'Консультирование по Git и 1С:EDT'
        ]
    }
]


def get_project_by_id(project_id):
    return next((project for project in projects_data if project['id'] == project_id), None)


@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About Me page"""
    return render_template('about.html')


@app.route('/projects')
def projects():
    """Projects page"""
    return render_template('projects.html', projects=projects_data)


@app.route('/projects/<project_id>')
def project_info(project_id):
    """Project detail page"""
    project = get_project_by_id(project_id)
    if not project:
        abort(404)
    return render_template('project_info.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)
