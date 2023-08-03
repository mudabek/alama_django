from django import forms


class MonthYearWidget(forms.DateInput):
    input_type = 'month'
    format = '%Y-%m'

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({'placeholder': 'MM-YYYY'})
        super().__init__(attrs=attrs)

class CoursePurchaseForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_holder_first_name = forms.CharField(label='Card Holder First Name', max_length=100)
    card_holder_last_name = forms.CharField(label='Card Holder Last Name', max_length=100)
    expiration_date = forms.DateField(
        label='Expiration Date',
        widget=MonthYearWidget(attrs={'class': 'form-control'}),  # Use the custom MonthYearWidget
        input_formats=['%m-%Y'],  # Specify the allowed date format (year-month)
    )