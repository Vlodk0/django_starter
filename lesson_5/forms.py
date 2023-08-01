from django import forms
from durationwidget.widgets import TimeDurationWidget
from lesson_4.models import Client


class MyForm(forms.Form):
    name = forms.CharField(label="User name", initial="User name", error_messages={'required': 'PLease enter your '
                                                                                               'available email'})
    profile_picture = forms.ImageField(widget=forms.FileInput)
    additional_form = forms.FileField(widget=forms.FileInput)
    email = forms.EmailField(initial="admin@admin.com", error_messages={'required': 'Please enter your '
                                                                                    'available email'})
    password = forms.CharField(max_length=20, min_length=10, widget=forms.PasswordInput(), required=False)
    age = forms.IntegerField(required=False, help_text="Enter your current age", initial="20")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    birthday = forms.DateField(widget=forms.SelectDateWidget)
    work_experience = forms.DurationField(widget=TimeDurationWidget)
    gender = forms.ChoiceField(choices=[("1", "man"), ("2", "woman")])


# class FormFromModel(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ['user', 'second_email']
