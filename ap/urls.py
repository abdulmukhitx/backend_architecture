from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home, name='home'),  # Example view
    path('joblist/', views.JobListView.as_view(), name='job_list'),
    
]

