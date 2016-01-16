from django.forms import Form, CharField, Textarea


class CatStatusForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'placeholder': "Tell us how you feel..."}),
from django.forms import Form, CharField, Textarea, PasswordInput


class SearchBarForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 1, 'cols': 30, 'placeholder': 'Search ...'}),
        label='')