from django.urls import path,include
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login
from .views import *



urlpatterns = [
    path('', index, name= 'index'),
    path("accounts/", include('django.contrib.auth.urls')),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    path('profiles/', profiles, name= 'profiles'),
    path('details/', details, name= 'details'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),


    path('clear_history/',clear_history,name='clear_history'),
    path('reset/',reset,name='reset'),

    path('export/excel/', export_to_excel, name='export_to_excel'),


]
