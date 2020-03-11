from  django import forms
from .models import OrderPre

class OrderPreForm (forms.Form):
    kind_board = forms.CharField()
    thikness  = forms.FloatField()
    lenght = forms.IntegerField()
    widht = forms.IntegerField()
    quantity = forms.IntegerField()

    def save(self):
        new_pre_order = OrderPre.objects.create(
            kind_board=self.cleaned_data['kind_board'],
            thikness=self.cleaned_data['thikness'],
            lenght=self.changed_data['lenght'],
            widht=self.cleaned_data['widht'],
            quantity=self.cleaned_data['quantity']
        )
        return new_pre_order



