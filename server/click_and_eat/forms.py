from django import forms
from django.forms import ModelForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)


class RegisterForm(LoginForm):
    first_name = forms.CharField(max_length=12)
    email = forms.EmailField()
    repeat_password = forms.CharField(widget=forms.PasswordInput())


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
       


class RestaurantEditForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['title', 'description', 'logo', 'preview_image', 'open_time', 'close_time']


class CategoryModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class RestaurantAddProductForm(ModelForm):
    def set_restaurant(self, restaurant):
        self.fields['category'].queryset = Category.objects.filter(restaurant=restaurant)

    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'price', 'value', 'category']
        field_classes = {'category': CategoryModelChoiceField}
        widgets = {
            'category': forms.Select(attrs={'class': 'uk-select'}),
        }


class RestaurantAddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class RestaurantAddressForm(ModelForm):
    class Meta:
        model = AddressOfRestaurant
        fields = ['address', 'longitude', 'latitude']
