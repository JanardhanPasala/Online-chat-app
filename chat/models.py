from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'sender')
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'receiver')
    chat_message = models.TextField()
    
    def __str__(self):
        return str(self.sender)+ ' to ' +str(self.receiver)