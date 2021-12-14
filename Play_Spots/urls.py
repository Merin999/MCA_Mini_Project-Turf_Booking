"""Pharmacy_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Play_Spots import settings
# from Turf import
from Turf import admin_urls, user_urls, owner_urls
from Turf.views import IndexView, CategoryView, OwnerReg, UserReg, LoginView, AboutView, De, Forgot_Password
urlpatterns = [

    path('', IndexView.as_view()),
    path('AboutView', AboutView.as_view()),
    path('LoginView', LoginView.as_view()),
    path('CategoryView', CategoryView.as_view()),
    path('ownerreg', OwnerReg.as_view()),
    path('userreg', UserReg.as_view()),
    path('admin/', admin_urls.urls()),
    path('user/', user_urls.urls()),
    path('owner/', owner_urls.urls()),
    path('De', De.as_view()),
    path('Forgot_Password', Forgot_Password.as_view()),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
