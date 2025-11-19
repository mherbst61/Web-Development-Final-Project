from django import forms

from TicketFinder.models import Search


class ticketSearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
        widgets = {
            'genre':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Type to search by genre',
                'list': 'datalistOptions'
        }),
            'city':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter a city e.g., Hartford',
            })

        }
