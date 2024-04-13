import re

from django import forms

from catalog.models import Product, Version

exclude_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for data_word in exclude_words:
            if re.search(data_word, cleaned_data.lower(), flags=re.S) is not None:
                raise forms.ValidationError(f'Название товара содержит запрещенное слово - {data_word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for data_word in exclude_words:
            if re.search(data_word, cleaned_data.lower(), flags=re.S) is not None:
                raise forms.ValidationError(f'Описание товара содержит запрещенное слово - {data_word}')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
