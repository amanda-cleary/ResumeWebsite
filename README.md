# About This Repository

This repository contains two projects: ResumeWebsite and RecipeBook. ResumeWebsite is served at amandacleary.com through an AWS EC2 instance. Similarly, RecipeBook is accessed through amandacleary.com/recipes. 

Originally, this repository only contained ResumeWebsite, which was built using HTML, CSS, and JavaScript. For ease of access, RecipeBook was added to this repository, as it would also use the amandacleary domain for deployment.

However, RecipeBook is a Django project, which ResumeWebsite was not. Including RecipeBook necessitated a migration of the repository to be compatible with Django. 

As these are independent projects, the development process has included many opportunities for learning and improving design, processing power, and deployment. 

## Resources

Font Awesome Icons (CSS): https://fontawesome.com/icons
Color Scheme Generator (CSS): https://colorffy.com/color-scheme-generator?color=%23ffebf1 
Ignacio Figueroa's Resume Website (UI Reference): https://ignaciofigueroa.dev/en 
Sheldon Codling's Resume Website (UI Reference): https://www.sheldonc.ca/
Javier Morales's Resume Website (UI Reference): https://www.javiermorales.dev/ 

Supplementary AI tools included ChatGPT and Copilot. These were primarily used for learning new tools, configuring deployment, and generating starter code.

## Navigation

resumewebsite
- djangoproject
    - 'settings.py'
    - 'urls.py'
- files
    - 'cleary_resume.pdf'
- images
- recipebook -> Django app
    - 'models.py'
    - 'views.py'
- scripts
- styles
- templates
    - recipebook -> html files related to RecipeBook project
        - 'edit_recipe.html'
        - 'login.html'
        - 'recipe_base.html'
        - 'recipe.html'
        - 'recipes.html'
    - 'base.html'
    - 'experiences.html'
    - 'index.html'
    - 'portfolio.html'
- 'manage.py'
- 'README.md'
- 'requirements.txt'
- 'styles.css'

# Updating and Running the Projects

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
- `/admin`
- `/about`
- `/experiences`
- `/portfolio`
- `/recipes`
- `/recipes/login`

## Updating the AWS EC2 Server

1. SSH into the server using PuTTY
2. Navigate to folder:              cd ~/ResumeWebsite
2. Enter the virtual environment:   source venv/bin/activate 
3. Restart project:                 sudo systemctl restart django
4. Pull from GitHub:                git pull