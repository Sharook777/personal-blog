from django.db import models

# Create your models here.


class Blog(models.Model):
   title = models.CharField(max_length=200)
   body = models.TextField()
   date = models.DateTimeField()
   image = models.FileField(null=True, blank=True)

   def __str__(self):
      return self.title

   class Meta:
      ordering = ["-date"]

class Comments(models.Model):
   post = models.ForeignKey(Blog, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   comment = models.TextField()
   pic = models.FileField(null=True, blank=True)
   date = models.DateTimeField(auto_now=False, auto_now_add=True)
   def __str__(self):
      return self.name+" - "+self.comment
   class Meta:
      ordering = ["-date"]

class Contact(models.Model):
   name = models.CharField(max_length=200)
   mail_id = models.CharField(max_length=300)
   message = models.TextField()
   date = models.DateTimeField(auto_now=False, auto_now_add=True)
   def __str__(self):
      return self.name+" - "+self.mail_id
