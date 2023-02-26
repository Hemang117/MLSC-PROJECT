from django.contrib import admin
from app1 import models
from .models import loginpage
from .models import profile
from .models import application
from .models import events
from .models import lof
from .models import queries 

admin.site.register(loginpage)
admin.site.register(profile)
admin.site.register(application)
admin.site.register(events)
admin.site.register(lof)
admin.site.register(queries)

# Register your models here.
