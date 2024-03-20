from django import forms
from .models import Author,Book
from django.forms import inlineformset_factory

class Author_Form(forms.ModelForm):
       class Meta:
              model=Author
              fields='__all__'
class Book_Form(forms.ModelForm):
       class Meta:
              model=Book
              fields='__all__'


book_formset=inlineformset_factory(Author,Book,form= Book_Form,  extra=1,fields='__all__',fk_name='name',can_delete=True)

