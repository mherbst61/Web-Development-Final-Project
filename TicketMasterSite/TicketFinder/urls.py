from django.urls import path
from . import views
urlpatterns = [
    path('', views.launchHomePage, name='home'),
    path('searchPage/', views.searchPage, name='searchPage'),
    path('search/', views.search, name='search'),
    path('savedTickets/', views.SavedTicket, name='savedTickets'),
    path('loadTickets/', views.loadTickets, name='loadTickets'),
    path('deleteTicket/<str:ticket_id>/', views.deleteTicket, name='deleteTicket'),
    path('deleteAllNotes/<str:ticket_id>/', views.deleteAllNotes, name='deleteAllNotes'),
    path('createNewNote/<str:ticket_id>/', views.createNewNote, name='createNewNote'),
    path('deleteNote/<str:note_id>/', views.deleteNote, name='deleteNote'),
    path('updateNote/<str:note_id>/', views.updateNote, name='updateNote'),
]