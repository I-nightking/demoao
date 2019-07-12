from django.contrib import admin
from index.models import AndroidTitle,AndroidFile,AndroidText,AndroidSubtitle
# Register your models here.
admin.site.register(AndroidText)
admin.site.register(AndroidSubtitle)
admin.site.register(AndroidTitle)
admin.site.register(AndroidFile)
