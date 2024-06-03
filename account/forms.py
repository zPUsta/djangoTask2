from django import forms

class AnotherForm(forms.Form):
    SEX = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    
    name_surname = forms.CharField(max_length=50, label="Name and Surname")
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=10, min_length=5, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10, min_length=5, label="Confirm Password", widget=forms.PasswordInput)
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect, label="Gender")
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 1920)))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
