from django.contrib.auth import login, authenticate
from .forms import DoanhNghiepForm
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import  View
from django.urls import reverse
def signup(request):
    if request.method == 'POST':
        form = DoanhNghiepForm(request.POST)
        print('form post ne',form)
        tenDN=form.cleaned_data['matinhthanh']
        print('tenDN',tenDN)
        if form.is_valid():
            form.save()
            return HttpResponse('oke')
        else:
            return HttpResponse('khong validate')
    else:
        form = DoanhNghiepForm()
        print('form ne',form)
    return render(request, 'website/register.html', {'form': form})
class signin(View):
    def get(self,request):
        return render(request,'website/sign-in.html')
    def post(self,request):
        name=request.POST.get('userName')
        matkhau=request.POST.get('password')
        userName=authenticate(username=name,password=matkhau)
        print(userName,matkhau)
        if userName is None:
            return HttpResponse('not exist')
        login(request,userName)
        return HttpResponseRedirect(reverse("website:count-history"))

