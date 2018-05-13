from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import MaidForm,ImageUploadForm
from .models import Maid
from django.contrib.auth.decorators import login_required


class MaidRegister(CreateView):
    template_name='registerM.html'
    form_class = MaidForm
    success_url = 'profilemaid/'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(MaidRegister,self).form_valid(form)

def	getAllinfo(request):
	info = Maid.objects.all()
	return render(request, 'profileMaid.html', {'object_list':info})
