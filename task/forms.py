from django import forms


class Name(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField()


class Hleb(forms.Form):
    description = forms.CharField()
    button = forms.CharField()
    img = forms.FileField()

class Proba(forms.Form):
    o = forms.TextInput()

