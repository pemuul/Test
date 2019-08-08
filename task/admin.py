from django.contrib import admin

# Register your models here.
from task.models import Name, Hleba, Proba, Hleb, Koment

admin.site.register(Name)
admin.site.register(Hleba)
admin.site.register(Hleb)
admin.site.register(Proba)
admin.site.register(Koment)