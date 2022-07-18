# Django personal portfolio website

This is a Python Django-based personal portfolio website.

The website uses [Wagtail CMS](https://github.com/wagtail/wagtail). Wagtail is a Django Content Management System.

All content: personal information, portfolio projects, social media links, Google Analytics tracking code, etc. can be
adjusted in Wagtail admin.

The fronted theme is an inspiration from [Start Bootstrap Freelancer theme](https://startbootstrap.com/theme/freelancer)
.

This repo can be used as a starting point for developing a production-ready Django personal website with deployment to
Heroku. I am releasing the full source code for the site so that others may benefit from it.

## Live website

To view the website demo, please visit [vladislavalerievich.herokuapp.com](https://vladislavalerievich.herokuapp.com/).

> **_NOTE:_**  The web application may take a few seconds to start up.

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

## Production deployment

Heroku uses `Dockerfile` to build and run the application.

To deploy your application on Heroku, you need to do several things:

1) [Create Heroku Account](https://signup.heroku.com/dc)
2) [Download/Install/Setup Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3) After installation, log into Heroku CLI: `heroku login`.
4) Run: `heroku create <your app name>` to create the Heroku application.
5) Run: `heroku stack:set container` so Heroku knows this is a containerized application.
6) Run: `heroku addons:create heroku-postgresql:hobby-dev`, creating the Postgres add-on for Heroku.
7) Set the URL (e.g. `https://<app name>.herokuapp.com)` of your application into environment variable`HOST_NAME` in
   Heroku config settings.
8) To receive emails from the contact form you need an email account. If you choose Google, you need to
   configure [Sign in with App Passwords]( https://support.google.com/accounts/answer/185833?hl=en) for this account.
   Then provide your email and password into environment variables `EMAIL_HOST_USER`
   and `EMAIL_HOST_PASSWORD` in Heroku config vars settings.
9) To store media files you need to configure storage. I have chosen [Cloudinary](https://cloudinary.com/).
   Run: `heroku addons:add cloudinary` and proceed with finishing account setup. Then provide data from dashboard into
   environment variables `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY` and `CLOUDINARY_API_SECRET` in Heroku config
   settings.
10) Deploy your app by running: `git push heroku master`.
11) Create a superuser by running: `heroku run python manage.py createsuperuser`.
12) Go to `<your app name>.herokuapp.com` to see the published web application.


