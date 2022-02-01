from django.shortcuts import render
from blog.forms import ContactForm



def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def elements(request):
    return render(request,'elements.html')

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm()
    return render(request,'contact.html',{'form':form})

def maintenance(request):
    return render(request,'maintenance.html')