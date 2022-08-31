from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.widgets.EmailInput)

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password",
        min_length=8
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password confirmation",
        min_length=8
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'password1', 'password2']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data

    def save(self, commit=True):
        profile = super(CustomUserRegistrationForm, self).save(commit=False)
        profile.set_password(self.cleaned_data['password1'])
        if commit:
            profile.save()
        return profile


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    class Meta:
        fields = ['email', 'password']
