from django.urls import path
from .views import registration, userLogin, userLogout, profile, update_profile, delete_profile

urlpatterns = [
    path('registration/', registration, name='registr'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('profile/<int:uid>/', profile, name='profile'), 
    path('update-profile/<int:uid>/', update_profile, name='update-profile'), 
    path('delete-profile/<int:uid>/', delete_profile, name='delete-profile'),
]
