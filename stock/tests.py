from django.test import TestCase
from .models import Company, Seller, Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Empresa Teste")
        self.seller = Seller.objects.create(name="Vendedor Teste", company=self.company)

    def test_product_status_in_stock(self):
            product = Product.objects.create(
                name_product="Produto A",
                price=10.00,
                stock_quantity=5,
                sku="SKU123",
                seller=self.seller
            )
            self.assertEqual(product.product_status, "IN_STOCK")

    def test_product_status_exhausted(self):
        product = Product.objects.create(
            name_product="Produto B",
            price=15.00,
            stock_quantity=0,
            sku="SKU456",
            seller=self.seller
        )
        self.assertEqual(product.product_status, "EXHAUSTED")

    def test_update_quantity_A(self):
        product = Product.objects.create(
            name_product="Camisa",
            price=50.00,
            stock_quantity=10,
            sku="CAMISA-01",
            seller=self.seller
        )

        quantity_out = 3

        product.stock_quantity -= quantity_out
        product.save()

        product.refresh_from_db()

        self.assertEqual(product.stock_quantity, 7)

        self.assertEqual(product.product_status, "IN_STOCK")

    def test_update_quantity_B(self):
        product = Product.objects.create(
            name_product="Camisa",
            price=50.00,
            stock_quantity=5,
            sku="CAMISA-02",
            seller=self.seller
        )

        quantity_out = 5

        product.stock_quantity -= quantity_out
        product.save()

        product.refresh_from_db()

        self.assertEqual(product.stock_quantity, 0)
        
        self.assertEqual(product.product_status, "EXHAUSTED")