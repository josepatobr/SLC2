from django.test import TestCase
from stock.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile


class test_home(TestCase):
    def test_home_view(self):
        imagem_ficticia = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61', 
            content_type='image/jpeg'
        )
        Product.objects.create(name_product="soldado", price=10.0, stock_quantity=5, product_image=imagem_ficticia)

        response = self.client.get('/cassino/home/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "soldado")