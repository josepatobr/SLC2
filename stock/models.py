from django.db import models, transaction


class ProductStatus(models.TextChoices):
    IN_STOCK = 'IN_STOCK', 'Em Estoque'
    EXHAUSTED = 'EXHAUSTED', 'Esgotado'


class Company(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=15, blank=True, null=True)
    ender = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='seller_images/', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_status = models.CharField(
        max_length=20, 
        choices=ProductStatus.choices, 
        default=ProductStatus.EXHAUSTED
    )

    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    name_product = models.CharField(max_length=200)
    stock_quantity = models.IntegerField(default=0) 

    price = models.FloatField(default=0, verbose_name=f"Preço de venda (R$)")
    price_restocking = models.FloatField(verbose_name="Preço para reabastecer", default=0)

    sku = models.CharField(max_length=50, unique=True)
    product_image = models.ImageField(upload_to='products/')

    
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
    quantity_out = models.IntegerField(verbose_name="Quantidades vendidas")
    date_moved = models.DateTimeField(auto_now_add=True, verbose_name="Data da venda")
    profits = models.FloatField(default=0, verbose_name="Lucro da Venda")

    def __str__(self):
        return f"Foi vendido o total de: {self.quantity_out} unidade(s) do produto: {self.product.name_product}"

    def save(self, *args, **kwargs):
        if self.product:
            total_sales = float(self.product.price) * self.quantity_out
            self.profits = total_sales - self.product.price_restocking

        with transaction.atomic():
            is_new = self.pk is None
            super().save(*args, **kwargs)

        if is_new:
            Product.objects.filter(pk=self.product.pk).update(
                stock_quantity=models.F('stock_quantity') - self.quantity_out
                )
            self.product.refresh_from_db(fields=['stock_quantity'])

