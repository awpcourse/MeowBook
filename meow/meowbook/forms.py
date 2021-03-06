from django.forms import Form, CharField, ImageField, Textarea, PasswordInput, FileField


class CatStatusForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'placeholder': "Tell us how you feel...", 'class': "form-control"}),
        label='')


class SearchBarForm(Form):
    search_text = CharField(widget=Textarea(
        attrs={'rows': 1, 'cols': 30, 'placeholder': 'Search ...'}),
        label='')


class LoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class StatusCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'placeholder': "MEEOOOWW..."}),
        label='')


class PhotoCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 2, 'class': 'form-control', 'placeholder': "MEEOOOWW THIS PHOTO..."}),
        label='')



class AddPicForm(Form):
    pic = ImageField(label='Choose a picture', required=False)
    desc = CharField(widget=Textarea(
        attrs={'rows': 1, 'placeholder': "Description", 'class': "form-control"}),
        label='Now say something about it!')
