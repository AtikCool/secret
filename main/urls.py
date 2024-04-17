from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    path('AlfiaILoveYou/', views.main, name='main'),
    path('login/', views.signin_view, name='login')
]
