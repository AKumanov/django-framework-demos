from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Add title..',
                    'autofocus': True,
                }

            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Add description',
                    'rows': 5,
                }
            ),
            'urgency': forms.Select(
                attrs={
                    'required': True,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TodoCreateForm(TodoForm):
    pass


class TodoUpdateForm(TodoForm):
    pass
