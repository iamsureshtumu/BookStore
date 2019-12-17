from django.contrib import admin
from .models import Sslc,Puc,Engineering,Masters,User_data
# Register your models here.
admin.site.register(Sslc)
admin.site.register(Puc)
admin.site.register(Engineering)
admin.site.register(Masters)
admin.site.register(User_data)
admin.site.site_header = 'BookStore Admin'
