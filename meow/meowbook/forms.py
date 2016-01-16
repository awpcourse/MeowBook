from django.forms import Form, CharField, Textarea, PasswordInput


class CatStatusForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'placeholder': "Tell us how you feel..."}))

class SearchBarForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 1, 'cols': 30, 'placeholder': 'Search ...'}),
        label='')


class LoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)
