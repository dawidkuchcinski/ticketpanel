from django import forms
from ticketlist.models import Device
from ticketlist.models import Ticket
from ticketlist.models import Devicedamage

class AddDevice(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['ticket']

class AddTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['uzytkownik','firma','status']

class AddDamage(forms.ModelForm):
    class Meta:
        model = Devicedamage
        exclude = ['device','ticket']
        labels = {
            "damagedpart": "Uszkodzona część",
            "damagedescription": "Opis uszkodzenia"
        }

class DeleteDamage(forms.Form):
    damagetodelete = forms.IntegerField(widget=forms.HiddenInput())