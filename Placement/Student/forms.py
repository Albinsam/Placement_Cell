
import re
from django import forms
from .models import Student
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from .models import Student

class LoginForm(forms.Form):
    username = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Check if the user exists
        try:
            user = Student.objects.get(email=email)
        except Student.DoesNotExist:
            raise forms.ValidationError('Invalid email or password.')

        # Verify the password
        if not check_password(password, user.password):
            raise forms.ValidationError('Invalid email or password.')

        # Store user in cleaned_data so we can use it in the view
        cleaned_data['user'] = user
        return cleaned_data



  

class RegistrationForm(forms.ModelForm):
     confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

     class Meta:
        model = Student
        fields = ['full_name', 'age', 'email', 'department', 'skills', 'phone_number', 'password', 'confirm_password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department'}),
            'skills': forms.TextInput(attrs={'placeholder': 'Skills'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
    # Cross-field validation for password match
     def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Ensure passwords match
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data

    # Phone number validation
     def clean_phone_number(self):
       phone_number = self.cleaned_data.get('phone_number')
    
    # Check for empty field
       if not phone_number:
        raise ValidationError("Phone number cannot be empty.")

    # Ensure the phone number contains only digits and has exactly 10 digits
       if not phone_number.isdigit() or len(phone_number) != 10:
        raise ValidationError("Phone number must be exactly 10 digits long.")
    
       return phone_number


     def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        # Ensure the full name does not contain any numbers
        if re.search(r'\d', full_name):
            raise ValidationError("Full name cannot contain numbers.")
        
        return full_name
    # Email validation
     def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if email is already registered
        if Student.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        
        return email

     def save(self, commit=True):
        student = super().save(commit=False)
        # Hash the password before saving
        student.password = make_password(self.cleaned_data["password"])
        if commit:
            student.save()
        return student