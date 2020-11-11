"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cars.views import add_car,add_manufactuer,home,add_multi_cars
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='home'),
    path('admin/', admin.site.urls),
    path('add_car/',add_car,name='add_car'),
    path('add_manufactuer/',add_manufactuer,name='add_manufactuer'),
    path('add_multi_cars/',add_multi_cars,name='add_multi_cars')
    # path('/',)
]
