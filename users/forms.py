from django import forms
from .models import User


class DateInput(forms.DateInput):
    """ Sirve para mostrar el date picker en el template """
    input_type = 'date'


class UserForm(forms.ModelForm):
    """ Formulario de edición de datos de usuario """
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'pais',
            'fecha_de_nacimiento',
            'biografia',
            'intereses',
            'avatar']
        widgets = {
            'fecha_de_nacimiento': DateInput(),
        }
