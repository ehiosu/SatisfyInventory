from django.contrib import admin
from django.urls import path
from views import create_inventory

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

