from django import forms
from .models import Apointment


class ApointmentForm(forms.ModelForm):
	class Meta:
		model = Apointment
		fields = '__all__'