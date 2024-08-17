from django.db import models

class ai_chat_history(models.Model):
    server_id = models.BigIntegerField()
    prompt = models.CharField(max_length=2000 , null = False)

class confession_model(models.Model):
    server_id = models.BigIntegerField()
    count = models.BigIntegerField()
    title = models.CharField(default="anonymous confession" ,max_length=100 , null = False)
    message = models.CharField(max_length=2000 , null = False)

