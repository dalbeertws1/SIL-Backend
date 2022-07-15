from django.db import models



class Player(models.Model):

    username = models.CharField(max_length=50)
    photo = models.ImageField()


    def __str__(self):
        return self.username
    

class Room(models.Model):

    room_name = models.CharField(max_length=200, unique=True)
    room_password = models.CharField(max_length=100)
    created_by = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='created_by')
    player = models.ManyToManyField(Player) 
    bhabi = models.ForeignKey(Player, on_delete=models.CASCADE, related_name = 'bhabi', null=True, blank=True)

    def __str__(self):
        return self.room_name
    
