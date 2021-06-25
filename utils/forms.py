from django.forms import ModelForm, CharField, IntegerField, Form, forms, DateField, FloatField, ModelChoiceField, \
    ImageField, TextInput, BooleanField, RadioSelect, ChoiceField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from utils.models import Box, Fefco, Layer

PAYMENT = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class BoxModelForm(ModelForm):
    class Meta:
        model = Box
        fields = '__all__'




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class StockModelForm(ModelForm):
    class Meta:
        model = Box
        fields = ('quantity',)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class FefcoModelForm(ModelForm):
    class Meta:
        model = Fefco
        fields = '__all__'




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LayerModelForm(ModelForm):
    class Meta:
        model = Layer
        fields = '__all__'




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CheckoutForm(Form):
    street_address = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234 Main St'
    }))

    apartment_address = CharField(required=False, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apartment or suite'
    }))

    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))

    zip = CharField(widget=TextInput(attrs={
        'class': 'form-control'
    }))

    same_billing_address = BooleanField(required=False)
    save_info = BooleanField(required=False)
    payment_option = ChoiceField(
        widget=RadioSelect, choices=PAYMENT)

class ItemModelForm(ModelForm):
    class Meta:
        model = Box
        fields = '__all__'

    name = CharField(max_length=50)
    size = CharField(max_length=20)
    color = CharField(max_length=20)
    layer = ModelChoiceField(queryset=Layer.objects)
    fefco = ModelChoiceField(queryset=Fefco.objects)
    photo = ImageField()
    price_n = FloatField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'