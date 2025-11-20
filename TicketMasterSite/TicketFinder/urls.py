from django.urls import path
from . import views
urlpatterns = [
    path('', views.search, name='search'),
    path('savedTickets/', views.SavedTicket, name='savedTickets'),
    path('loadTickets/', views.loadTickets, name='loadTickets'),
    path('deleteTicket/<str:ticket_id>/', views.deleteTicket, name='deleteTicket'),
]