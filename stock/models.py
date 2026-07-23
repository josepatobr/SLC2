from django.db import models

class ProductStatus(models.TextChoices):
    IN_STOCK = 'IN_STOCK', 'Em Estoque'
    EXHAUSTED = 'EXHAUSTED', 'Esgotado'

class Product(models.Model):
    product_status = models.CharField(
        max_length=20, 
        choices=ProductStatus.choices, 
        default=ProductStatus.EXHAUSTED
    )
    
    name_product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_quantity = models.IntegerField(default=0) 

    sku = models.CharField(max_length=50, unique=True)
    product_image = models.ImageField(upload_to='products/')
    
    # Detalhes do vendedor
    seller_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_number = models.CharField(max_length=15, blank=True, null=True) 
    company_ender = models.CharField(max_length=200, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name_product
    
    def save(self, *args, **kwargs):
        if self.stock_quantity > 0:
            self.product_status = ProductStatus.IN_STOCK
        else:
            self.product_status = ProductStatus.EXHAUSTED
        super().save(*args, **kwargs)


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_out = models.IntegerField(verbose_name="Quantidade Retirada")
    date_moved = models.DateTimeField(auto_now_add=True, verbose_name="Data da Saída")

    def __str__(self):
        return f"Saída de {self.quantity_out} unidade(s) de {self.product.name_product}"