from django.forms import ModelForm, CharField, IntegerField

from utils.models import Box, Fefco


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