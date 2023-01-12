from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
import datetime
from . import forms
from foodtracker.models import FoodCategory,Food,User
from foodtracker.forms import FoodCategoryForm,FoodForm


# Create your views here.

class Signup(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {}
        context["form"] = form
        return render(request, "admin_signup.html", context)

    def post(self,request):
        context={}
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminlogin")
        else:
            context["form"] = form
            return render(request, "admin_signup.html", context)

class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {"form": form}
        return render(request, "admin_login.html", context)

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("dashboard")

            else:
                return render(request, "admin_login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("adminlogin")


class Dashboard(TemplateView):
    template_name = "dashboard.html"

#------------------------- FOOD CATEGORY -----------------------

class AddcategoryView(CreateView):
    template_name = "admin_food_category_add.html"
    model = FoodCategory
    form_class = FoodCategoryForm
    success_url = reverse_lazy("category")

class ListcategoryView(ListView):
    template_name = "admin_food_category_list.html"
    model = FoodCategory
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.model.objects.all()
        return context

class EditcategoryView(UpdateView):
    template_name = "admin_food_category_edit.html"
    model = FoodCategory
    form_class = FoodCategoryForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("category")

def delete_category(request, id):
  data = FoodCategory.objects.get(id=id)
  data.delete()
  return HttpResponseRedirect(reverse('category'))

#------------------------- FOOD -----------------------

class AddFoodView(CreateView):
    template_name = "admin_food_add.html"
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy("food")

class ListFoodView(ListView):
    template_name = "admin_food_list.html"
    model = Food
    context_object_name = "food"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food"] = self.model.objects.all()
        return context

class EditFoodView(UpdateView):
    template_name = "admin_food_edit.html"
    model = Food
    form_class = FoodForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("food")

#------------------------- Users -----------------------


class ListUserView(ListView):
    template_name = "user_list.html"
    model = User
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = self.model.objects.all()
        return context



#------------------------- EDUCATION -----------------------

def delete_food(request, id):
  data = Food.objects.get(id=id)
  data.delete()
  return HttpResponseRedirect(reverse('food'))

