from django.shortcuts import render
from rest_framework.response import Response  # Import from REST Framework
from rest_framework.decorators import api_view

from .filters import ProductsFilter # Import for API view
from .models import Product
from .serializers import ProductSerializer  # Assuming a serializer for Product
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET'])
def get_products(request):
  #products = Product.objects.all()
  filterset  = ProductsFilter(request.GET, queryset= Product.objects.all().order_by('id'))
  
  count = filterset.qs.count()
  
  
  resPerPage = 1
  paginator = PageNumberPagination()
  paginator.page_size = resPerPage
  
  queryset = paginator.paginate_queryset(filterset.qs, request)
  
  serializer = ProductSerializer(queryset, many=True)
  return Response({
    'count':count,
    'resPerPage':resPerPage,
    'Products' : serializer.data 
    })



@api_view(['GET'])
def get_product(request, pk):
  product = get_object_or_404(Product, id=pk)
  serializer = ProductSerializer(product, many=False)
  return Response({"product" :serializer.data })