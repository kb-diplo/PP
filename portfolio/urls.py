from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('documents/', views.DocumentListView.as_view(), name='documents'),
    path('documents/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
]
