from django.urls import path
from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
urlpatterns = [
    path('' , ProductListView.as_view() , name='home-page'),
    path('view/<int:pk>' , ProductDetailView.as_view() , name='view-product'),
    path('new/' , ProductCreateView.as_view(), name='create-product'),
    path('update/<int:pk>' , ProductUpdateView.as_view() , name='update-product'),
    path('delete/<int:pk>' , ProductDeleteView.as_view() , name='delete-product'),
]
