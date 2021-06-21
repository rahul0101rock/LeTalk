from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class user_search(models.Model):
    username=models.CharField(max_length=100)

class friends_list(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="friends")

    def add_in_list(self,acc):
        if not acc in self.friends.all(): self.friends.add(acc)
        self.save()

    def remove_from_list(self,acc):
        if acc in self.friends.all(): self.friends.remove(acc)
        self.save()

class request_list(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    is_in=  models.BooleanField(blank=False, null=False, default=True)

    def allow(self):
        rl = friends_list.objects.get(user=self.recevier)
        if rl:
            rl.add_in_list(self.sender)
            self.is_in = False
            self.save()
    def remove(self):
        self.is_in = False
        self.save()

    def __str__(self): return self.sender.username


