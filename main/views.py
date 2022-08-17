from django.shortcuts import render, redirect
from .models import UserInfo
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'main/base.html', {})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/identification')
    else:
        form = UserForm()
    return render(request, 'main/forms.html', {'form' : form})

def identification(request):
    data = UserInfo.objects.all().order_by('-id').values()
    return render(request, 'main/id.html', {'data': data})

def delete(request, id):
    data = UserInfo.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('identification'))
    
def success(request):
    return HttpResponse('successfully uploaded')
