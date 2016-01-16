from django.contrib import admin
from models import CatPicture, CatProfile, CatStatus, StatusComment, PictureComment
# Register your models here.

admin.site.register(CatPicture)
admin.site.register(CatProfile)
admin.site.register(CatStatus)
admin.site.register(StatusComment)
admin.site.register(PictureComment)

