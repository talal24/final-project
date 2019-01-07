from django.forms import ModelForm, TextInput
from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create the form class.
class ProductForm(ModelForm):
    # name1 = forms.CharField(max_length= 50)
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'image', 'quantity', 'user')

        widgets = {
            'name': TextInput(attrs={'class': 'custom-class', 'placeholder': 'الاسم هنا'})
        }
        labels = {
            'name': 'name for product'
        }
        help_texts = {
            'name': 'name for product must be string'
        }
        error_messages = {

        }

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        name = cleaned_data.get('name')
        products = Product.objects.all()
        product_name = []
        for item in products:
            product_name.append(item.name)
        if name in product_name:
            self.add_error('name', 'this name is sjkdhfsjkfhskjddf')


class EditProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'password1', 'password2')


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    name = forms.CharField(required=False, initial=False, widget=forms.HiddenInput)
