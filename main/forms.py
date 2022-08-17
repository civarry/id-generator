from cProfile import label
from django import forms
from .models import *
from .widgets import DatePickerInput

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('first_name','last_name', 'image','gender', 'date_of_birth', 'civil_status', 'blood_type', 'validity' ,'motto')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control neu'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control neu'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control neu'}),
            'date_of_birth' : DatePickerInput(),
            'civil_status': forms.Select(attrs={'class': 'form-control neu'}),
            'blood_type': forms.Select(attrs={'class': 'form-control neu'}),
            'motto': forms.Textarea(attrs={'class': 'form-control neu1'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        uneditable_fields = ['validity']
        for field in uneditable_fields:
            self.fields[field].widget.attrs['readonly'] = 'true'   