from django.contrib import admin

# Register your models here.
from home.models import Person, Question, Answer

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)