from django import forms
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet

from .models import Reviews


class SizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].required = True


class ColorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].required = True


class SizeInlineFormSet(BaseInlineFormSet):
    """
    Fills in the default sizes in the admin
    """

    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [
            {'size': 12, 'available': False},
            {'size': 13, 'available': False},
            {'size': 14, 'available': False},
            {'size': 15, 'available': False},
            {'size': 16, 'available': False},
            {'size': 17, 'available': False},
            {'size': 18, 'available': False}
        ]
        super(SizeInlineFormSet, self).__init__(*args, **kwargs)


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating', 'text')
