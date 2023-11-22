from django import forms
from .models import Task


class FormsTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "descriptions", "due_data", "status"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'due_data': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de vencimiento'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            # Etiquetas personalizadas
            'title': '', 'descriptions': '', 'due_data': 'Fecha de Vencimiento', 'status': 'Estado'
        }
