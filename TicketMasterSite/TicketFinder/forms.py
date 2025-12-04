from random import choices

from django import forms

from TicketFinder.models import Search, SavedTickets, Notes


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
class createNewNoteForm (forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
        'title':forms.TextInput(attrs={
        'class' :'form-control',
        'placeholder':'Enter title for note',
        'id':'titleArea'
            }),
        'note':forms.Textarea(attrs={
        'rows':'20',
        'id': 'noteArea',
        'class': 'form-control',
        'placeholder':'Enter your note'
        }),
        'ticket_id':forms.NumberInput(attrs={
            'class':'form-control',
            'id':'ticketIdForm',
            'hidden':'true'
        })
        }