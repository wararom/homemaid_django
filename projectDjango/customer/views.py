from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from customer.forms import *
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
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
@login_required
def success(request):
    return render(request,"success.html")
    
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
    success_url = '/app/viewmaid'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(ReserveMaid,self).form_valid(form)

@login_required
@transaction.atomic
def update_reserve(request,pkmaid):
        # if request.method == 'POST':
            # reserve_form = ReserveForm(request.POST, instance=request.user)
        reserve = Reserve.objects.get(user=request.user)
        idmaid = Maid.objects.get(id=pkmaid)
        reserve.maid_id = idmaid

        if reserve.typearea == 'home' and reserve.size == 'less25':
            cost = 300
        elif reserve.typearea == 'home' and reserve.size == 'between':
            cost = 600
        elif reserve.typearea == 'home' and reserve.size == 'morethan':
            cost = 1200
        elif reserve.typearea == 'condo' and reserve.size == 'less25':
            cost = 500
        elif reserve.typearea == 'condo' and reserve.size == 'between':
            cost = 800
        elif reserve.typearea == 'condo' and reserve.size == 'morethan':
            cost = 1500
        
        reserve.cost = cost
        reserve.save()
        pk = User.objects.get(username = request.user.username)
        temp = Reserve.objects.filter(user_id=pk.id)
        return render(request, 'detail_reserve.html', {'object_list':temp})


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
        return context
    
   
class ListMaidView(LoginRequiredMixin,ListView):
    model = Maid  
    template_name='display_maid.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

@login_required
def	getinfo(request,pk=None):
    pk = User.objects.get(username = request.user.username)
    temp = Reserve.objects.filter(user_id=pk.id)
    return render(request, 'detail_reserve.html', {'object_list':temp})

def signin(request):
	if request.method == 'POST' and 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:	
			if user.is_active:
				if 'remember' in request.POST:
					if request.POST['remember']=='1':
						request.session.set_expiry(604800) #remember keep session for a week
				else:
					request.session.set_expiry(14400) #not remember keep session for 4hrs

				login(request, user)
				request.session['username'] = user.username
				
				return redirect('reserve')
			else:
				msg="Disabled account"
		else:
			msg="Invalid username or password"
		return render(request,'login.html',{'msg': msg})   
	return render(request,'login.html',{'msg': ""})

def signout(request):
	if 'username' in request.session:
		del request.session['username']
	logout(request)
	return redirect('signin')
   

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
        return render(request, 'profile_update.html', {
            'user_form': user_form,
            'profile_form': profile_form})

class SlipView(LoginRequiredMixin,CreateView):
    model = Money
    form_class = UpSlipForm  
    template_name='slip.html'
    success_url = '/app/success'
    def form_valid(self,form):
        form.instance.user=self.request.user
        res = Reserve.objects.get(user=self.request.user)
        form.instance.resever_id=res
        return super(SlipView,self).form_valid(form)