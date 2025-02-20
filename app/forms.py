from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Case, Payment, CaseQuestionnaire

class UserRegistrationForm(UserCreationForm):
    is_lawyer = forms.BooleanField(
        required=False, 
        label='Register as Lawyer',
        help_text='Check this if you want to register as a lawyer',
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
        })
    )
    phone_number = forms.CharField(
        max_length=15, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter your phone number'
        })
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3, 
            'placeholder': 'Enter your address',
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
        }), 
        required=False
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter your email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_lawyer', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize help texts to be more concise
        self.fields['username'].help_text = 'Required. 150 characters or fewer.'
        self.fields['password1'].help_text = 'At least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before.'
        
        # Add styling and placeholders to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.PasswordInput, forms.EmailInput)):
                field.widget.attrs.update({
                    'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
                })

    def save(self, commit=True):
        user = super().save(commit=True)
        profile = user.userprofile
        profile.is_lawyer = self.cleaned_data.get('is_lawyer', False)
        profile.phone_number = self.cleaned_data.get('phone_number', '')
        profile.address = self.cleaned_data.get('address', '')
        if commit:
            profile.save()
        return user 

class CaseQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = CaseQuestionnaire
        exclude = ['case', 'created_at']
        widgets = {
            'incident_date': forms.DateInput(attrs={'type': 'date'}),
            'incident_description': forms.Textarea(attrs={'rows': 4}),
            'witnesses': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Name: \nAddress: \nContact: \n\nAdd multiple witnesses in the same format'}),
            'defendant_address': forms.Textarea(attrs={'rows': 3}),
            'client_address': forms.Textarea(attrs={'rows': 3}),
            'previous_legal_actions': forms.Textarea(attrs={'rows': 3}),
            'desired_outcome': forms.Textarea(attrs={'rows': 3}),
            'additional_info': forms.Textarea(attrs={'rows': 3}),
        }

class CaseForm(forms.ModelForm):
    preferred_lawyer = forms.ModelChoiceField(
        queryset=User.objects.filter(userprofile__is_lawyer=True),
        required=False,
        empty_label="Select a preferred lawyer (optional)",
        help_text="You can select a specific lawyer to handle your case, or leave it empty to have one assigned."
    )

    class Meta:
        model = Case
        fields = ['title', 'description', 'category', 'preferred_lawyer']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount'] 

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add styling to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            })
            
        # Add placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password' 