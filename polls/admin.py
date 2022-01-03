from django.contrib import admin

from .templates import polls 
from .models import Question
admin.site.register(Question)

# admin.site.register(polls)
# Register your models here.




