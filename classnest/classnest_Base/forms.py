# classnest_Base/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile

# classnest_Base/forms.py

from django import forms
from classnest_Base.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']  # Add any other fields you need

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # Include email if needed
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact', 'github', 'linkedin']
# Use Django's built-in PasswordChangeForm

class PasswordResetForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm New Password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")