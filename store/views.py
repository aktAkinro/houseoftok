from drf_yasg.utils import swagger_auto_schema
# from store.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly, ViewCustomerHistoryPermission
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import  AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes, renderer_classes, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import renderers
from .models import Product
from .serializers import ProductSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.shortcuts import render
# from account.models import IsSuperUser



@swagger_auto_schema(methods=['POST'], request_body=ProductSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('category').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=ProductSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)