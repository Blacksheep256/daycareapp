from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [    
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
    path('fees',views.schoolfeeslist, name="fees"),
    path('', auth_views.LoginView.as_view(template_name='daycareapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='daycareapp/logout.html/'), name='logout'),
    path('restricted/', views.restricted_page, name='restricted_page'),
]