from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Inventory, InventoryItem,Abilities,Effects
from .serializer import AbilitySerializer,InventorySerializer
from rest_framework.views import APIView


# @csrf_exempt
class CreateInventory(APIView):
    def post(self,request):
        name = request.data['name']
        owner=request.data['owner']
        if not name:
            return JsonResponse({'error': 'Please provide a name for the inventory'})
        inventory = Inventory.objects.create(Name=name,Owner=owner)
        return JsonResponse({'success': 'Inventory created successfully'})





# def create_inventory(request):
#     if request.method == 'POST':
        
class getInventories(APIView):
    def post(self,request):
        owner=request.data['owner']
        inventories = Inventory.objects.filter(Owner=owner)
        invs= InventorySerializer(Inventory.objects.filter(Owner=owner),many=True).data
        return JsonResponse({'inventories': invs})

       



class UpdateInventory(APIView):
    def put(self,request, inventory_id):
        
        owner = request.data['owner']
        inventory = Inventory.objects.filter(id=inventory_id,Owner=request.data['owner'])
       
        name = request.data['name']
        if name and inventory:
            # Update other fields here
            inventory.update(Name='name',Owner=request.data["newOwner"])
            return JsonResponse({'success': 'Inventory updated successfully'})
        else:
            return JsonResponse({'failed': 'you\'re not the owner'})


class delete_inventory(APIView):
    def delete(self,request, inventory_id,owner):
        if request.method == 'DELETE':        
            inventory = get_object_or_404(Inventory, id=inventory_id, Owner=owner)
            inventory.delete()
            return JsonResponse({'success': 'Inventory deleted successfully'})


class create_inventory_item(APIView):
    def post(self,request):
            item_name = request.data['item_name']
            quantity = request.data['quantity']
            informationIndex = request.data['informationIndex']
            if not (item_name and quantity and informationIndex):
                return JsonResponse({'error': 'Please provide an item name and quantity'})
            item = InventoryItem.objects.create( item_name=item_name, quantity=quantity,informationIndex=informationIndex)
            for ability in request.data['Abilities']:
                ablty= Abilities.objects.get(id=ability)
                item.Abilities.add(ablty)
            item.save()
            return JsonResponse({'success': 'Inventory item created successfully'})





# class update_inventory_item(APIView):
#     def put(self,request, inventory_id, item_id):
#         if request.method == 'PUT':
            
#             Owner=request.data('Owner')
#             inventory = get_object_or_404(Inventory, id=inventory_id, Owner=Owner)
#             item = InventoryItems.objects.get( id=item_id)
#             item_name = request.data('item_name')
#             quantity = request.data('quantity')
#             if item_name:
#                 item.item_name = item_name
#             if quantity:
#                 item.quantity = quantity
#             for ability in request.data['Abilities']:
#                 ablty= Abilities.objects.get(id=ability)
#                 item.Abilities.add(ablty)
#             # Update other fields here
#             item.save()
#             return JsonResponse({'success': 'Inventory item updated successfully'})


class delete_inventory_item(APIView):
    def delete(self,request, inventory_id, item_id,Owner):
        if request.method == 'DELETE':
            
            inventory = get_object_or_404(Inventory, id=inventory_id, Owner=Owner)
            item = get_object_or_404(InventoryItem, id=item_id, inventory=inventory)
            item.delete()
            return JsonResponse({'success': 'Inventory item deleted successfully'})

        
class CreateAbility(APIView):
    def post(self,request):
        if not(request.data['AbilityName'] and request.data['AbilityID']):
            return JsonResponse({'error': 'Please provide a name for the inventory'})
        ability=Abilities.objects.create(AbilityName=request.data['AbilityName'],Level=1,AbilityID=request.data['AbilityID'])
        return JsonResponse({'success': 'Ability Created Succesfully'})

class AddItemTOInventory(APIView):
    def put(self,request,inventory_id):
        inventory = Inventory.objects.get(id=inventory_id)
        for item in request.data['Items']:
            _item = InventoryItem.objects.get(id=item)
            inventory.Items.add(_item)
        inventory.save()
        return JsonResponse({'success': 'Update Inventory Succesfully'})
