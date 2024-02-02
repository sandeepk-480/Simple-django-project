from django import forms
from app.models import Student
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    roll = forms.IntegerField(required=True)
    class Meta:
        model = Student
        fields = '__all__'

    
    def clean(self):
        cleaned_data = super().clean()
        roll_number = cleaned_data.get('roll')

        if roll_number <= 0:
            raise ValidationError("Roll number must be a positive integer.")