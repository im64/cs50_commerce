from django import forms


class AddAuction(forms.Form):
    name = forms.CharField(label="Item name", max_length=120)
    description = forms.CharField(label="Item description", widget=forms.Textarea)
    price = forms.DecimalField(label="Starting Price")
    photo = forms.ImageField()


