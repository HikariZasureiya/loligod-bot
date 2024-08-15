from django.db import models

class ai_chat_history(models.Model):
    server_id = models.BigIntegerField()
    prompt = models.CharField(max_length=2000 , null = False)


