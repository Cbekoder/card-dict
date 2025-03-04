from django.urls import path
from .views import RegisterView, GetMeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('get-me/', GetMeView.as_view(), name='get-me')
]
