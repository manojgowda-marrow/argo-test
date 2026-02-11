from django.urls import path
from api.views import health, name

urlpatterns = [
    path('health/', health, name='health v2'),
    path('name/', name, name='name'),
]
