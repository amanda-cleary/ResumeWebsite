# ResumeWebsite

## Django setup

This site now runs as a Django project from the repository root.

## Project layout

- `manage.py` starts the Django project.
- `djangoproject/` contains the project settings and URL routing.
- `index.html`, `experiences.html`, and `portfolio.html` are served as pages.
- `recipes/` contains the recipe pages.
- `scripts/`, `styles/`, `images/`, and `files/` store shared assets.

## Run the site

Install dependencies, apply the initial Django setup, and start the development server:

```bash
python -m pip install -r requirements.txt
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