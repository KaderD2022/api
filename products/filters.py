from django_filters import rest_framework as filters

from .models import Product

class ProductsFilter(filters.FilterSet):
  keyword = filters.Filter(field_name="name", lookup_expr="icontains")
  category = filters.Filter(field_name="category", lookup_expr="icontains")
  min_price = filters.Filter(field_name="price" or 0 , lookup_expr="gte")
  max_price = filters.Filter(field_name="price" or 1000000 , lookup_expr="lte")
  min_ratings = filters.Filter(field_name="ratings" or 0 , lookup_expr="gte")
  max_ratings = filters.Filter(field_name="ratings" or 1000000 , lookup_expr="lte")
  
  model = Product
  fields = ('category', 'ratings',   'keyword', 'min_price', 'max_price')
   