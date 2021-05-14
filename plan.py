# The way we learned it in class, we went 'urls, views, templates' > 'data models' > 'auth', but I think I'd like to go the opposite direction by starting with auth. So things might feel a bit mixed up but this feels more natural to me. I'd like to see if I can get this opinionated framework to flex. 

# ROADMAP:
# - set up database and tables 
# - create django application
# - set up super user and django admin page
# - create a user model
# - create a url&view for a register page
# - try to register a new user!

#=====================================================================#

### How to restart postgres:
## `brew servies restart postgresql` for macs
## `service postgresql start` for windows

### NOTE: Python docstrings can only be created in functions, so ignore the 'def function-name():' please! 

#=====================================================================#

### Steps to set up a Django server.

## Create a database for your server from your terminal
def create_db():
    # in your terminal, enter:
    """ psql """
    # the prompt in your terminal should change to include a hash (#), which indicates you're in the psql shell
    """ CREATE DATABASE senddit; """
    # expected output: "CREATE DATABASE"
    """ \l """
    # L for list, lists all the databases, make sure 'senddit' is there
    """ \q """
    # Q for quit, leave psql so we can reenter connected to the db
    """ psql senddit """
    # your terminal promt should look like this: 'senddit=#'
    """ CREATE TABLE users(id SERIAL PRIMARY KEY, username varchar(100), email varchar(250), password varchar(100))"""
    # expected output: "CREATE TABLE"
    """ SELECT * FROM users; """
    # expected output, because we have no users:  
        # id | username | email | password
        # ----+----------+-------+----------
        # (0 rows)
    """ \q """
    # takes you back to your terminal 
    """ git add -A """
    """ git commit -m 'complete database creation' """
    """ git push origin master """

## Create a virtual environment and install dependencies
def make_env():
    # you can doublecheck you have python installed on your machine with: 
    """ which python3 """
    # expected outcome: /usr/bin/python3
    """ python3 -m venv .env """
    """ ls -a """ # [WSL] dir -a 
    # expected output: " .  ..  .env  .git "
    # start your environment :
    """ source .env/bin/activate """
    # expected output: your terminal prompt should change to show '(.env)' somewhere
    """ pip3 install django """
    # expected output: a message that mentions "successfully installed"
    """ pip3 install psycopg2-binary """
    # expected output: a message that mentions "successfully installed"
    """ pip3 freeze > requirements.txt """
    # this will save your dependencies to the txt file, which we can check by running:
    """ pip3 freeze """
    # expected output: 
        # asgiref==3.3.4
        # Django==3.2.3
        # psycopg2-binary==2.8.6
        # pytz==2021.1
        # sqlparse==0.4.1
    
# NOTE: you can install dependencies from cloned projects with:
    """ pip3 install -r requirements.txt """ 
    # ^^^ ONLY RUN IF YOU'RE CLONING ^^^

    """ deactivate """
    # leaves the virtual environment
    """ touch .gitignore """
    """ open .gitignore """ # [WSL] sorry idk just use 'code .' 
    # hide the .env file from github by typing this in the gitignore file: 
    """ .env """ 
    
    """ git add -A """
    """ git commit -m 'complete env creation' """
    """ git push origin master """    

## Create a Django application and run the server and connect db
def create_django_app():
    # enter your environment
    """ source .env/bin/activate """
    # expected output: your terminal prompt should change to show '(.env)' somewhere
    """ django-admin startproject senddit_project . """ #DON'T FORGET THE "DOT"
    """ ls -a """ # [WSL] dir -a
    # expected output: .  ..  .env  .git  .gitignore  .vscode  manage.py  requirements.txt  senddit_project
    # next create the main app
    """ django-admin startapp main_app """
    # check it was actually created 
    """ ls -a """ # [WSL] dir -a
    # expected output: .  ..  .env  .git  .gitignore  .vscode  PLAN.py  main_app  manage.py  requirements.txt  senddit_project

    # in senddit_project/settings.py
    ## install the new app by adding it to the list of INSTALLED_APPS
    """ 'main_app', """
    # result: 
        # INSTALLED_APPS = [
        #     'django.contrib.admin',
        #     'django.contrib.auth',
        #     'django.contrib.contenttypes',
        #     'django.contrib.sessions',
        #     'django.contrib.messages',
        #     'django.contrib.staticfiles',
        #     'main_app',
        # ]
    # in senddit_project/settings.py
    ## add the database by changing the engine and name in DATABASES
    """ 'django.db.backends.postgresql' """
    """ 'senddit' """
    # result: 
        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.postgresql',
        #         'NAME': 'senddit',
        #     }
        # }
    
    # migrate our changes
    """ python3 manage.py migrate """
    # expected output:" Applying lots_of_different_things_we_need... OK "

    # run the server!
    """ python manage.py runserver """
    # expected output:
        # Django version 3.2.3, using settings 'senddit_project.settings'
        # Starting development server at http://127.0.0.1:8000/
        # Quit the server with CONTROL-C.
    # check it's working by visiting 'localhost:8000'

    # NOTE: is there a way to write a script that will automatically open the browser like the node command we wrote `npm run dev`? ask Dalton

    # quit the server, leave environment, and add-commit-push
    """ CONTROL-C """
    """ deactivate """
    """ git add -A """
    """ git commit -m 'complete django app creation, successfully run server' """
    """ git push origin master """    


