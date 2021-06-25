from django.conf import settings
from django.db.models import Model, IntegerField, CharField, ForeignKey, DO_NOTHING, DecimalField, ImageField, \
    ManyToManyField, DateTimeField, BooleanField, SET_NULL, CASCADE, FloatField
from django.shortcuts import reverse
from django_countries.fields import  CountryField


class Fefco(Model):
    fefco_code = IntegerField(primary_key=True)
    description = CharField(max_length=500)

    def __str__(self):
        return f'{self.fefco_code}'

class Layer(Model):
    layer = CharField(max_length=5)
    description = CharField(max_length=128)

    def __str__(self):
        return f'{self.layer}'


class Box(Model):
    name = CharField(max_length=50)
    size = CharField(max_length=20)
    color = CharField(max_length=20)
    layer = ForeignKey(Layer, on_delete=DO_NOTHING)
    fefco = ForeignKey(Fefco, on_delete=DO_NOTHING)
    description = CharField(max_length=500)
    price_a = DecimalField(max_digits=8, decimal_places=2)
    price_n = DecimalField(max_digits=8, decimal_places=2)
    photo = ImageField(upload_to='media')
    quantity = IntegerField()
    discount_price = FloatField(blank=True, null=True)



    def __str__(self):
        return f'{self.name} {self.layer} {self.size} {self.price_a} Kc'

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={
            "pk" : self.pk

        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            "pk" : self.pk
        })


class OrderItem(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=CASCADE)
    ordered = BooleanField(default=False)
    item = ForeignKey(Box, on_delete=CASCADE)
    quantity = IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price_a

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()


class Order(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    items = ManyToManyField(OrderItem)
    start_date = DateTimeField(auto_now_add=True)
    ordered_date = DateTimeField()
    ordered = BooleanField(default=False)
    checkout_address = ForeignKey(
        'CheckoutAddress', on_delete=SET_NULL, blank=True, null=True)
    payment = ForeignKey(
        'Payment', on_delete=SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    street_address = CharField(max_length=100)
    apartment_address = CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Payment(Model):
    stripe_id = CharField(max_length=50)
    user = ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=SET_NULL, blank=True, null=True)
    amount = FloatField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username