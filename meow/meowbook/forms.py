from django.forms import Form, CharField, Textarea


class CatStatusForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'placeholder': "Tell us how you feel..."}),
        label='')