## Create a superuser and log into the admin panel
def create_super_user():
    # enter environment
    """ source .env/bin/activate """
    # create superuser
    """ python3 manage.py createsuperuser """
    # fill out the prompts in the terminal, 
        # Username (leave blank to use 'eweb'): """ admin """"
        # Email address: [LEAVE BLANK, HIT ENTER]
        # Password: """" admin """"
        # Password (again): """ admin """"
        # The password is too similar to the username.
        # This password is too short. It must contain at least 8 characters.
        # This password is too common.
        # Bypass password validation and create user anyway? [y/N]: """ y """"
    # expected output: Superuser created successfully.
    # start the server
    """ python3 manage.py runserver """
    # visit 'localhost:8000/admin' and login with your credentials

    # lets create a user! Click 'Users' and fill out the form
    # stop server to check database
    """ CONTROL-C """
    """ psql senddit """
    """ SELECT * FROM users; """
    # expected output: 
        #  id | username | email | password
        # ----+----------+-------+----------
        #  1    gonzo             (hopefully a hashed password?)
        # (0 rows)
    # ACTUAL OUTPUT: 
        #  id | username | email | password
        # ----+----------+-------+----------
        # (0 rows)
    # ??????????
    """ \dt """
    # output:
        #                   List of relations
        #  Schema |            Name            | Type  | Owner
        # --------+----------------------------+-------+-------
        #  public | auth_group                 | table | eweb
        #  public | auth_group_permissions     | table | eweb
        #  public | auth_permission            | table | eweb
        #  public | auth_user                  | table | eweb
        #  public | auth_user_groups           | table | eweb
        #  public | auth_user_user_permissions | table | eweb
        #  public | django_admin_log           | table | eweb
        #  public | django_content_type        | table | eweb
        #  public | django_migrations          | table | eweb
        #  public | django_session             | table | eweb
        #  public | users                      | table | eweb
        # (11 rows)
    # so maybe I need to use auth_user instead of users?
    """ SELECT * FROM auth_user; """
    # output is biiiig but I can see the usernames and the passwords are hashed, so yay ?
        # id |                                         password                                         |          last_login           | is_superuser | username | first_name | last_name | email | is_staff | is_active |          date_joined
        # ----+------------------------------------------------------------------------------------------+-------------------------------+--------------+----------+------------+-----------+-------+----------+-----------+-------------------------------
        # 1 | pbkdf2_sha256$260000$zr2wrdGPvqQke05fg7uvvQ$S+Udei/bptNEEF0XH8weos1Mp9/aMALpJ7EM36XyCwA= | 2021-05-13 13:08:43.598934-06 | t            | admin    |            |           |       | t        | t         | 2021-05-13 13:04:33.771419-06
        # 2 | pbkdf2_sha256$260000$bPTmbuorxBAivMsMKmNcOi$K2PWSILJRyauvFsXIHBC+LjRSo+Evn+62Rq9ryfi8zk= |                               | f            | gonzo    |            |           |       | f        | t         | 2021-05-13 13:11:01.894157-06
        # (2 rows)
    # so I think we didn't need to create the table 'users' from earlier!
    # let's rename it to user_profiles!
    """ ALTER TABLE users RENAME TO user_profiles; """
    # expected output: ALTER TABLE
    # let's check it worked by starting the server and going to the admin site
    """ \q """
    """ python3 manage.py runserver """ # 'localhost:8000/admin'
    # I'm still seeing "Groups" and "Users", so I think I need to make a migration
    """ CONTROL-C """
    """ python3 manage.py migrate """
    # output: 
        # Operations to perform:
        # Apply all migrations: admin, auth, contenttypes, sessions
        # Running migrations:
        # No migrations to apply.
    """ python3 manage.py runserver """ # 'localhost:8000/admin'
    # still not working, must've needed to use 'make migrations'
    """ CONTROL-C """
    """ python3 manage.py makemigrations """
    # output: No changes detected

