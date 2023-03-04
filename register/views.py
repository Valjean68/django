from django.shortcuts import render,redirect
from .forms import registerform
# Create your views here.

def register(response):
	if response.method=="POST":
		form=registerform(response.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form=registerform()
	form=registerform()
	return render(response,'register/register.html',{'form':form})