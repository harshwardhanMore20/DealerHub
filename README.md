# Dealer Review Platform

A Django-based web application for browsing dealers, filtering by state, reading reviews, and posting new reviews after login.

## Features
- Dealer listings on the home page
- Dealer details with reviews
- User registration and login
- Review submission for authenticated users
- About and Contact pages
- API endpoints for dealers, reviews, car makes, and sentiment analysis

## Project Structure
- `DjangoFirst/` - Django project settings and URLs
- `dealers/` - App with models, views, templates, and URLs

## Requirements
- Python 3.10+
- Django 6.0+

## Setup
1. Open PowerShell in the project folder:
   ```powershell
   cd d:\django_project\env\DjangoFirst
   ```
2. Activate the virtual environment:
   ```powershell
   d:\django_project\env\Scripts\Activate.ps1
   ```
3. Install dependencies (if needed):
   ```powershell
   pip install django
   ```
4. Apply migrations and load sample data:
   ```powershell
   python manage.py migrate
   python manage.py seed_data
   ```

## Run the Application
```powershell
python manage.py runserver 127.0.0.1:8000
```
Then open:
```text
http://127.0.0.1:8000/
```

## Admin Panel
Create an admin account:
```powershell
python manage.py createsuperuser
```
Then open:
```text
http://127.0.0.1:8000/admin/
```

## Example API Calls
- Get all dealers:
  ```powershell
  curl http://127.0.0.1:8000/api/dealers/
  ```
- Get dealer reviews:
  ```powershell
  curl http://127.0.0.1:8000/api/dealers/1/reviews/
  ```
- Analyze review sentiment:
  ```powershell
  curl "http://127.0.0.1:8000/api/analyze-review/?text=Fantastic%20services"
  ```
