from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('homepage/', views.view_schedule, name='homepage'),
    path('schedule-queries/', views.schedule_queries, name='schedule_queries'),
    path('flight-queries/', views.flight_queries, name='flight_queries'),
    path('edit-schedule/<str:pk>/', ScheduleUpdateView.as_view(), name='edit_schedule'),
    path('edit-flight/<str:pk>/', FlightUpdateView.as_view(), name='edit_flight'),
    path('delete-schedule/<str:pk>/', ScheduleDeleteView.as_view(), name='delete_schedule'),  
    path('delete-flight/<str:pk>/', FlightDeleteView.as_view(), name='delete_flight'),
]

app_name = "flight_scheduler"