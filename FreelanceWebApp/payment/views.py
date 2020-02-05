from django.shortcuts import render, redirect
from payment.forms import PaymentForm
from django.contrib import messages
from user.models import AppUser
from payment.models import Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def payment(request,id):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_amount = int(payment_form.cleaned_data['payment_amount'])
            funds = AppUser.objects.get(user=request.user).funds or 0
            other_funds = AppUser.objects.get(pk=id).funds or 0
            if funds <  payment_amount:
                messages.success(request,f'Please add funds')
                return redirect('user:add_funds')
            else:
                pay = payment_form.save(commit=False)
                pay.payment_status = True
                pay.user_id = request.user.id
                pay.pay_to_id = id
                pay.save()
                funds = funds - payment_amount
                other_funds = other_funds + payment_amount
                AppUser.objects.filter(pk=id).update(funds=other_funds)
                AppUser.objects.filter(user=request.user).update(funds=funds)
                return redirect('payment:view_payments')
    payment_form = PaymentForm()
    return render(request,"payment/payment.html", {'payment_form':payment_form})

@login_required
def view_payments(request):
    payment = Payment.objects.filter(payment_status__exact=1)
    return render(request,'payment/view_payments.html',{'payment':payment})
