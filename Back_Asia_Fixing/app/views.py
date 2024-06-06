from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Product, ProductImage, Category, Type, Technology, Certificate
from .serializer import (
    ProductSerializer, ProductDetailsSerializer, CategorySerializer, 
    TypeSerializer, TechnologySerializer, CertificateSerializer
)

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        return Product.objects.filter(local=local)

class InstallationProductListView(generics.ListAPIView):
    serializer_class = ProductDetailsSerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        return Product.objects.filter(local=local, price__gt=0)

class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

class ProductsByTypeView(generics.ListAPIView):
    serializer_class = ProductDetailsSerializer

    def get_queryset(self):
        type_id = self.kwargs['type_id']
        return Product.objects.filter(category__type_id=type_id)

class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'

class TechnologyListView(generics.ListAPIView):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        return Technology.objects.filter(local=local)

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        return Category.objects.filter(local=local)

class HidroIsolationCategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        type_name = "Hidroisolation" if local == "en" else "Гидроизоляция"
        type_instance = Type.objects.filter(name=type_name).first()
        if not type_instance:
            raise NotFound(detail="Type 'HidroIsolation' not found")
        return Category.objects.filter(type_id=type_instance.id)

class CategoriesByTypeView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        type_id = self.kwargs['type_id']
        return Category.objects.filter(type_id=type_id)

class TypeListView(generics.ListAPIView):
    serializer_class = TypeSerializer

    def get_queryset(self):
        local = self.request.query_params.get('local')
        return Type.objects.filter(local=local)

class TypesWithCategoriesView(generics.ListAPIView):
    serializer_class = TypeSerializer

    def list(self, request, *args, **kwargs):
        local = request.query_params.get('local')
        types = Type.objects.filter(local=local).exclude(name__in=["Гидроизоляция", "Hidroisolation"])
        if not types:
            raise NotFound(detail="No types found")

        response_data = []
        for type_instance in types:
            categories = Category.objects.filter(type_id=type_instance.id)
            category_serializer = CategorySerializer(categories, many=True)
            type_data = {
                "id": type_instance.id,
                "name": type_instance.name,
                "description": type_instance.description,
                "categories": category_serializer.data
            }
            response_data.append(type_data)
        
        return Response(response_data)

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import UploadedFile
from .serializer import UploadedFileSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FileListView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer


class IsolationCertificateListView(generics.ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.filter(description="isolation")

class InstallationCertificateListView(generics.ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.filter(description="installation")
    
class CertificateUploadView(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)