from django.shortcuts import render, redirect
from payment.forms import PaymentForm
from django.contrib import messages
from user.models import AppUser

# Create your views here.

def payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        # print(request.user.id)
        if payment_form.is_valid():
            payment_amount = payment_form.cleaned_data['payment_amount']
            funds = AppUser.objects.get(user=request.user).funds
            if funds <  payment_amount:
                messages.success(request,f'Please add funds')
                return redirect('user:add_funds')
            else:
                pay = payment_form.save(commit=False)
                pay.payment_status = True
                pay.user_id = request.user.id
                pay.save()
                funds = funds - payment_amount
                AppUser.objects.filter(user=request.user).update(funds=funds)
                return redirect('user:view_profile')
    payment_form = PaymentForm()
    return render(request,"payment/payment.html", {'payment_form':payment_form})

