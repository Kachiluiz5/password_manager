from django import forms
from .models import Password

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['name', 'length']

    def clean_length(self):
        length = self.cleaned_data.get('length')
        if length < 6:
            raise forms.ValidationError("Password length should be at least 6 characters.")
        return length
    
class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['name', 'value']
