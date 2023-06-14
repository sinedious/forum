from django.contrib import admin
from forum_app.models import beitrag, comment
from lehrer.models import Feedback
from message.models import Message

class PostAdmin(admin.ModelAdmin):
    list_filter=("pub_date")    #Zum filtern von den beiträgen gedacht, funktioniert nicht xd?
    list_display=("pub_date")

admin.site.register(beitrag)
admin.site.register(Feedback)
admin.site.register(Message)
admin.site.register(comment)
