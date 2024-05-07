from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages  # new
from django.urls import reverse  # new
from .forms import ContactForm #new
from .bot import send_message
from .models import Contact,Article,Trainer,Jamoa

def index_view(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"index.html",context)


def about_view(request):
    articles = Jamoa.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"about.html",context)


def blog_view(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"blog.html",context)


def blogg_view(request):
    return render(request,"blog.html")


def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]

            send_message(name,email,phone_number,description)
            form.save()
            form = ContactForm()
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...') 
            return HttpResponseRedirect(reverse('index-page'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
             
    context = {"form":form}

    return render(request, "contact.html",context)


def portfolio_view(request):
    return render(request,"portfolio.html")

