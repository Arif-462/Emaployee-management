from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('emp_list/', views.emp_list, name = "emp_list"),
    path('emp_add/', views.emp_add, name = "emp_add"),
    path('emp_delete/', views.emp_delete, name = "emp_delete"),
    path('emp_delete/<int:id>/', views.emp_delete, name = "emp_delete"),
    path('emp_edit/', views.emp_edit, name = "emp_edit"),
    path('emp_edit/<int:id>/', views.emp_edit, name = "emp_edit"),
    path('emp_filter/', views.emp_filter, name = "emp_filter"),
    # path('searchitem/', views.searchitem, name = "searchitem"),
]
