from django.urls import path
from . import views

urlpatterns = [

    path("category", views.FoodCategoryApi.as_view()),
    path("foodlog", views.FoodLogApi.as_view()),
    path("weight", views.WeightApi.as_view()),

]