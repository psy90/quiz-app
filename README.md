## Environment Setup

### Pre-requisites

    1. python 3.7 & pip3
    2. virtualenvwrapper or Pyenv

Official documentation referred for Django and DRF links are as follow,

    https://docs.djangoproject.com/en/3.0/

    https://www.django-rest-framework.org/

The SMTP related values you need to modify in `settings.py` to send mails i.e for signup etc.

Install requirements from the `requirements.txt` using `pip install -r requirements.txt`

Run migrations using `python manage.py migrate`

Create superuser using `python manage.py createsuperuser` by providing details.

Start server from project directory using command `python manage.py runserver`

You can access the admin dashboard on `http://localhost:8000/admin/` and account related urls on `http://localhost:8000/accounts/`

Cheers, thank you!
