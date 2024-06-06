from django.db import models

class Product(models.Model):
    vendor_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='categories')
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    text = models.TextField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.name

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name