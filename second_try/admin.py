from django.contrib import admin
from second_try.models import AccessRecord,Topic,Webpage,Users_test
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users_test)