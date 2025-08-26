# Django Personal Portfolio

A modern, responsive personal portfolio website built with Django and Tailwind CSS. This portfolio showcases projects, skills, experience, education, documents, and provides a contact form for potential clients and employers.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with Tailwind CSS
- **Admin Interface**: Easy content management through Django admin
- **Contact Form**: Functional contact form with email notifications
- **Project Showcase**: Display projects with images, descriptions, and technology tags
- **Skills Management**: Categorized skills with proficiency levels
- **Education Timeline**: Display educational background and certifications
- **Document Viewer**: PDF downloads and image viewing for certificates/resumes
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Production Ready**: Security settings and deployment configuration

## Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- Virtual environment (recommended)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/kb-diplo/PP.git
   cd PP
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load sample data**
   ```bash
   python manage.py load_portfolio_data
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open [http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser

## Project Structure

```
portfolio/
├── config/                 # Django project settings
│   ├── settings.py        # Main settings file
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── portfolio/             # Main portfolio app
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin configuration
│   ├── urls.py           # App URL patterns
│   ├── fixtures/         # Sample data
│   └── management/       # Custom management commands
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   └── portfolio/       # App-specific templates
├── static/              # Static files (CSS, JS, images)
├── media/               # User-uploaded files
└── requirements.txt     # Python dependencies
```

## Models

### Profile
Stores personal information, social links, and contact details.

### Project
Manages portfolio projects with images, descriptions, and technology tags.

### Skill
Tracks technical skills with categories and proficiency levels.

### ContactMessage
Stores messages from the contact form.

## Admin Interface

Access the admin interface at `/admin/` to manage your content:

- **Profile**: Update your personal information and social links
- **Projects**: Add, edit, and organize your portfolio projects
- **Skills**: Manage your technical skills and proficiency levels
- **Contact Messages**: View and manage contact form submissions

## Customization

### Updating Your Information

1. **Profile Data**: Use the admin interface to update your profile information
2. **Projects**: Add your projects through the admin panel
3. **Skills**: Update your skills and proficiency levels
4. **Images**: Upload profile and project images through the admin interface

### Styling

- **Tailwind CSS**: The project uses Tailwind CSS for styling
- **Custom CSS**: Add custom styles in `static/css/styles.css`
- **Templates**: Modify templates in the `templates/` directory

### Environment Variables

Copy `.env.example` to `.env` and update with your settings:

```bash
cp .env.example .env
```

Update the `.env` file with your actual values:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
SERVER_EMAIL=your-email@gmail.com
ADMIN_EMAIL=your-email@gmail.com
```

## Management Commands

### `load_portfolio_data`

This command populates the database with the initial data from the fixture files located in `portfolio/fixtures/`. It's essential for setting up the portfolio for the first time.

**Usage:**

- To load the initial data into an empty database:
  ```bash
  python manage.py load_portfolio_data
  ```

- To clear all existing portfolio data and reload it from the fixtures (useful for a fresh start or after updating the fixture files):
  ```bash
  python manage.py load_portfolio_data --clear
  ```

## Deployment

### Production Settings

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper email configuration
4. Configure static files serving
5. Set up a production database (PostgreSQL recommended)

### Security

The project includes security best practices:
- CSRF protection
- XSS protection
- Secure headers
- SQL injection protection through Django ORM

## Technologies Used

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (development), PostgreSQL (recommended for production)
- **Icons**: Font Awesome
- **Forms**: Django Forms with CSRF protection

## Extending the Portfolio

This portfolio is designed to be easily extensible:

### Adding a Blog
1. Create a `Blog` model
2. Add blog views and templates
3. Update navigation

### Adding a CMS
1. Install django-cms or wagtail
2. Configure CMS settings
3. Create CMS templates

### Adding More Features
- Testimonials section
- Resume/CV download
- Project categories/filtering
- Search functionality
- Social media integration

## Contributing

Feel free to fork this project and customize it for your own portfolio. If you find bugs or have suggestions for improvements, please open an issue.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email**: tingzlarry@gmail.com
- **GitHub**: [@kb-diplo](https://github.com/kb-diplo)
- **LinkedIn**: [Lawrence Mbugua Njuguna](https://linkedin.com/in/lawrence-mbugua)
- **Portfolio**: [Live Demo](https://your-portfolio-url.com)
