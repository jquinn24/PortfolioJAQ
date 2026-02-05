# Portfolio Website

A modern, responsive portfolio website built with Python Flask, HTML, and CSS.

## Features

- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Modern Styling**: Clean and professional design with smooth animations
- **Multiple Pages**: Home, About, Projects, and Contact pages
- **Contact Form**: Functional contact form with validation
- **Skills Section**: Showcase your technical skills
- **Projects Showcase**: Display your work and projects
- **Social Media Links**: Connect your social profiles

## Project Structure

```
Portfolio JAQ/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── app/
    ├── templates/        # HTML templates
    │   ├── base.html    # Base template with navigation
    │   ├── index.html   # Home page
    │   ├── about.html   # About page
    │   ├── projects.html # Projects page
    │   └── contact.html # Contact page
    └── static/          # Static files
        ├── css/
        │   └── style.css # Main stylesheet
        ├── js/
        │   └── script.js # JavaScript functionality
        └── images/      # Image assets (placeholder)
```

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "c:\Users\jonat\Desktop\CODING PROJECTS\Portfolio JAQ"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Activate the virtual environment** (if not already active):
   ```bash
   venv\Scripts\activate
   ```

2. **Run the Flask app**:
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

The website will be live on `http://localhost:5000`

## Customization

### Update Your Information

- **Name & Title**: Edit `app/templates/index.html` to replace "Jonathan" with your name
- **About Section**: Update `app/templates/about.html` with your bio
- **Projects**: Add your projects in `app/templates/projects.html`
- **Contact Info**: Update email, phone, and social links in `app/templates/contact.html`

### Styling

All styles are in `app/static/css/style.css`. The design uses CSS custom properties (variables) for easy customization:

```css
:root {
    --primary-color: #3498db;      /* Main blue */
    --secondary-color: #2c3e50;    /* Dark blue */
    --accent-color: #e74c3c;       /* Red accent */
    /* ... more colors ... */
}
```

### Add Images

Place your images in `app/static/images/` and reference them in templates:
```html
<img src="{{ url_for('static', filename='images/your-image.jpg') }}" alt="Description">
```

## Backend Features

The Flask backend includes:

- **Route Management**: Multiple pages with clean routing
- **Template Rendering**: Jinja2 templating for dynamic content
- **Contact API**: `/api/send-message` endpoint for form submissions (currently returns success)
- **Static File Serving**: Automatic serving of CSS, JS, and images

### Adding Email Functionality

To enable email sending, update `app.py`:

1. Install Flask-Mail:
   ```bash
   pip install Flask-Mail
   ```

2. Configure your email settings in `app.py` and implement the email logic in the `send_message()` function

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Responsive CSS Grid and Flexbox
- **Server**: Flask Development Server

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Deployment

To deploy this website:

1. **Heroku**:
   - Add a `Procfile`: `web: python app.py`
   - Push to Heroku

2. **PythonAnywhere**:
   - Upload files and configure WSGI

3. **Traditional Hosting**:
   - Use Gunicorn: `pip install gunicorn`
   - Run: `gunicorn app:app`

## Future Enhancements

- [ ] Add database integration (SQLAlchemy)
- [ ] Implement email notifications
- [ ] Add blog section
- [ ] Integrate analytics
- [ ] Add dark mode toggle
- [ ] Create admin panel for content management

## License

This project is open source and available under the MIT License.

## Support

For questions or improvements, feel free to modify the code and customize it to your needs!

---

**Happy coding! 🚀**
