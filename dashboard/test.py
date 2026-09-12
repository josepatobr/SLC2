from django.test import TestCase
from django.urls import reverse
from stock.models import Product, StockMovement

class ProductTest(TestCase):
    def test_produto_id(self):
        produto_A = Product.objects.create(name_product="produto A", price=10, stock_quantity=5)
        get_produt_id = Product.objects.get(id=produto_A.id)
        self.assertEqual(get_produt_id.name_product, "produto A")

    #test de vendas por id do produto
    def test_vendas_id_produto(self):
        produto_A = Product.objects.create(name_product="produto A", price=10, stock_quantity=10)
        venda_produto_A = StockMovement.objects.create(product=produto_A, quantity_out=10, date_moved="2007-01-22")
        self.assertEqual(venda_produto_A.product.name_product, "produto A")      

