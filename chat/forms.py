from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control field', 'placeholder':'Email Address'}), )
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control field'
	    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
	    self.fields['username'].label = ''
	    self.fields['username'].help_text = ''

	    self.fields['password1'].widget.attrs['class'] = 'form-control field'
	    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
	    self.fields['password1'].label = ''
	    self.fields['password1'].help_text = ''

	    self.fields['password2'].widget.attrs['class'] = 'form-control field'
	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
	    self.fields['password2'].label = ''
	    self.fields['password2'].help_text = ''

class EditProfileForm(UserChangeForm):
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'', 'placeholder':'Last Name'}))
	bio = forms.CharField(label="", max_length=100,widget=forms.Textarea(attrs={'class':'', 'placeholder':'Add Bio'}) )
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','bio' ,)

	def __init__(self, *args, **kwargs):
	    super(EditProfileForm, self).__init__(*args, **kwargs)

	    self.fields['email'].widget.attrs['class'] = 'user_inp'
	    self.fields['email'].widget.attrs['placeholder'] = ''
	    self.fields['email'].label = ''
	    self.fields['email'].help_text = ''
