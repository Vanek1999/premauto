from django import forms
 
class UserForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput())
    number = forms.CharField(max_length = 15)
    name = forms.CharField(max_length = 10)

class Cart(forms.Form):
    product_title = forms.CharField(max_length = 200)
    product_description = forms.CharField(max_length = 2000)
    product_price = forms.CharField(max_length = 200)
