from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import City, Location, Room


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["city", "location", "house_number", "floor", "price", "image1", "image2", "image3", "water", "internet", "parking","description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = "Select City"
        self.fields['location'].empty_label = "Select Location"
        self.fields['location'].queryset = Location.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['location'].queryset = Location.objects.filter(city_id=city_id).order_by('location')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['location'].queryset = self.instance.city.location_set
            # .order_by('name')

class EditForm(forms.ModelForm):
    status = forms.ModelChoiceField()
    class Meta:
        model = Room
        fields = ["city", "location", "house_number", "floor", "price", "image1", "image2", "image3", "water", "internet", "parking","description"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['image1'].queryset = Room.objects.none()
    #     self.fields['image2'].queryset = Room.objects.none()
    #     self.fields['image3'].queryset = Room.objects.none()

    #     if 'city' in self.data:
    #         try:
    #             city_id = int(self.data.get('city'))
    #             self.fields['location'].queryset = Location.objects.filter(city_id=city_id).order_by('location')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['location'].queryset = self.instance.city.location_set
    #         # .order_by('name')