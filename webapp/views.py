from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Contact, Blog, Comments
from webapp.form import Comment

def index(request):
   return render(request, 'webapp/home.html')


def contact(request):
   return render(request, 'webapp/contact.html')


def send(request):
   new = Contact()
   if request.method == 'POST':
      name = request.POST.get('name')
      mail = request.POST.get('mail')
      message =request.POST.get('message')
      if name == '' or mail == '' or message == '':
         return render(request, 'webapp/contact.html', {"error":"* All fields required"})
      new.name = name
      new.mail_id = mail
      new.message = message
      new.save()
   return render(request, 'webapp/contact.html')

def blog(request):
   blog = Blog.objects.all()
   return render(request,'webapp/blog.html', {'blog':blog})

def detail(request,number):
   post = get_object_or_404(Blog,pk=number)
   form = Comment()
   return render(request,'webapp/details.html',{'post':post,'form':form,})

'''def comment(request, number):
   post = get_object_or_404(Blog,pk=number)
   new = Comments()
   if request.method == 'POST':
      form = Comment(data=request.POST )
      if form.is_valid():
         
         name = request.POST.get('name')
         content = request.POST.get('content')

         new.post = post
         new.name = name
         new.comment = content
         new.save()
         return redirect('detail')
   return render(request,'webapp/details.html',{'post':post,"form":form})'''
def comment(request, number):
   post = get_object_or_404(Blog,pk=number)
   new = Comments()
   form = Comment(data=request.POST )
   if request.method == 'POST':
      
      name = request.POST.get('name')
      content = request.POST.get('content')
      if name == '' or content == '':
         return render(request,'webapp/details.html',{'post':post,"form":form,"error":"*fields required"})

      new.post = post
      new.name = name
      new.comment = content
      new.save()
      
   return render(request,'webapp/details.html',{'post':post,"form":form})
