from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default='Опис відсутній')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # 8 полів:
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    # Поле з choices:
    STATUS_CHOICES = [
        ('new', 'New'),
        ('sale', 'Sale'),
        ('old', 'Old'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.name

