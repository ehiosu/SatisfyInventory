from django.db import models

class Abilities(models.Model):
    AbilityName=models.TextField(max_length=1000)
    Level=models.PositiveIntegerField(default=1)
    AbilityID=models.PositiveIntegerField(default=1)
    class Meta:
   

        def __str__(self):
            return self.AbilityName

       

class Effects (models.Model):
    EffectName=models.TextField(max_length=1000)
 
    Level=models.PositiveIntegerField(default=1)
    AbilityID=models.PositiveIntegerField(default=1)

    class Meta:
      

        def __str__(self):
            return self.Effect

     
class InventoryItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    informationIndex= models.PositiveIntegerField()
    Abilities = models.ManyToManyField(Abilities)
    Effects = models.ManyToManyField(Effects)
# Create your models here.
class Inventory(models.Model):
    Name=models.CharField( max_length=250)
    Owner=models.TextField(max_length=1000)
    Items = models.ManyToManyField(InventoryItem)

