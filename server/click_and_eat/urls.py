from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth import Login, Register, Logout
from .views.index import Index
from .views.restaurant import *
from .views.restaurateur import *
from .simple_views import *
from .views.account import *
urlpatterns = [
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('auth/logout', Logout.as_view(), name='logout'),
    path('', Index.as_view(), name='index'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile/password_change', PasswordChange.as_view(), name='password_change'),
    path('habits', Habits.as_view(), name='habits'),
    path('history', History.as_view(), name='history'),
    path('allergy', Allergy.as_view(), name='allergy'),
    path('settings', Settings.as_view(), name='settings'),
    path('restaurateur', Restaurateur.as_view(), name='restaurateur'),
    path('restaurateur/register_form', RestaurantRegister.as_view(), name='restaurant_register_form'),
    path('restaurateur/register', RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurateur/dashboard', RestaurateurDashboard.as_view(), name='restaurateur_dashboard'),
    path('restaurateur/restaurant/<int:restaurant_id>', RestaurantDashboard.as_view(), name='restaurant_dashboard'),
    path('restaurateur/restaurant/<int:restaurant_id>/edit', RestaurantEdit.as_view(), name='restaurant_edit'),
    path('restaurateur/restaurant/<int:restaurant_id>/category/add', RestaurantAddCategory.as_view(),
         name='restaurant_add_category'),
    path('restaurateur/restaurant/<int:restaurant_id>/category/edit/<int:category_id>', RestaurantAddCategory.as_view(),
         name='restaurant_edit_category'),
    path('restaurateur/restaurant/<int:restaurant_id>/category/delete/<int:category_id>',
         RestaurantDeleteCategory.as_view(),
         name='restaurant_delete_category'),
    path('restaurateur/restaurant/<int:restaurant_id>/products/add', RestaurantAddProduct.as_view(),
         name='restaurant_add_product'),
    path('restaurateur/restaurant/<int:restaurant_id>/products/edit/<int:product_id>', RestaurantAddProduct.as_view(),
         name='restaurant_edit_product'),
    path('restaurateur/restaurant/<int:restaurant_id>/products/delete/<int:product_id>', RestaurantDeleteProduct.as_view(),
         name='restaurant_delete_product'),
    path('restaurateur/restauratn/<int:restaurant_id>/addresses/add', RestaurantAddAddress.as_view(),
         name='restaurant_add_address'),
    path('restaurateur/restauratn/<int:restaurant_id>/addresses/edit/<int:address_id>', RestaurantAddAddress.as_view(),
         name='restaurant_edit_address'),
    path('restaurateur/restauratn/<int:restaurant_id>/addresses/delete/<int:address_id>',
         RestaurantDeleteAddress.as_view(),
         name='restaurant_delete_address'),

    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view(), name='restaurant'),
    path('cart/add/<int:product_id>/<int:count>', CartAdd.as_view(),
         name='cart_add'),
    path('cart/delete/<int:product_id>/<int:count>', CartDelete.as_view(),
         name='cart_delete'),
    path('cart/remove/<int:product_id>', CartRemove.as_view(), name='cart_remove'),
    path('cart/clear', CartClear.as_view(),
         name='cart_clear'),
    path('cart/view', CartViewComponent.as_view(),
         name='cart_view'),
    path('map', restaurant_map, name="restaurant_map"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

