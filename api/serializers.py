from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from foodtracker.models import FoodCategory,Food,User,\
    FoodLog,Weight


class FoodSerializer(ModelSerializer):
    food_name = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Food
        fields = "__all__"


class FoodCategorySerializer(ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = "__all__"

class FoodLogSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    food_consumed = serializers.StringRelatedField()

    class Meta:
        model = FoodLog
        fields = "__all__"

class WeightSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Weight
        fields = "__all__"