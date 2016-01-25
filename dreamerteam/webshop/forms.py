from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    ROLE_CHOICES = (
    ('Customer', 'Customer'),
    ('Developer', 'Developer'),)
    group = forms.ChoiceField(choices = ROLE_CHOICES,required = True, label = 'Role')

    class Meta:
        model = User
        #fields = ('username','email', 'password1', 'password2')
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
        return user
