from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth import Login, Register, Logout
from .views.index import Index
from .views.restaurant import *
from .views.restaurateur import *
from .simple_views import *

urlpatterns = [
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('auth/logout', Logout.as_view(), name='logout'),
    path('', Index.as_view(), name='index'),
    path('restaurateur', Restaurateur.as_view(), name='restaurateur'),
    path('restaurateur/register_form', RestaurantRegister.as_view(), name='restaurant_register_form'),
    path('restaurateur/register', RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurateur/dashboard', RestaurateurDashboard.as_view(), name='restaurateur_dashboard'),
    path('restaurateur/restaurant/<int:restaurant_id>', RestaurantDashboard.as_view(), name='restaurant_dashboard'),
    path('restaurateur/restaurant/<int:restaurant_id>/edit', RestaurantEdit.as_view(), name='restaurant_edit'),
    path('restaurateur/restaurant/<int:restaurant_id>/add_category', RestaurantAddCategory.as_view(),
         name='restaurant_add_category'),
    path('restaurateur/restaurant/<int:restaurant_id>/edit_category/<int:category_id>', RestaurantAddCategory.as_view(),
         name='restaurant_edit_category'),
    path('restaurateur/restaurant/<int:restaurant_id>/add_product', RestaurantAddProduct.as_view(),
         name='restaurant_menu_create'),
    path('restaurateur/restaurant/<int:restaurant_id>/edit_product/<int:product_id>', RestaurantAddProduct.as_view(),
         name='restaurant_edit_product'),
    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view(), name='restaurant'),
    path('map/', restaurant_map, name="restaurant_map"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

