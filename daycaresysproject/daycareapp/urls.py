"""
URL configuration for daycaresysproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home),
    path('list-babies', views.list_babies, name="list-babies"),
    path('list-babysitter',views.list_babysitter, name="list-babysitter"),
    path('child-profile/<int:pk>/',views.child_profile,name="child-profile"),
    path('child-reg',views.child_reg, name="child-reg"),
    path('babysitter-reg',views.babysitter_reg, name="babysitter-reg"),
    path('babysitter-profile/<str:pk>/',views.babysitter_profile,name="babysitter-profile"),
    path('admin-panel',views.admin_panel,name="admin-panel"),
    path('babysitter-update/<babysitter_id>/',views.babysitter_update, name="babysitter-update"),
    path('baby-delete/<baby_id>/',views.baby_delete, name="baby-delete"),
    path('babysitter-delete/<babysitter_id>/',views.babysitter_delete, name="babysitter-delete"),
    path('baby-update/<baby_id>/',views.baby_update, name="baby-update"),
    path('procure',views.pro, name="procure"),
    path('procrueform',views.procure_form, name="procrueform"),
    path('dollsdashboard',views.dollsdashboard, name="dollsdashboard"),
    path('schoolfees',views.schoolfees, name="schoolfees"),
    path('dollsales',views.dollssales_reg, name="dollsales"),
    


   

]
 