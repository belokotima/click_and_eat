from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.auth import Login, Register
from .views.index import Index
from . import simple_views

urlpatterns = [
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('', Index.as_view(), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)