from django.shortcuts import render
from rest_framework import generics, mixins
from foodtracker.models import FoodCategory,Food,User,\
    FoodLog,Weight
from rest_framework.response import Response

from .serializers import FoodCategorySerializer,\
    FoodLogSerializer,WeightSerializer,FoodSerializer
# Create your views here.

# -------------------------------Food Category -------------------------------------------------------
class FoodCategoryApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        id = self.request.data.get("id")
        queryset = FoodCategory.objects.get(id=id)
        serializer = FoodCategorySerializer(queryset)
        return Response(serializer.data)



    # -------------------------------Food -------------------------------------------------------

class FoodApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        food_name = self.request.data.get("food_name")
        category = self.request.data.get("category")


        queryset = Food.objects.filter(food_name=food_name,category__category_name=category)
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)


# -------------------------------Food Log -------------------------------------------------------
class FoodLogApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        user = self.request.data.get("user")
        queryset = FoodLog.objects.filter(user__username=user)
        serializer = FoodLogSerializer(queryset, many=True)
        return Response(serializer.data)

# -------------------------------Weight -------------------------------------------------------
class WeightApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.data.get("user")
        queryset = Weight.objects.filter(user__username=user)
        serializer = WeightSerializer(queryset, many=True)
        return Response(serializer.data)
