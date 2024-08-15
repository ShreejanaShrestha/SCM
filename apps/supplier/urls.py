from django.urls import path
from .views import supplier_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('supplier/', supplier_view, name="supplier_view"),
    # path('register/', register_user, name="register"),
]
