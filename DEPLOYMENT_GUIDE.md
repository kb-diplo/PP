# PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (https://www.pythonanywhere.com/)
- Git installed on your local machine
- Your Django project code in a Git repository (GitHub, GitLab, etc.)

## Step 1: Upload Your Code to GitHub

1. Initialize a Git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create a new repository on GitHub and push your code:
   ```bash
   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main
   ```

## Step 2: Set Up PythonAnywhere

1. Log in to your PythonAnywhere account
2. Go to the "Web" tab and click "Add a new web app"
3. Choose "Manual Configuration" (not "Flask" or "Django")
4. Select Python 3.10 (or your preferred version)
5. Click "Next"

## Step 3: Configure Your Web App

1. In the "Code" section:
   - Source code: `/home/mbugualawrence/Personal-portfolio`
   - Working directory: `/home/mbugualawrence/Personal-portfolio`

2. In the "Virtualenv" section:
   - Enter the path to your virtualenv: `/home/mbugualawrence/.virtualenvs/portfolio_env`

3. In the "WSGI configuration file" section:
   - Click on the WSGI configuration file link
   - Delete all the content and paste the content from `pythonanywhere_wsgi.py`
   - Save the file

## Step 4: Set Environment Variables

1. **Create a `.env` file** in your project root with the following content (replace with your actual values):

```bash
# Django Settings
# Generate a new secret key: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-username.pythonanywhere.com

# Database
# SQLite (default) - no additional configuration needed
# For MySQL, uncomment and configure:
# DB_NAME=your_db_name
# DB_USER=your_db_user
# DB_PASSWORD=your_db_password
# DB_HOST=your-db-host.mysql.pythonanywhere-services.com

# Email Configuration (Required for contact form)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password  # Generate from Google Account > Security > App passwords
DEFAULT_FROM_EMAIL=your-email@gmail.com
SERVER_EMAIL=your-email@gmail.com
ADMIN_EMAIL=your-email@gmail.com
```

2. **For Gmail SMTP Access**:
   - Go to your Google Account > Security
   - Enable 2-Step Verification if not already enabled
   - Go to App passwords
   - Generate a new app password for your PythonAnywhere app
   - Use this app password as `EMAIL_HOST_PASSWORD`

3. **On PythonAnywhere**:
   - Go to the "Web" tab in your dashboard
   - Click on "Add a new environment variable"
   - Add each environment variable from your `.env` file
   - Make sure to use the actual values, not the placeholders

## Step 5: Set Up the Database

1. In the "Databases" tab, click "Initialize MySQL"
2. Note down your MySQL credentials
3. Update the database settings in `config/settings.py` if needed
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Step 6: Collect Static Files

1. Run the following command in the PythonAnywhere console:
   ```bash
   python manage.py collectstatic --noinput
   ```

## Step 7: Restart Your Web App

1. Go to the "Web" tab
2. Click the green "Reload" button to restart your web app

## Step 8: Access Your Site

Your site should now be live at: https://mbugualawrence.pythonanywhere.com/

## Troubleshooting

1. **500 Error**: Check the error log in the "Web" tab
2. **Static files not loading**: Make sure `DEBUG` is set to `False` and you've run `collectstatic`
3. **Database issues**: Verify your database settings and run migrations

## Updating Your Site

1. Push changes to your Git repository
2. In PythonAnywhere, pull the latest changes:
   ```bash
   cd /home/mbugualawrence/Personal-portfolio
   git pull origin main
   ```
3. Run migrations if needed:
   ```bash
   python manage.py migrate
   ```
4. Collect static files if needed:
   ```bash
   python manage.py collectstatic --noinput
   ```
5. Reload your web app from the "Web" tab
