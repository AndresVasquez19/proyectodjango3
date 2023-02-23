from django import forms
from . models import tarea

class TareaForm (forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    class Meta: 
        model = tarea
        fields = ['titulo', 'descripcion', 'estado']