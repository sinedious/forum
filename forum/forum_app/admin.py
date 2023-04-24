from django.contrib import admin
from forum_app.models import beitrag,Feedback

class PostAdmin(admin.ModelAdmin):
    list_filter=("pub_date")    #Zum filtern von den beiträgen gedacht, funktioniert nicht xd?
    list_display=("pub_date")

admin.site.register(beitrag)
admin.site.register(Feedback)
