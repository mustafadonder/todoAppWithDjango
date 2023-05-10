"""
URL configuration for myFirstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myTODOapp import views #modül olarak import ettik
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),    #ana dizine gittiğimizde hiç bir url vermiyoruz '' şeklinde bırakıyoruz ve views içindeki index fonksiyonunu çalıştırıyor
    path('Gorevler', views.gorevler), #views içerisindeiki gorevler fonksiyonunun urlsini verdik
    path('update/<int:id>', views.update), #views içerisindeiki update fonksiyonunun urlsini verdik, görev id'leri sürekli değişebileceği için dinamik id yapıyoruz
    path('delete/<int:id>', views.delete), #views içerisindeiki delete fonksiyonunun urlsini verdik, görev id'leri sürekli değişebileceği için dinamik id yapıyoruz
]
