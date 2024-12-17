"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from vege.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('reciepes/',reciepe,name='reciepes'),
    path('delete_reciepe/<id>/',delete_reciepe,name='delete'),
    path('update_reciepe/<id>/',update_reciepe,name='update'),
    path('login_page/',login_page,name='login'),
    path('register_page/',register,name='register'),
    path('logout_page/',logout_page,name='logout'),
    path('student_page/',student_page,name='student'),
    path('details/<student_id>/',details,name='details'),
    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()
