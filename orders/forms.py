from django import forms
from .models import Orders
from houses.models import House


class OrderForm(forms.ModelForm):
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Orders
        fields = ["house", "name", "phone"]