from django import forms
from .models import Order, Item, Comment, Address


class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('seller', 'customer', 'designer', 'status',)

        widgets = {
            'seller': forms.Select(attrs={'class': 'custom-selector'}),
            'customer': forms.TextInput(attrs={'class': 'custom-selector'}),
            'designer': forms.Select(attrs={'class': 'custom-selector'}),
            'status': forms.Select(attrs={'class': 'custom-selector'}),
        }


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'order', 'name', 'material', 'thickness', 'color', 'dimensions', 'width', 'height', 'depth', 'fastening',
            'hole', 'rounding', 'mark', 'quantity', 'description', 'actions')

        widgets = {
            'order': forms.HiddenInput(),
            'name': forms.Select(attrs={'class': 'custom-selector'}),
            'material': forms.Select(attrs={'class': 'custom-selector'}),
            'thickness': forms.Select(attrs={'class': 'custom-selector'}),
            'color': forms.Select(attrs={'class': 'custom-selector'}),
            'dimensions': forms.Select(attrs={'class': 'custom-selector'}),
            'width': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'height': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'depth': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'fastening': forms.Select(attrs={'class': 'custom-selector'}),
            'hole': forms.TextInput(attrs={'class': 'custom-selector'}),
            'rounding': forms.TextInput(attrs={'class': 'custom-selector'}),
            'mark': forms.Select(attrs={'class': 'custom-selector'}),
            'quantity': forms.NumberInput(attrs={'class': 'custom-selector'}),
            'description': forms.Textarea(attrs={'class': 'custom-selector'}),
            'actions': forms.SelectMultiple(attrs={'class': 'custom-selector'}),
        }


class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('order', 'message')

        widgets = {
            'order': forms.HiddenInput(),
            'message': forms.Textarea(attrs={'class': 'custom-selector'}),
        }


class SearchForm(forms.Form):
    customer = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-selector'}))
    # klient = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-selector'}))


class AddressAddForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'order', 'customer', 'street', 'zip_code', 'city', 'shipment_date', 'shipment_comment', 'phone_number')

        widgets = {
            'order': forms.HiddenInput(),
            'customer': forms.TextInput(attrs={'class': 'custom-selector'}),
            'street': forms.TextInput(attrs={'class': 'custom-selector'}),
            'zip_code': forms.TextInput(attrs={'class': 'custom-selector'}),
            'city': forms.TextInput(attrs={'class': 'custom-selector'}),
            'shipment_date': forms.DateInput(attrs={'class': 'custom-selector'}),
            'shipment_comment': forms.Textarea(attrs={'class': 'custom-selector'}),
            'phone_number': forms.TextInput(attrs={'class': 'custom-selector'}),
        }
