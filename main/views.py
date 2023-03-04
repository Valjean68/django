from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import createnewlist
# Create your views here.

def index(response,id):
	ls=ToDoList.objects.get(id=id)
	if ls in response.user.todolist.all():
		if response.method=='POST':


			if response.POST.get('save'):
				for item in ls.item_set.all():
					if response.POST.get('c'+str(item.id))=='clicked':
						item.complete=True
					else:
						item.complete=False
					item.save()


			elif response.POST.get('newitem'):
				txt=response.POST.get('new')
				if len(txt)>2:
					ls.item_set.create(text=txt,complete=False)
				else:
					print('invalid')
		return render(response,'main/list.html',{'ls':ls})
	return render(response,'main/view.html',{})
def v1(response):
	return HttpResponse('<h1 style="color:darkgoldenrod;font-family:sans-serif;"><a href="/" style="text-decoration:none;color:inherit;">activate dj</a></h1>')

def home(response):
	return render(response,'main/home.html')

def create(response):
	if response.method=='POST':
		form=createnewlist(response.POST)
		if form.is_valid():
			n=form.cleaned_data['name']
			t=ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)
		return HttpResponseRedirect('/%i' %t.id)

	else:
		form=createnewlist()
	return render(response,'main/create.html',{'form':form})

def view(response):
	return render(response,'main/view.html',{})