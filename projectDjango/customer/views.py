from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ReserveForm, CustomerForm, UserForm, SignUpForm, ProfileForm
from .models import Customer, Maid, Reserve, Money
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect ,render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.views import generic
from django.db.models import signals
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages


# Create your views here.
@login_required
def homepage(request):
    return render(request,"home.html")
def slip(request):
    return render(request,"slip.html")

def viewmaidchoose(request, pk=None):
    return None


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
    success_url = '/app/slip'
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
    template_name='detail_reserve.html'
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context
    
   
class ListMaidView(LoginRequiredMixin,ListView):
    model = Maid  
    template_name='display_maid.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


@login_required
@transaction.atomic
def update_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, instance=request.user.customer)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return redirect('reserve')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.customer)
        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form})