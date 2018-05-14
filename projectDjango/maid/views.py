from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import MaidForm,SignUpMaidForm,MaidProfileForm,UserForm
from .models import Maid
from customer.models import Reserve
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class SignUpMaid(CreateView):
    form_class = SignUpMaidForm
    success_url = '/maid/signin'
    template_name = 'signupmaid.html'

class MaidRegister(LoginRequiredMixin,CreateView):
    template_name='registerM.html'
    form_class = MaidForm
    success_url = '/maid/profilemaid'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(MaidRegister,self).form_valid(form)
        
# @login_required
# def	getAllinfo(request):
#     temp = User.objects.get(username = request.user.username)
#     info = Reserve.objects.filter(maid_id=temp.id)
#     return render(request, 'profileMaid.html', {'object_list':info})

@login_required
def	getinfomaid(request,pk=None):
    t = User.objects.get(username = request.user.username)
    pk = Maid.objects.get(user_id = t.id)
    temp = Reserve.objects.filter(maid_id=pk.id)
    return render(request, 'profileMaid.html', {'object_list':temp})

def signin(request):
	if request.method == 'POST' and 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:	
			if user.is_active:
				if 'remember' in request.POST:
					if request.POST['remember']=='1':
						request.session.set_expiry(604800)
				else:
					request.session.set_expiry(14400) 
				login(request, user)
				request.session['username'] = user.username
				return redirect('/maid/profilemaid')
			else:
				msg="Disabled account"
		else:
			msg="Invalid username or password"
		return render(request,'loginmaid.html',{'msg': msg})   
	return render(request,'loginmaid.html',{'msg': ""})

def signout(request):
	if 'username' in request.session:
		del request.session['username']
	logout(request)
	return redirect('signinmaid')

@login_required
@transaction.atomic
def update_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = MaidProfileForm(request.POST,instance=request.user.maid)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return redirect('profilemaid')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = MaidProfileForm(instance=request.user.maid)
        return render(request, 'updateprofile.html', {
            'user_form': user_form,
            'profile_form': profile_form})

