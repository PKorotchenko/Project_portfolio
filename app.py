from flask import Flask, render_template, request

app = Flask(__name__)


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
    projects_list = [
        {
            'title': 'Portfolio Website',
            'description': 'A responsive portfolio website built with Flask. Features a clean dark theme with minimalistic design and smooth navigation.',
            'github': 'https://github.com/yourusername/portfolio-website'
        },
        {
            'title': 'Weather App',
            'description': 'A weather forecast application that provides real-time weather data. Built with Python and integrated with OpenWeatherMap API.',
            'github': 'https://github.com/yourusername/weather-app'
        },
        {
            'title': 'Task Manager',
            'description': 'A todo application with task management features. Allows users to create, edit, and delete tasks with a clean user interface.',
            'github': 'https://github.com/yourusername/task-manager'
        },
        {
            'title': 'E-commerce Platform',
            'description': 'A full-featured e-commerce platform with product catalog, shopping cart, and payment integration.',
            'github': 'https://github.com/yourusername/ecommerce-platform'
        }
    ]
    return render_template('projects.html', projects=projects_list)


if __name__ == '__main__':
    app.run(debug=True)
