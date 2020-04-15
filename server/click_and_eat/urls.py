from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth import Login, Register, Logout
from .views.index import Index
from .views.restaurateur import *

urlpatterns = [
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('auth/logout', Logout.as_view(), name='logout'),
    path('', Index.as_view(), name='index'),
    path('restaurateur', Restaurateur.as_view(), name='restaurateur'),
    path('restaurateur/register_form', RestaurantRegister.as_view(), name='restaurant_register_form'),
    path('restaurateur/register', RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurateur/restaurant/<str:restaurante_id>/', RestaurantMenu.as_view(), name='restaurant'),
    path('restaurateur/menu', RestaurantMenuAdd.as_view(), name='menu_create')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)