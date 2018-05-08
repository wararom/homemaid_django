from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ReserveForm, CustomerForm, UserForm, SignUpForm
from .models import Customer, Maid, Reserve, Money
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect ,render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.views import generic
from django.db.models import signals
from django.contrib.auth.models import User
# Create your views here.
@login_required
def homepage(request):
    return render(request,"home.html")

@login_required
def regis(request):
    return render(request,"register.html")

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = '/auth/signin'
    template_name = 'signup.html'
    
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class ReserveMaid(LoginRequiredMixin,CreateView):
    template_name='reserve.html'
    form_class = ReserveForm
    success_url = '/app/home'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(ReserveMaid,self).form_valid(form)

class CustomerRegis(LoginRequiredMixin,CreateView):
    template_name='register.html'
    form_class = CustomerForm
    success_url = '/app/reserve'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(CustomerRegis,self).form_valid(form)

class CustomerProfile(DetailView):
    model = Customer
    # template_name=''
    # def book_detail_view(self,request,pk):
   
class ListMaidView(LoginRequiredMixin,ListView):
    model = Maid  
    template_name='register1.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


        