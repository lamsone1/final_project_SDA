
from django.db.models import Model, IntegerField, CharField, ForeignKey, DO_NOTHING, DecimalField, ImageField


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



    def __str__(self):
        return f'{self.name} {self.layer} {self.size} {self.price_a} Kc'


