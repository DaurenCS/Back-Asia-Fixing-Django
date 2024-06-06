from django.urls import path
from .views import (
    ProductListView, InstallationProductListView, ProductsByCategoryView, 
    ProductsByTypeView, ProductDetailsView, TechnologyListView, CategoryListView, 
    HidroIsolationCategoryListView, CategoriesByTypeView, TypeListView,IsolationCertificateListView, InstallationCertificateListView,
    TypesWithCategoriesView,FileListView, CertificateUploadView
)
from .views import FileUploadView

urlpatterns = [
    path('products', ProductListView.as_view(), name='product-list'),
    path('installation/products', InstallationProductListView.as_view(), name='installation-product-list'),
    path('products/category/<int:category_id>', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('products/type/<int:type_id>', ProductsByTypeView.as_view(), name='products-by-type'),
    path('products/<int:id>', ProductDetailsView.as_view(), name='product-details'),
    path('technologies', TechnologyListView.as_view(), name='technology-list'),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('products/isolation/categories', HidroIsolationCategoryListView.as_view(), name='hidro-isolation-categories'),
    path('categories/<int:type_id>', CategoriesByTypeView.as_view(), name='categories-by-type'),
    path('types', TypeListView.as_view(), name='type-list'),
    path('types-with-categories', TypesWithCategoriesView.as_view(), name='types-with-categories'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('certificates/isolation/', IsolationCertificateListView.as_view(), name='isolation-certificates'),
    path('certificates/installation/', InstallationCertificateListView.as_view(), name='installation-certificates'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('upload_certificate/', CertificateUploadView.as_view(), name='certificate-upload'),

]
