from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth import Login, Register, Logout
from .views.index import Index
from .views.restaurant import *
from .views.restaurateur import *
from .simple_views import *
from .views.account import *
from .views.cart import *
from .views.main import *
from .views.address import *

urlpatterns = [
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('auth/logout', Logout.as_view(), name='logout'),
    path('', Index.as_view(), name='index'),
    path('profile', ProfileView.as_view(), name='profile'),
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
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/add', RestaurantAddAddress.as_view(),
         name='restaurant_add_address'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/edit/<int:address_id>', RestaurantAddAddress.as_view(),
         name='restaurant_edit_address'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/delete/<int:address_id>',
         RestaurantDeleteAddress.as_view(),
         name='restaurant_delete_address'),

    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>',
         RestaurantAddressDashboard.as_view(),
         name='restaurant_address_dashboard'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/orders_contents',
         RestaurantAddressOrdersContents.as_view(),
         name='restaurant_address_orders_contents'),

    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/order/<int:order_id>',
         RestaurantAddressOrder.as_view(),
         name='restaurant_address_order'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/order/<int:order_id>/contents',
         RestaurantAddressOrderContents.as_view(),
         name='restaurant_address_order_contents'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/order/<int:order_id>/in_progress',
         RestaurantAddressOrderInProgress.as_view(),
         name='restaurant_address_order_in_progress'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/order/<int:order_id>/cancel',
         RestaurantAddressOrderCancel.as_view(),
         name='restaurant_address_order_cancel'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/order/<int:order_id>/ready',
         RestaurantAddressOrderReady.as_view(),
         name='restaurant_address_order_ready'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/orders',
         RestaurantAddressOrdersMonitor.as_view(),
         name='restaurant_address_order_monitor'),
    path('restaurateur/restaurant/<int:restaurant_id>/addresses/<int:address_id>/orders_monitor_contents',
         RestaurantAddressOrdersMonitorContents.as_view(),
         name='restaurant_address_order_monitor_contents'),


    path('restaurant/<int:restaurant_id>/', RestaurantView.as_view(), name='restaurant'),
    path('restaurant_address', RestaurantAddressView.as_view(), name='restaurant_address'),
    path('order/<int:order_id>', OrderView.as_view(), name='order'),
    path('order/<int:order_id>/contents', OrderContentsView.as_view(), name='order_contents'),
    path('checkout', Checkout.as_view(), name='checkout'),

    path('cart/add/<int:product_id>/<int:count>', CartAdd.as_view(),
         name='cart_add'),
    path('cart/delete/<int:product_id>/<int:count>', CartDelete.as_view(),
         name='cart_delete'),
    path('cart/remove/<int:product_id>', CartRemove.as_view(), name='cart_remove'),
    path('cart/clear', CartClear.as_view(),
         name='cart_clear'),
    path('cart/view', CartViewComponent.as_view(),
         name='cart_view'),
    path('cart/checkout_view', CartCheckoutViewComponent.as_view(), name='cart_checkout_view'),
    path('cart/set_address', CartSetAddress.as_view(), name='cart_set_address'),

    path('map_contents', restaurants_map_data, name="restaurants_map_data"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

