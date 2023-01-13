from django.db import models

from foodtracker.models import FoodCategory


# Create your models here.

class UserFood(models.Model):
    food_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0,null=True)
    fat = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    protein = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    category_food = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='category_food',null=True)
    food_image = models.ImageField(upload_to='images/',null=False)

    def __str__(self):
        return f'{self.food_name} - category: {self.category_food}'