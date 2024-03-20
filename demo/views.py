from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Book
from .forms import Book_Form,Author_Form,book_formset


def demo(request):
    if request.method=='GET':
    
    
        #form=Book_Form()
        form=book_formset(queryset=Book.objects.none())
        author_form=Author_Form()
    elif request.method=='POST':
        author_form=Author_Form(request.POST)
        form=book_formset(request.POST)
        
        if form.is_valid() and author_form.is_valid():
            author=author_form.save()
            for x in form:
                book=x.save(commit=False)
                book.name=author
                book.save()
                

         
                
                
           
            
    else:
        return HttpResponse("welcome demo")
    return render(request,'demo_app/gemo1.html',{'formset':form,'author_form':author_form})



    #author=Author.objects.get(name="sonu")
    #author=author.from_books.all()
    #books=Book.objects.all()
    #return render(request,'demo_app/gemo1.html',{'author':author,'books':books})


    #return HttpResponse("welcome demo")