from django.urls import path
from sistema.views import index

urlpatterns = [
  path('', index)
]