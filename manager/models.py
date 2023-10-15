from django.db import models
from django.contrib.auth.models import User
import string
import random

class Password(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwords")
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)
    length = models.IntegerField()

    def generate(self):
        # Generate a random password
        characters = string.ascii_letters + string.digits + string.punctuation
        self.value = ''.join(random.choice(characters) for _ in range(self.length))

    def __str__(self):
        return self.name