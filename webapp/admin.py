from django.contrib import admin

# Register your models here.

from .models import Blog, Comments, Contact

class BlogModelAdmin(admin.ModelAdmin):
   list_display = ["title", "date","image"]
   list_filter = ["date"]
   search_fields = ["title",]

   class Meta:
      model = Blog

class CommentModelAdmin(admin.ModelAdmin):
   list_display = ["post", "name",]
   list_filter = ["post"]
   search_fields = ["name","post"]

   class Meta:
      model = Comments

class ContactModelAdmin(admin.ModelAdmin):
   list_display = ["name", "mail_id","date"]
   list_filter = ["date","name"]
   search_fields = ["name",]

   class Meta:
      model = Contact

admin.site.register(Blog, BlogModelAdmin)
admin.site.register(Comments, CommentModelAdmin)
admin.site.register(Contact, ContactModelAdmin)
