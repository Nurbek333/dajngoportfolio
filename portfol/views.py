from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages  # new
from django.urls import reverse  # new
from .forms import ContactForm #new
from .bot import send_message
from .models import Contact,Article,Jamoa,Comment,Port
from .forms import ArticleForm, CommentForm


def index_view(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"index.html",context)


def about_view(request):
    articles = Jamoa.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"about.html",context)


def blog_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"blog.html",context)


def article_detail(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
          first_name = form.data.get("first_name")
          text = form.data["text"]
          rating = form.data["rating"]
          comment = Comment(
            first_name = first_name,
            text = text,
            rating = rating,
            article = article,
          )
          comment.save()
          messages.success(request,'Izoh yuborildi')
          return HttpResponseRedirect(reverse("article-detail",args=[id]))


    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id).order_by("-create_date")
    
    form = CommentForm()
    context = {"article":article,"comments":comments, "form":form}
    return render(request,"article.html",context)


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
    ports = Port.objects.all()
    context = {"ports":ports}
    return render(request, "portfolio.html" ,context=context)

