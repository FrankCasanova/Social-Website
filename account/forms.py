from django import forms


class LoginForm(forms.Form):
    """
    Form that work in order to allow the users log in into the website
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
