from django.urls import path
from .views import LoginView, LogoutView


login_patterns = ([
    path('',LoginView.as_view(), name='login'),        
    path('logout/',LogoutView.as_view(),name='logout'),
],'login')