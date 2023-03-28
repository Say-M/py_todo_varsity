from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('task', views.TaskPage, name='task'),
    path('deleteTask/<str:pk>', views.DeleteTaskPage, name='deleteTask'),
    path('task/<str:pk>', views.UpdateTaskPage, name="updateTask"),
    path('login', views.LoginPage, name='login'),
    path('logout', views.LogoutPage, name='logout'),
]
