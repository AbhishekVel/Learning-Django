from django import forms

from .models import RestaurantLocation
#
# class RestaurantCreateForm(forms.Form):
#     name            = forms.CharField(max_length=120)
#     location        = forms.CharField(required=False)
#     category        = forms.CharField(required=False)
#
#     # this is called by django api when you do form.is_valid()
#     def clean_name(self):
#         name = self.cleaned_data.get("name")
#         if name == "Hello":
#             raise forms.ValidationError("Not a valid name")
#         return name

class RestaurantLocationCreateForm(forms.ModelForm):

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'
        ]

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if name == "Hello":
    #         raise forms.ValidationError("Not a valid name")
    #     return name
