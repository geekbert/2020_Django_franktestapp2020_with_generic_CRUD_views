from django.db import models

# Create your models here.

class Entity(models.Model): # PK will be Entity_id
    entity_name = models.CharField(max_length=200)
    def __str__(self): 
        return self.entity_name # # so it displays in admin


class yearlydata(models.Model): # PK will be yearlydata_id
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE) # many-to-one relationship
    year = models.IntegerField() # warning: max_length ignored with integer field
    def __str__(self):
        return str(self.year) # so it displays in admin 
    # add: date_added like date_pub before
    revenues = models.IntegerField()  
    people = models.IntegerField()  



