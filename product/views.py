from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductForm
# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'product/productList.html'
    context_object_name = 'products'
    ordering = ['-created']
    # paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/productDetail.html'
    context_object_name = 'product'
    # pk_url_kwarg = 'id' the default is pk

class ProductCreateView(SuccessMessageMixin , CreateView):
    model = Product
    form_class = ProductForm
    # success_url =  reverse_lazy('home-page')
    success_message = 'Product successfully created!'
    template_name = 'product/productForm.html'

class ProductUpdateView(SuccessMessageMixin , UpdateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('home-page')
    success_message = 'Product successfully updated!'
    template_name = 'product/productForm.html'

class ProductDeleteView(SuccessMessageMixin , DeleteView):
    model = Product
    success_url = reverse_lazy('home-page')
    success_message = 'Product successfully deleted!'
    template_name = 'product/confirmDelete.html'
    context_object_name = 'product'
