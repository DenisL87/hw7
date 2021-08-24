from math import sqrt

from django import forms

class TriangleForm(forms.Form):
    leg_a = forms.IntegerField(label='Cathetus a', min_value=1)
    leg_b = forms.IntegerField(label='Cathetus b', min_value=1)
    hypotenuse = forms.IntegerField(label='Hypotenuse', required=False)