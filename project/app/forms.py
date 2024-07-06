from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from .models import WordFile

# class LoadForm(forms.ModelForm):
#     file = forms.FileField()


class WordFileForm(forms.ModelForm):
    class Meta:
        model = WordFile
        fields = ('file', )

class WordCountForm(forms.ModelForm):
    # word_count = forms.IntegerField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = WordFile
        fields = ('search_word',)