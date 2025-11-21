from django.urls import path
from . import views
urlpatterns = [
    path('', views.launchHomePage, name='home'),
    path('searchPage/', views.searchPage, name='searchPage'),
    path('search/', views.search, name='search'),
    path('savedTickets/', views.SavedTicket, name='savedTickets'),
    path('loadTickets/', views.loadTickets, name='loadTickets'),
    path('deleteTicket/<str:ticket_id>/', views.deleteTicket, name='deleteTicket'),
]