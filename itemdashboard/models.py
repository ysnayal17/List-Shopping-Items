from django.db import models

# Create your models here.
class Item(models.Model):
    itemid        = models.AutoField(primary_key=True)
    item          = models.CharField(max_length=100)
    quantity      = models.IntegerField(default=1)
    bought        = models.BooleanField(default=False)

    def __str__(self):
        return self.item
