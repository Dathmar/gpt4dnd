from django import forms


class InputForm(forms.Form):
    text = forms.TextInput()
