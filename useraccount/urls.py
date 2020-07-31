from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from useraccount.views import Signup, Profileupdate, Userdetailpage, sendrequest, acceptreuest, addreview
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView,PasswordChangeView, PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

urlpatterns = [

   path("register", Signup.as_view()),
   path("profile/<int:pk>", Profileupdate.as_view()), 
   path("userdetail/profile/<int:pk>", Profileupdate.as_view()),
   path('userdetail/<int:id>', Userdetailpage, name="userdetail"),
   path("login",LoginView.as_view()),
   path("logout/", LogoutView.as_view()),
   path("friend/<int:id>", sendrequest),
   path("accept/<int:id>", acceptreuest),
   path("addreview/<int:id>", addreview, name='addreview'),
]