from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'firstname',
            'lastname',
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname  = self.cleaned_data['lastname']
        user.username  = self.cleaned_data['username']
        user.email   = self.cleaned_data['email']

        if commit:
            user.save()
            return user
