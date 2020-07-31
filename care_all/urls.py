"""care_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Care.views import HomePage
from useraccount.views import sendrequest
from Care.views import detailpage
from useraccount.views import deletereuest, Userdetailpage, acceptreuest
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView,PasswordChangeView, PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('account/', include('useraccount.urls')),
    path('care/', include('Care.urls')),
    path('', HomePage.as_view()),
    path("care/detail/account/friend/<int:id>", sendrequest),
    path('account/userdetail/care/detail/<int:id>', detailpage),
    path('account/userdetail/care/delete/<int:id>', deletereuest),
    path('account/userdetail/care/delete/userdetail/<int:id>', Userdetailpage),
    path('account/userdetail/account/accept/<int:id>', acceptreuest),
    path('account/userdetail/account/accept/userdetail/<int:id>', Userdetailpage),
    path('account/addreview/detail/<int:id>', detailpage),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
