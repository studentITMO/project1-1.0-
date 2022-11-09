from django.db import models

class myLinks(models.Model):
    link_url = models.CharField(max_length = 100)
    link_name = models.CharField(max_length = 50)
    link_text = models.TextField()
