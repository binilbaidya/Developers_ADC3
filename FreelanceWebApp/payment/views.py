from django.shortcuts import render, redirect
from payment.forms import PaymentForm
from django.http import HttpResponse

# Create your views here.

def payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        # print(request.user.id)
        if payment_form.is_valid():
            pay = payment_form.save(commit=False)
            pay.payment_status = True
            pay.user_id = request.user.id
            pay.save()
            return redirect('project:project')
    payment_form = PaymentForm()
    return render(request,"payment/payment.html", {'payment_form':payment_form})

