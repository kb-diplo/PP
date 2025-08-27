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

## Step 4: Set Up Environment Variables

1. In the "Web" tab, go to the "Environment variables" section
2. Add the following environment variables:
   - `DEBUG=False`
   - `SECRET_KEY=your-secret-key` (use the same as in your local settings)
   - `ALLOWED_HOSTS=mbugualawrence.pythonanywhere.com,www.mbugualawrence.pythonanywhere.com`
   - `EMAIL_HOST_USER=your-email@example.com`
   - `EMAIL_HOST_PASSWORD=your-email-password`
   - `DEFAULT_FROM_EMAIL=your-email@example.com`

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
