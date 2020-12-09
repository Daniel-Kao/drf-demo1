from django.urls import path
from . import views

urlpatterns = [
    path(
        'auth/login/',
        views.TokenObtainPairAndUserView.as_view(),
        name='auth-login'
    )
]
