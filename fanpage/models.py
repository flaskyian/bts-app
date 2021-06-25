from django.db import models
import uuid

class Post(models.Model):

    public_id = models.UUIDField(default=uuid.uuid4, editable=False)

    active = models.BooleanField(default=True)

    author = models.CharField(max_length=64)

    post = models.TextField()
    
    created_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author