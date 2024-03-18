from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth import (authenticate, get_user_model,
                                 password_validation)
from django.contrib.auth.forms import (UserChangeForm, UserCreationForm,
                                       UsernameField)
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Blog


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Sign Up',
             
            ),
            Field('username','password1','password2', css_class="mb-3", css_id="custom_field_id",),
     
            
            Submit('submit', 'Submit', css_class='btn btn-info mt-3'),
           
        )

class Add_Blog(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('title','description')

class EditUserPrifoleForm(UserChangeForm):
    
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        labels={'email':'Email'}

class AdminUserPrifoleForm(UserChangeForm):
    
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}