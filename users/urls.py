from django.urls import path
from .views import UserRegistrationView, UserLoginView, CustomLogoutView, CustomLogoutSuccessView

app_name = 'users'


urlpatterns= [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('logged-out/', CustomLogoutSuccessView.as_view(), name='logged-out'),

]