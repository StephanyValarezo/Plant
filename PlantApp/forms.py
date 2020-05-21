from django import forms

class FormularioEstado(forms.Form):

    estado=forms.BooleanField(required=False)