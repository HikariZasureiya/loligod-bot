from django.contrib import admin

# Register your models here.
from .models import ai_chat_history , confession_model

admin.site.register(ai_chat_history)
admin.site.register(confession_model)