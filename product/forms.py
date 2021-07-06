from django.forms import ModelForm

from .models import Product

class ProductForm(ModelForm):
    def __init__(self , *args , **kwargs):
        super(ProductForm , self).__init__(*args , **kwargs)
        self.fields['name'].widget.attrs = {
            'class':'form-control col-md-6' ,
            'placeholder':'Product\'s Name',
        }
        self.fields['description'].widget.attrs = {
            'class':'form-control col-md-6',
            'placeholder':'Product\'s Description',
        }
        self.fields['price'].widget.attrs = {
            'class':'form-control col-md-6' ,
            'placeholder':'Product\'s Price',
            'step':'any' ,
            'min':'1',
        }
    class Meta:
        model = Product
        fields = ['name' , 'description' , 'price']
