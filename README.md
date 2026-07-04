# ResumeWebsite

## Django setup

This site now runs as a Django project from the repository root.

## Project layout

- `manage.py` starts the Django project.
- `djangoproject/` contains the project settings and URL routing.
- `index.html`, `experiences.html`, and `portfolio.html` are served as pages.
- `recipes/` contains the recipe pages.
- `scripts/`, `styles/`, `images/`, and `files/` store shared assets.

## Run the site locally

Install dependencies, apply the initial Django setup, and start the development server:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Page URLs

- `/`
- `/index.html`
- `/experiences.html`
- `/portfolio.html`
- `/recipes/pancakecookies.html`
- `/recipes/cakecookies.html`
- `/recipes/peachdumplings.html`

## Updating the AWS EC2 Server

1. SSH into the server using PuTTY
2. Navigate to folder:              cd ~/ResumeWebsite
2. Enter the virtual environment:   source venv/bin/activate 
3. Restart project:                 sudo systemctl restart django
4. Pull from GitHub:                git pull