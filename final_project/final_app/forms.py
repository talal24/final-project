from django.forms import ModelForm, TextInput
from .models import Product
from django import forms


# Create the form class.
class ProductForm(ModelForm):
    # name1 = forms.CharField(max_length= 50)
    class Meta:
        model = Product
        fields = ('name', 'price', 'category')

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

