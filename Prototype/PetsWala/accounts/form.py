from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms import widgets
from .models import User, Vendor, Profile
from marketplace.models import Category, Product

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        return user


class VendorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    product_category = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        vendor = Vendor.objects.create(user=user)
        vendor.address = self.cleaned_data.get('address')
        user.is_vendor = True
        vendor.product_category = self.cleaned_data.get('product_category')
        vendor.save()
        return user

class UserUpdateForm(forms.ModelForm):              #Add email later
    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class AddNewProduct(forms.ModelForm):         #Implement add_product form here
    # category = forms.Select()
    # vendor = forms.Select()
    # title = forms.CharField(required=True)
    # slug = forms.CharField(required=True)
    # description = forms.CharField(required=True)
    # price = forms.DecimalField(required=True)
    # image = forms.ImageField(required=True)
    # thumbnail = forms.ImageField(required=True)

    class Meta:
        model = Product
        fields = ['title', 'vendor', 'slug','category', 'description', 'price', 'image', 'thumbnail']

        widgets={
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Product Title here..."
            }),
            'slug': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Unique Slug here..."
            }),
            'category': forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Enter Product Category here..."
            }),
             'vendor': forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Enter Product Category here..."
            }),
            'description': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter Product Description here...",
                "rows": 4
            }),
            'price': forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Price"
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),

        }

    # @transaction.atomic
    # def save(self):
    #     product = super().save(commit=False)
    #     product.title = self.cleaned_data.get('title')
    #     product.description = self.cleaned_data.get('description')
    #     product.price = self.cleaned_data.get('price')
    #     product.image = self.cleaned_data.get('image')
    #     product.thumbnail = self.cleaned_data.get('thumbnail')
    #     product.save()
    #     return product


