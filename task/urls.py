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
import cars.views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',cars.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('add_car/',cars.views.add_car,name='add_car'),
    path('add_manufactuer/',cars.views.add_manufactuer,name='add_manufactuer'),
    path('add_multi_cars/',cars.views.add_multi_cars,name='add_multi_cars'),
    path('all_cars/',cars.views.all_cars,name='all_cars'),
    path('all_manufactuers/',cars.views.all_manufactuers,name='all_manufactuers'),
    path('delete_manufactuer/',cars.views.delete_manufactuer,name='delete_manufactuer'),
    path('delete_car/',cars.views.delete_car,name='delete_car'),
    path('check_manufactuer/',cars.views.check_manufactuer,name='check_manufactuer'),
    path('country_wise_manufactuer/',cars.views.country_wise_manufactuer,name='country_wise_manufactuer'),
]
