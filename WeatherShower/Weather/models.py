from django.db import models as md

class city(md.Model):
    name = md.CharField(max_length=30)

    def __str__(self):
        return self.name
