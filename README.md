## Restart your postgresql server with, 
`brew services restart postgresql`
`service postgresql start`


# Create a database

In your terminal run, 

`psql`

`CREATE DATABASE senddit;`

`\q`

`psql senddit`

#### GIT Add * Commit * Push


# Create a virtual environment

In your terminal, run,

`python3 -m venv .env`

`source .env/bin/activate`

`pip3 install django`

`pip3 install psycopg2-binary`

`pip3 freeze > requirements.txt`

`deactivate`

`touch .gitignore`, and add ".env" to that file

#### GIT Add * Commit * Push


# Create a django app

In your terminal, run, 

`source .env/bin/activate`

`django-admin startproject senddit_project . `

`django-admin startapp main_app`

In senddit_project/settings.py, make these changes,

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'senddit',
    }
}
```
In your terminal, run,

`python3 manage.py migrate`

`python3 manage.py runserver`

#### GIT Add * Commit * Push


# Create Signup view

In main_app/views.py, make these changes,
```
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "signup.html", context)
```
[info about login](https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in)

In your terminal, run, 

`mkdir main_app/templates main_app/templates/registration`

`touch main_app/templates/base.html main_app/templates/signup.html`

In main_app/templates/base.html, make these changes,
```
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Senddit</title>
</head>
<body>

    <a href="{% url 'home' %}">Home</a>
    <h1>Senddit</h1>

    {% block content %}
    {% endblock %}

</body>
</html>
```

In main_app/templates/signup.html, make these changes,
```
{% extends 'base.html' %}
{% block content %}

<h1>Sign up</h1>
{{ form.errors }}
<form method="post" action="{% url 'signup' %}">
    {% csrf_token %}{{form.as_p}}
    <input type="submit" value="Sign up" />
    <input type="hidden" value="{{ next }}" name="next">
</form>

{% endblock %}
```

#### GIT Add * Commit * Push


# Create Signup url

In your terminal, run, 

`touch main_app/urls.py`

In main_app/urls.py, make these changes, 
```
from django.urls import path
from . import views
from .views import Signup

urlpatterns = [
    path('signup/', views.Signup.as_view(), name="signup")
]
```

#### GIT Add * Commit * Push


# Create Home view

In main_app/views.py, make these changes,
```
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            context = {"form": form}
            return render(request, "signup.html", context)
```

#### GIT Add * Commit * Push


# Create a Home template

In your terminal, run, 

`touch main_app/templates/home.html`

In main_app/templates/home.html, make these changes, 
```
{% extends 'base.html' %}
{% block content %}

<h2>Senddit Home</h2>
<h3>Welcome {{user.username}}</h3>

{% endblock %}
```

#### GIT Add * Commit * Push


# Create Home url

In main_app/urls.py, make these changes, 

```
from django.urls import path
from .views import Home, Signup

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('account/signup/', views.Signup.as_view(), name="signup")
]
```

#### GIT Add * Commit * Push


# Get Signup functionality

In senddit_project.urls.py, make these changes, 
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```

In main_app/models.py, make these changes,
```
from django.db import models
from django.contrib.auth.models import User
```

In main_app/templates/home.html, make these changes, 
```
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Senddit</title>
</head>
<body>

    {% if user.is_authenticated %}
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'profile' %}">Profile</a>
        <a href="{% url 'logout' %}">Logout</a>
    {% else %}
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'signup' %}">Signup</a>
        <a href="{% url 'login' %}">Login</a>
    {% endif %}

    {% block content %}
    {% endblock %}

</body>
</html>
```

In senddit_project/templates/home.html, make this change at the bottom,
`LOGOUT_REDIRECT_URL = '/'`

#### GIT Add * Commit * Push


# Get Login functionality

In your terminal, run, 
`touch main_app/templates/registration/login.html`

In main_app/templates/registration/login.html, make these changes, 
```
{% extends 'base.html' %}
{% block content %}

<h1>Login</h1>
<form method="post" action="{% url 'login' %}">
    {% csrf_token %} {{form.as_p}}
    <input type="submit" value="Login" />
    <input type="hidden" value="{{ next }}" name="next" />
</form>

{% endblock %}
```

#### GIT Add * Commit * Push


# Create Profile url, view, template

In main_app/urls.py, make these changes, 
```
from django.urls import path
from .views import Home, Signup, Profile

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('accounts/signup/', Signup.as_view(), name="signup"),
    path('accounts/profile/', Profile.as_view(), name="profile")
]
```

In main_app/views.py, make these changes, 
```
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.http import HttpResponse

class Home(TemplateView):
    template_name = "home.html"

class Profile(View):
    def get(self, request):
        return render(request, "profile.html")

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            context = {"form": form}
            return render(request, "signup.html", context)
```

In your terminal, run,
`touch main_app/templates/profile.html`

In main_app/templates/profile.html, make these changes, 
```
{% extends 'base.html' %}
{% block content %}

{% if user.is_authenticated %}
    <p>Your profile information</p>
{% else %}
    <p>You don't have a profile</p>
{% endif %}

{% endblock %}
```

#### GIT Add * Commit * Push