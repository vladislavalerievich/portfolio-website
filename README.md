# Django personal portfolio website

This is a Python Django based personal portfolio website.

The website uses [Wagtail CMS](https://wagtail.org/). Wagtail is a Django Content Management System.

All content: personal information, portfolio projects, social media links, Google Analytics tracking code, etc. can be
adjusted in Wagtail admin.

Fronted theme is an inspiration from [Start Bootstrap Freelancer theme](https://startbootstrap.com/theme/freelancer).

This repo can be used as a starting point for developing a production-ready Django personal website with deployment to
Heroku. I am releasing the full source code for the site so that others may benefit from it.

## Live website

To view the website demo, please visit [vladislavalerievich.herokuapp.com](https://vladislavalerievich.herokuapp.com/).

## Local development

Setup local environment for the development process.

Go to `./portfolio` directory and activate virtual environment.

#### Run in a terminal

```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Go to `http://127.0.0.1:8000/admin/` in your browser to the Wagtail CMS admin to populate it with your data and to
configure homepage.

#### Run Dockerfile locally

If you want to build and run the production Dockerfile locally, use these commands:

```shell
docker build -t portfolio:latest .  
docker run -it portfolio:latest
```

## Production deployment

1) [Create Heroku Account](https://signup.heroku.com/dc)
2) [Download/Install/Setup Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3) After install, log into Heroku CLI: `heroku login`.
4) Run: `heroku create <your app name>` to create the Heroku application.
5) Run: `heroku stack:set container` so Heroku knows this is a containerized application.
6) Run: `heroku addons:create heroku-postgresql:hobby-dev` which creates the postgres add-on for Heroku.
7) To be able to receive emails from contact form you need an email account. If you choose Google, you need to
   configure [Sign in with App Passwords]( https://support.google.com/accounts/answer/185833?hl=en) for this account.
8) Then provide your email and password from email account into environment variables `EMAIL_HOST_USER`
   and `EMAIL_HOST_PASSWORD`. in Heroku config vars settings.
9) Deploy your app by running: `git push heroku master`.
10) Create superuser by running: `heroku run python manage.py createsuperuser`.
11) Go to `<your app name>.herokuapp.com` to see the published web application.

Heroku uses `Dockerfile` to build and run the application.

