from django import forms
from payment.models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['project','payment_amount','payment_details']

