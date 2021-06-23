from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Perfil(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='example.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Estacionamiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estacionamientos')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'{self.user.username}: {self.content}'
