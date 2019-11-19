# CURD-Operations
Create a simple django application use CURD Operations in title, description, creation date and updation date
 
# Django CRUD Example Apps
This is a small Django project to demonstrate Django CRUD functionality, it consist of 1 small applications:
# .CurdApp
# Requirements for project:
 
   Django>=2.2,<2.3 Python 3 install on your computer and set paths and others requriments corrcetly.
# 1.Create Project
   > django-admin startproject CurdPro
# 2.Create App inside project
   > cd CurdPro
   > CurdPro > python manage.py startapp CurdApp
# 3.Register RESTFull API and app in project
   CurdPro> settings.py
    Installed_apps=[
                    'rest_framework',
                    'CurdApp'
                    ]    
                    save it
           
# 4.Create model Notes
from django.db import models

class Notes(models.Model):
    title=models.CharField(max_length=40,null=True,blank=False)
    description=models.TextField(max_length=40,null=True,blank=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField() like this.
    
 # 5.Register model in Admin panel
   from django.contrib import admin
   from .models import Notes
   Register your models here.
   admin.site.register(Notes)
   
# 6.Conver model into database table
> CurdPro > python manage.py makemigrations CurdApp
> CurdPro > python manage.py migrate

# 7.Create superuser for store data into database
> CurdPro > python manage.py createsuperuser

username:
email:
password:
Reenter Password:

# 8.Run server
> CurdPro > python manage.py runserver

# 9.Goto admin panel 
 by typing in web search bar http://localhost:8000/admin/
 then login with user name and password as chaitu/chaitu
 
 enter data in Notes like Title,Description,Creation Date,Updation Date and save it.
 Logout it.
 
 # 10.Convert model into JSON Data
 
   for this purpose we create a new file 'serializers.py' inside CurdPro/CurdApp in the application.
   
   from rest_framework import serializers
   from . import models
   class NotesSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = models.Notes
          fields = ('title', 'description', 'created_at', 'updated_at')

# 11.Implement CURD operations in views.
  
  from rest_framework import viewsets
  from . import models
  from . import serializers
  class NotesView(viewsets.ModelViewSet):
     queryset = models.Notes.objects.all()
     serializer_class = serializers.NotesSerializer

# 12.Connect this view with URL

from rest_framework import routers
from CurdApp import views as myapp_views

router = routers.DefaultRouter()

router.register(r'notes', myapp_views.NotesView)

# 13.Run server

 > CurdPro > python manage.py runserver
  
  
# 14.Get the required OUTPUT

Api Root Notes List

Notes List
GET /api/v1/notes/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "title": "java",
        "description": "java is a programming langvage",
        "created_at": "2019-11-18T17:38:22.283527Z",
        "updated_at": "2019-11-18T17:38:22.283527Z"
    },
    {
        "title": "java",
        "description": "java is a programming langvage",
        "created_at": "2019-11-18T17:38:29.194026Z",
        "updated_at": "2019-11-18T17:38:29.194026Z"
    },
    {
        "title": "java",
        "description": "java is a programming langvage",
        "created_at": "2019-11-18T17:38:35.288200Z",
        "updated_at": "2019-11-18T17:38:35.288200Z"
    },
    {
        "title": "Django",
        "description": "framework",
        "created_at": "2019-11-18T17:40:05.581765Z",
        "updated_at": "2019-11-18T17:40:05.582764Z"
    },
    {
        "title": "spring",
        "description": "framework",
        "created_at": "2019-11-18T17:46:36.503824Z",
        "updated_at": "2019-11-18T17:46:36.503824Z"
    },
    {
        "title": "Python",
        "description": "It is a programming language.",
        "created_at": "2019-11-19T03:28:01Z",
        "updated_at": "2019-11-21T03:28:08Z"
    },
    {
        "title": "anaconda",
        "description": "It is a programming language.",
        "created_at": "2019-11-19T09:00:00Z",
        "updated_at": "2019-11-20T09:00:00Z"
    }
]   as like this.
