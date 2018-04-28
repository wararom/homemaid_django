from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ReserveForm, CustomerForm
from .models import Customer, Maid, Reserve, Money
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,"home.html")

# @login_required
def reserve(request):
    return render(request,"reserve.html")

class ReserveMaid(CreateView):
    template_name='reserve.html'
    form_class = ReserveForm
    success_url = '/slip'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(ReserveMaid,self).form_valid(form)

class CustomerRegis(CreateView):
    template_name='register.html'
    form_class = CustomerForm
    success_url = '/home'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(CustomerRegis,self).form_valid(form)
