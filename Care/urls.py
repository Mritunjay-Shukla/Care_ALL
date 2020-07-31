from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from Care.views import HomePage, detailpage

urlpatterns = [
    path('', HomePage.as_view()),
    #path("home", homepage),
    path('detail/<int:id>', detailpage)
    
   

]