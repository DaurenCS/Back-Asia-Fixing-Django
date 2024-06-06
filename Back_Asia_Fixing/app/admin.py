from django.contrib import admin

from .models import Product, ProductImage, Category, Type, Technology, Certificate, UploadedFile

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Technology)
admin.site.register(Certificate)
admin.site.register(UploadedFile)
