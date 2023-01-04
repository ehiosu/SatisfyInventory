"""SatisfyInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory.views import CreateInventory,getInventories,UpdateInventory,delete_inventory,create_inventory_item,CreateAbility,create_inventory_item,AddItemTOInventory

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Satisfy/CreateInventory",CreateInventory.as_view()),
    path("Satisfy/getInventories",getInventories.as_view()),
    path("Satisfy/UpdateInventory/<int:inventory_id>",UpdateInventory.as_view()),
    path("Satisfy/DeleteInventory/<int:inventory_id>/<str:owner>",delete_inventory.as_view()),
    path("Satisfy/CreateItem/<int:inventory_id>/<str:owner>",delete_inventory.as_view()),
    path("Satisfy/CreateAbility",CreateAbility.as_view()),
    path("Satisfy/CreateInventoryItem",create_inventory_item.as_view()),
    path("Satisfy/AddItemToInventory/<int:inventory_id>",AddItemTOInventory.as_view())
]
