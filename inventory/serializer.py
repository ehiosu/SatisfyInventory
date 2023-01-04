from  rest_framework import serializers
from .models import Inventory,InventoryItem,Abilities,Effects


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields="__all__"
        depth=1

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryItem
        fields="__all__"
        depth=1

class AbilitySerializer(serializers.ModelSerializer):

     class Meta:
        model=Abilities
        fields="__all__"
        depth=1