
from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('ticket/new/', views.ticket_create, name='ticket_create'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:pk>/resolve/', views.ticket_resolve, name='ticket_resolve'),
    
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]


