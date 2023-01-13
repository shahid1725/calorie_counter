from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import UserFood
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserFoodForm(forms.ModelForm):
    '''
    A ModelForm class for adding a new food item
    '''
    class Meta:
        model = UserFood
        fields = ['food_name', 'quantity', 'calories', 'fat', 'carbohydrates', 'protein', 'category_food','food_image']

    def __init__(self, *args, **kwargs):
        super(UserFoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'