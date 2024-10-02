from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# Customized Registration Form
class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(max_length=10,required=True, label='Phone Number')
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    address_line_1 = forms.CharField(max_length=100, required=True)
    address_line_2 = forms.CharField(max_length=100, required=False)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name' , 'email' ,'phone_no', 'dob', 'address_line_1', 'address_line_2','password1', 'password2']

    def save(self, commit=True):
        # Override the save method to handle custom fields correctly
        
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_no = self.cleaned_data['phone_no']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address_line_1 = self.cleaned_data['address_line_1']    
        user.address_line_2 = self.cleaned_data.get('address_line_1', '')
        user.dob = self.cleaned_data['dob']   
        
        if commit:
            user.save()
        
        return user            
    
# Customized Login Form
class UserLoginForm(AuthenticationForm):
    phone_no = forms.CharField(max_length=10, required=True, label='Phone Number')
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        fields = ['phone_no', 'password']