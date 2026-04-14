# Portfolio Website

A minimalistic, dark-themed portfolio website built with Flask.

## Features

- **Home Page**: Welcome message and brief description
- **About Me**: Experience, skills, and background information
- **Projects**: Showcase of 4 projects with GitHub links
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Dark Theme**: Eye-friendly dark interface with cyan accent color
- **Navigation**: Header menu with active page highlighting
- **Modern Typography**: Uses Roboto font family

## Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── about.html       # About Me page
│   └── projects.html    # Projects page
└── static/
    └── css/
        └── styles.css   # CSS styles (dark theme)
```

## Installation

### 1. Create a virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Customization

### Update Personal Information

Edit the Flask routes and templates to add your personal information:

1. **Home Page** (`templates/index.html`)
   - Update the welcome message and description

2. **About Page** (`templates/about.html`)
   - Add your experience details
   - Update technical skills
   - Modify experience timeline

3. **Projects Page** (`app.py`)
   - Update the projects list in the `projects()` function
   - Add your GitHub repository links
   - Modify project descriptions

### Styling

All styles are in `static/css/styles.css`:
- Colors can be customized by modifying the CSS variables
- The primary accent color is `#61dafb` (cyan)
- Background color is `#0f0f0f` (dark)

## Pages

### Home (`/`)
- Welcome section with call-to-action button
- Brief introduction

### About Me (`/about`)
- Personal journey narrative
- Technical skills grid (Backend, Frontend, Tools)
- Experience timeline

### Projects (`/projects`)
- 4-column project grid (responsive)
- Each project shows: title, description, GitHub link
- Hover effects for better interactivity

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

This project is open source and available under the MIT License.
