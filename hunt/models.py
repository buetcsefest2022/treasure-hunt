from tabnanny import verbose
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return 'puzzle/{0}'.format(filename)


class Puzzle(models.Model):
    class Meta:
        verbose_name = "Puzzle"
        verbose_name_plural = "(Add) Puzzles"

    serial_no = models.IntegerField(unique=True, blank=False)
    pdf = models.FileField(upload_to=user_directory_path, null=True)
    answer = models.CharField(max_length=100)

    def location_show(self):  # receives the instance as an argument
        return mark_safe('<img src="{thumb}" width="200" height="150" />'.format(
            thumb=self.location_clue.url,
        ))

    location_show.allow_tags = True
    location_show.short_description = 'Location Image'

    def save(self, *args, **kwargs):
        super(Puzzle, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.serial_no) + " ::: Answer: " + str(self.answer)


class PuzzleStatus(models.Model):
    class Meta:
        verbose_name = "Puzzle Status"
        verbose_name_plural = "Puzzle Statuses"

    team = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Puzzle, on_delete=models.CASCADE)

    puzzle_get_time = models.DateTimeField(null=True)
    puzzle_sub_time = models.DateTimeField(null=True)
    puzzle_tried = models.IntegerField(default=0)
    puzzle_finished = models.BooleanField(default=False)
    puzzle_finished_time = models.DateTimeField(null=True)


    def __str__(self) -> str:
        return str(self.team.username) + " ::: Puzzle: " + str(self.game.serial_no) + " | Tries: " + str(self.puzzle_tried)


class TeamTask(models.Model):
    class Meta:
        verbose_name = "Team Task"
        verbose_name_plural = "(Add) Team Tasks"

    team = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return str(self.team.username) + " ::: Task Serial: " + str(self.tasks)



class TeamTaskStatus(models.Model):
    class Meta:
        verbose_name = "Team Task Status"
        verbose_name_plural = "Team Task Statuses"

    team = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='n')

    def __str__(self) -> str:
        return str(self.team.username) + " ::: Task: " + str(self.task.serial_no) + " | Answer: " + str(self.task.answer)



class Tries(models.Model):
    class Meta:
        verbose_name = "Try"
        verbose_name_plural = "Tries"

    team = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    text = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.team.username) + " ::: Entry: " + str(self.text)


@receiver(post_save, sender=TeamTask)
def add_team_task_status(sender, instance, created, **kwargs):
    if not created:
        TeamTaskStatus.objects.filter(team=instance.team).delete()

    task_list = instance.tasks
    tasks = list(map(int, task_list.split(',')))
    print(tasks)
    for task in tasks:
        game = Puzzle.objects.filter(serial_no=task).get()
        status = TeamTaskStatus()
        status.team = instance.team
        status.task = game
        status.save()
