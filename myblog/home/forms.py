from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit,Field
from django import forms
from django.contrib.auth import (authenticate, get_user_model,
                                 password_validation)
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class Sign_Up(UserCreationForm):

    username=UsernameField()
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    name=forms.CharField(max_length=55)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Sign Up',
                'username',
                'password1',
                'password2',  
            ),
            Field('username', css_class="mt-3"),
            Submit('submit', 'Submit', css_class='button white mt-3'),
           
        )