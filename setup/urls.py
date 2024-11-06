from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # accounts
    path('register/', include('accounts.urls')),
    path('', include('sistema.urls')),
]
