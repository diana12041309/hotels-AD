from django.urls import path
from .views import registration, userLogin, userLogout

urlpatterns = [
    path('registration/', registration, name='registr'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
]
