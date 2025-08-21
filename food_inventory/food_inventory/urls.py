from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # User panel (signup, login, logout, dashboard)
    path("accounts/", include("users.urls")),  

    # Inventory app routes
    path("", include("inventory.urls")),
]
