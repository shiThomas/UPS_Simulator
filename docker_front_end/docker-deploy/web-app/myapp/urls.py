from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('packages/', views.PackageListView.as_view(), name='packages'),
    path('packages/<int:pk>', views.PackageDetailView.as_view(), name='package-detail'),
    path('packages/<int:pk>/update/', views.PackageUpdate.as_view(), name='package_update'),
    path('survey/create/', views.SurveyCreate.as_view(), name='survey_create'),


]

# User
urlpatterns += [

    path('signup/', views.register, name='signup'),
    path('profile', views.profile, name='profile'),
]