from django.db import models
from config.g_model import TimeStampMixin
from django.utils.timezone import now

# Create your models here.
class Variant(TimeStampMixin):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)


class Product(TimeStampMixin):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    variant1 = models.CharField(max_length=255,default=None,null=True,blank=True)
    variant2 = models.CharField(max_length=255,default=None,null=True,blank=True)
    variant3 = models.CharField(max_length=255,default=None,null=True,blank=True)
    variant4 = models.CharField(max_length=255,default=None,null=True,blank=True)
    price1 = models.FloatField(max_length=255,default=None,null=True,blank=True)
    price2 = models.FloatField(max_length=255,default=None,null=True,blank=True)
    price3 = models.FloatField(max_length=255,default=None,null=True,blank=True)
    price4 = models.FloatField(max_length=255,default=None,null=True,blank=True)
    instoke1 = models.CharField(max_length=255,default=None,null=True,blank=True)
    instoke2 = models.CharField(max_length=255,default=None,null=True,blank=True)
    instoke3 = models.CharField(max_length=255,default=None,null=True,blank=True)
    instoke4 = models.CharField(max_length=255,default=None,null=True,blank=True)

    created_at=models.DateTimeField(default=now)
    updated_at=models.DateTimeField(auto_now_add=True)


class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()


class ProductVariant(TimeStampMixin):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVariantPrice(TimeStampMixin):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
