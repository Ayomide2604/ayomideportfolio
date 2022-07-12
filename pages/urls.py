
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index , name='pages'),
    path('portfolio/<int:pk>', views.project , name='project-detail'),
]
