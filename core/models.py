from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class TeamProfile(models.Model):
    class Meta:
        verbose_name = "Team Profile"
        verbose_name_plural = "Team Profiles"
        db_table = 'user_profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_completed = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    start_code = models.CharField(max_length=6)
    password = models.CharField(max_length=20,null=True)

    def __str__(self) -> str:
        return str(self.user.username) + " :::  Level: " + str(self.level_completed) + " | StartCode: " + str(self.start_code) + " | Password: " + str(self.password)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        TeamProfile.objects.create(user=instance)
    instance.teamprofile.save()
