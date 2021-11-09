
from django.urls import path
from .views import sign_up, login_page, logout_user


urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
]
