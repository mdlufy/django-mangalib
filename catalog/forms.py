from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

from django import forms

from .models import Comment

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
            help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cleanedData = self.cleaned_data
        if cleanedData['password'] != cleanedData['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cleanedData['password2']