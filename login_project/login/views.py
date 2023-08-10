from django.shortcuts import render,redirect

# Create your views here.
from.models import Login
from.forms import LoginForm

from login import views

def showlogin(request):
    show = Login.objects.all()
    context = {
        'show':show
        }
    return render(request,'show.html', context)



def Creating(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')

    context = {
        'form': form
    }
    return render(request, 'creating.html', context)


def Edit(request,pk):
    login=Login.objects.get(id=pk)
    form=LoginForm(instance=login)
    if request.method=='POST':
        form=LoginForm(request.POST,request.FILES,instance=login)
        if form.is_valid():
            form.save()
            return redirect('show')
    context={
        'form':form
    }
    return render(request,'Editing.html',context)

def Delete(request,pk):
    det=Login.objects.get(id=pk)
    det.delete() 
    return redirect('show')