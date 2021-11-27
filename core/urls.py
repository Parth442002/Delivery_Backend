from django.urls import path
from . import views

urlpatterns = [
    path("house/<int:pk>/", views.HouseView.as_view(), name='houseview'),
]
