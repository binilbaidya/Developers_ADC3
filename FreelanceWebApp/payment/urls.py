from django.urls import path
from . import views

app_name = "payment"
urlpatterns = [
    path('payment/',views.payment,name="payment"),
    path('view-payment',views.view_payments,name="view_payments"),
]
