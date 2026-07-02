from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['icon_class'].required = False
        self.fields['accent'].required = False
        self.fields['border'].required = False

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'steps',
            'icon_class',
            'accent',
            'border',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'steps': forms.Textarea(attrs={'rows': 7}),
        }

    def clean_icon_class(self):
        return self.cleaned_data.get('icon_class') or 'fa-solid fa-cookie'

    def clean_accent(self):
        return self.cleaned_data.get('accent') or '#8f4c6c'

    def clean_border(self):
        return self.cleaned_data.get('border') or '#5c2f3e'
