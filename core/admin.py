from django.contrib import admin
#
#### Register your models here.
##
from .models import (User, Genre, Document,
                     Language, Currency, Account,
                     Project, Permissions)
                     

# Minimal registration of Models.
admin.site.register(Document)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Project)
admin.site.register(Permissions)
