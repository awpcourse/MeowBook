from django.contrib import admin
from models import CatPicture, CatProfile, CatStatus, StatusComment
# Register your models here.

admin.site.register(CatPicture)
admin.site.register(CatProfile)
admin.site.register(CatStatus)
admin.site.register(StatusComment)