# wait ... I created the user gonzo in the admin panel, and that sent it to the auth_user table in my database. The user table didn't hold any data, so it should be okay to rename it right? 
    """ CONTROL-C """
    """ python3 manage.py migrate """
        # Operations to perform:
        # Apply all migrations: admin, auth, contenttypes, sessions
        # Running migrations:
        # No migrations to apply.
    """ python3 manage.py makemigrations """
        # No changes detected
# so are the tables connected to the admin panel? idk really know, but I think I am falling down a rabbit hole and I can come back to this - it doesn't need to completely stop me
# NOTE: what is happening with the tables and migrations and what shows up in the admin panel?

    """ CONTROL-C """
    """ git add -A """
    """ git commit -m 'create superuser and user from admin panel' """
    """ git push origin master """   


# next steps: I wanna figure out this user creation thing. 
# So I need to: 
# - create user model
# - create user_profile model
# - migrate models
# - create template, view, url for profile

## Create a url, View, template for register and login

# Create a view for the signup page, should have a form to take their registration information
def sign_up():
    # in main_app/views.py
    """ 
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = ("form": form)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("profile")
            else:
                return redirect("signup")
    """

    # create templates to display some html. need a base.html to extend from, and a signup.html
    # in terminal, either open a new terminal tab or after stopping your server
    """ mkdir main_app/templates """
    """ touch main_app/templates/base.html main_app/templates/signup.html """
    
    # in main_app/templates/base.html
    """  
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

        <h1>Senddit, your home for Shouts and Forums</h1>

        {% block content %}
        {% endblock %}

    </body>
    </html>
    """

    # in main_app/templates/signup.html
    """
    {% extends 'base.html' %}
    {% block content %}

    <h1>Sign up</h1>
    <form method="POST" action="{% url 'signup' %}">
        {% csrf_token %}{{form.as_p}}
        <input type="submit" value="Sign up" />
        <input type="hidden" value="{{ next }}" name="next">
    </form>

    {% endblock %}
    """
    # build a nav bar in base.html to include if user.is_authenticated decorators? 
    # no - stay focused

    # in main_app/views.py
    """
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
                return redirect("profile")
            else:
                return redirect("signup")
    """

    # ahhh I see why my servers breaking, I've been putting things in senddit_project/urls.py that should've been in main_app
    # and now I'm so tired I need to sleep on it

    """ CONTROL-C """
    """ git add -A """
    """ git commit -m 'create views and templates. server down, urls in senddit_project need to go into main_app' """
    """ git push origin master """   

# Next steps: 
# move urls from the project urls.py to the main_app/urls.py
# look into 'include' documentation, do I have to follow Dalton's routing example with 'accounts/signup'?
# idea: for the 'tweets'/shouts, I don't want anyone to be able to interact with it, other users can see your shouts, but they can't do anything but READ
# 

### NEXT DAY
# start the environment 
# start the server

def fix_urls():
    # we need a urls file
    """ touch main_app/urls.py """
    # in senddit_project/urls.py
    """
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main_app.urls')),
    ]
    """
    # in main_app/urls.py
    """
    from django.urls import path
    from . import views
    from .views import Signup

    urlpatterns = [
        path('signup/', views.Signup.as_view(), name="signup")
    ]
    """
    # stop the server, and save our fix
    """ git add -A """
    """ git commit -m 'create views and templates. server down, urls in senddit_project need to go into main_app' """
    """ git push origin master """ 

