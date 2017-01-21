from django import forms
from .models import Comments

# Create your tests here.
class Contact(forms.Form):
   name = forms.CharField(required = True,)
   mail_id = forms.CharField(required = True,)
   message = forms.CharField(required = True, widget = forms.Textarea)
  
class Comment(forms.Form):
   name  = forms.CharField(required = True,)
   comment = forms.CharField(required = True,)
   



   '''class Meta:
      model = Comments
      fields = ["name","comment","pic"]'''
