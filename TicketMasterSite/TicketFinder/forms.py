from random import choices

from django import forms

from TicketFinder.models import Search, save_Ticket


class ticketSearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
        widgets = {
            'state':forms.Select(attrs={
                    'class':'form-control',
            }),
            'genre':forms.TextInput(attrs={
                'class':'form-control w-25',
                'placeholder':'Type to search by genre',
                'list': 'datalistOptions'
        }),
            'city':forms.TextInput(attrs={
                'class':'form-control w-25',
                'placeholder':'Enter a city e.g., Hartford',
            })

        }