# render a home page, with a link to signup page
def home_page():
    # in main_app/urls.py
    """
    from django.urls import path
    from . import views
    from .views import Home, Signup

    urlpatterns = [
        path('', views.Home.as_view(), name="home"),
        path('signup/', views.Signup.as_view(), name="signup")
    ]
    """
    # this will break the server, that's okay!
    # in main_app/views.py
    """
    from django.shortcuts import render, redirect
    from django.views import View
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
                return redirect("profile")
            else:
                return redirect("signup")
    """
    # next step make a home.html page
    """ touch main_app/templates/home.html """
    # in main_app/templates/home.html
    """
    {% extends 'base.html' %}
    {% block content %}

    <a href="{% url 'signup' %}">Signup</a>

    {% endblock %}
    """
    # now we have  ahomepage that links to the signup page!
    # stop the server, and save 
    """ git add -A """
    """ git commit -m 'create home.html that links to signup page' """
    """ git push origin master """ 

# now there's a signup page, but it doesn't seem to be working since it's never directing away from the signup page, and in our view that's where it goes if the form isn't valid
def fix_signup():
    # added in an httpresponse to main_app/views to test
    """
    from django.shortcuts import render, redirect
    from django.views import View
    from django.contrib.auth.forms import UserCreationForm
    from django.views.generic.base import TemplateView
    from django.http import HttpResponse

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
                return HttpResponse("<p> it worked </p>")
            else:
                return HttpResponse("<p>nope</p>")
    """
    # signup returns nope, so form is invalid
    # go back to senddit_project/urls.py and add in another route for the contrib auth
    # in senddit_project/urls.py
    """
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main_app.urls')),
        path('user/', include('django.contrib.auth.urls'))
    ]
    """
    # in main_app/urls.py
    """
    from django.urls import path
    from .views import Home, Signup

    urlpatterns = [
        path('', Home.as_view(), name="home"),
        path('user/signup/', Signup.as_view(), name="signup")
    ]
    """

    # idk what's going on so I'm going to try importing to models

    # in main_app/models.py
    """
    from django.db import models
    from django.contrib.auth.models import User
    """
    # in main_app/views.py
    """
    from django.shortcuts import render, redirect
    from django.views import View
    from django.contrib.auth import login
    from django.contrib.auth.forms import UserCreationForm
    from django.views.generic.base import TemplateView
    from django.http import HttpResponse

    class Home(TemplateView):
        template_name = "home.html"

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "signup.html", context)
        def post(self, request):
            form = UserCreationForm(request.POST)
            print(form.data)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                # print(form.data)
                return redirect('signup')
    """

    # so after this I tried to signup and got a redirection to home -- so this worked?? how?? why? tbh idc moving on to proving it's working

    # in main_app/templates/home.html
    """
    {% extends 'base.html' %}
    {% block content %}

    {% if user.is_authenticated %}
        <p>Welcom {{user.username}}</p>
    {% else %}
        <a href="{% url 'signup' %}">Signup</a>
    {% endif %}

    {% endblock %}
    """
    # after refreshing the homepage I see 'Welcome april' 
        # now I need a log out 
        # to do: setting.py needs a logout redirect url, need a url link in the home.html, (also need login link in home.html and a login.html file)

    # in senddit_project/settings.py, at the very bottom
    """
    LOGOUT_REDIRECT_URL = '/'
    """
    # in main_app/templates/home.html
    """
    {% extends 'base.html' %}
    {% block content %}

    {% if user.is_authenticated %}
        <p>Welcome {{user.username}}</p>
        <a href="{% url 'logout' %}">Logout</a>
    {% else %}
        <a href="{% url 'signup' %}">Signup</a>
        <a href="{% url 'login' %}">Login</a>
    {% endif %}

    {% endblock %}
    """
    # tried signing up a new user and it failed
    # idk why
    # can I log in with my created user?
    # in terminal
    """ touch main_app/templates/login.html """
    # in main_app/templates/login.html
    """
    {% extends 'base.html' %}
    {% block content %}

    <h1>Login</h1>
    <form method="post" action="{% url 'login' %}">
        {% csrf_token %} {{form.as_p}}
        <input type="submit" value="Login" />
        <input type="hidden" value="{{ next }}" name="next" />
    </form>

    {% endblock %}
    """
    ####### okay there was nonsense and I was very lost for a while #######
    # in main_app/views.py
    """
    from django.shortcuts import render, redirect
    from django.views import View
    from django.contrib.auth import login
    from django.contrib.auth.forms import UserCreationForm
    from django.views.generic.base import TemplateView
    from django.http import HttpResponse

    class Home(TemplateView):
        template_name = "home.html"

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "signup.html", context)
        def post(self, request):
            form = UserCreationForm(request.POST)
            print(form.data, 'start ***')
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                print(form.errors, 'failed<<<<<<')
                return HttpResponse(form.errors, 'errors =======')
                # return redirect('signup')
    """
    # stop the server, and FOR THE LOVE OF EVERYTHING PUSH UP 
    """ git add -A """
    """ git commit -m 'views.py printing form errors when the signup form is invalid' """
    """ git push origin master """ 
    # let's get the errors to render on the page with the form
    # in main_app/views.py
    """
    from django.shortcuts import render, redirect
    from django.views import View
    from django.contrib.auth import login
    from django.contrib.auth.forms import UserCreationForm
    from django.views.generic.base import TemplateView
    from django.http import HttpResponse

    class Home(TemplateView):
        template_name = "home.html"

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "signup.html", context)
        def post(self, request):
            form = UserCreationForm(request.POST)
            print(form.data, 'start ***')
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                print(form.errors, 'failed<<<<<<')
                context = {"form": form}
                return render(request, "signup.html", context)
    """
    # DEAR GOD SAVE IT
    """ git add -A """
    """ git commit -m 'render form errors on signup page when form submission is invalid' """
    """ git push origin master """ 

    # now that we can signup a new user, let's give them the ability to log in
    # in main_app/templates/home.html
    """
    {% extends 'base.html' %}
    {% block content %}

    {% if user.is_authenticated %}
        <p>Welcome {{user.username}}</p>
        <a href="{% url 'logout' %}">Logout</a>
    {% else %}
        <a href="{% url 'signup' %}">Signup</a>
        <a href="{% url 'login' %}">Login</a>

    {% endif %}

    {% endblock %}
    """
    # following the link to 'user/login' give an error: "TemplateDoesNotExist at /user/login/
    # registration/login.html"
    # so that makes me think that django needs to have a registration directory inside the templates directory, because that's where it'll automatically look for login
    # let's try it out
    """ mkdir main_app/templates/registration """
    """ mv main_app/templates/login.html main_app/templates/registration/login.html """
    # start the server
    """ python3 manage.py runserver """
    # sign up a new user: "apriltest" "secretpassword1"
    # try to log in - login success!
    # but it autoredirects to 'accounts/profile' and there's no profile page so we get a page not found error
    # in urls.py let's change 'user/signup' to 'accounts/signup' and see if we can still sign up and log in as a user
        # emily2 "testpassword"
    # still getting 404

    # in main_app/urls.py
    """
    from django.urls import path
    from .views import Home, Signup, Profile

    urlpatterns = [
        path('', Home.as_view(), name="home"),
        path('accounts/signup/', Signup.as_view(), name="signup"),
        path('accounts/profile', Profile.as_view(), name="profile")
    ]
    """
    # in main_app/views.py
    """
    from django.shortcuts import render, redirect
    from django.views import View
    from django.contrib.auth import login
    from django.contrib.auth.forms import UserCreationForm
    from django.views.generic.base import TemplateView
    from django.http import HttpResponse

    class Home(TemplateView):
        template_name = "home.html"

    class Profile(View):
        template_name = "profile.html"

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "signup.html", context)
        def post(self, request):
            form = UserCreationForm(request.POST)
            print(form.data, 'start ***')
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                print(form.errors, 'failed<<<<<<')
                context = {"form": form}
                return render(request, "signup.html", context)
    """
    # in terminal
    """ touch main_app/templates/profile.html """
    # in main_app/templates/profile.html
    """
    {% extends 'base.html' %}
    {% block content %}

    {{user.username}}

    {% endblock %}
    """
    # tried restarting the server and refreshing and logging in, still 404
    # now getting 405 errors ....

    # let's make sure the project is configured for the right urls
    # in senddit_project/urls.py
    """
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main_app.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
    ]
    """
    # restart server

    ##### lots of debugging and research #####

    # in main_app/views.py
    """
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
            # return HttpResponse("<p>profile</p>")
            return render(request, "profile.html")

    class Signup(View):
        def get(self, request):
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "signup.html", context)
        def post(self, request):
            form = UserCreationForm(request.POST)
            print(form.data, 'start ***')
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                print(form.errors, 'failed<<<<<<')
                context = {"form": form}
                return render(request, "signup.html", context)
    """

    """ git add -A """
    """ git commit -m 'clean up html and make links. can render home and profile page, signup login logout are working' """
    """ git push origin master """ 