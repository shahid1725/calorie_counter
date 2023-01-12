from django.shortcuts import render
from rest_framework import generics, mixins
from foodtracker.models import FoodCategory,Food,User,\
    FoodLog,Weight
from .serializers import FoodCategorySerializer,\
    FoodLogSerializer,WeightSerializer
# Create your views here.

# -------------------------------Food Category -------------------------------------------------------
class FoodCategoryApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# -------------------------------Food Category -------------------------------------------------------
class FoodLogApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# -------------------------------Weight -------------------------------------------------------
class WeightApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
