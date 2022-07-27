from django.contrib import admin

# Register your models here.
from hunt.models import Puzzle, PuzzleStatus, TeamTask, TeamTaskStatus, Tries


class GameAdmin(admin.ModelAdmin):
    fields = ('serial_no', 'description', 'pdf','answer')

admin.site.register(Puzzle, GameAdmin)

models = [ PuzzleStatus, TeamTask, TeamTaskStatus, Tries]
admin.site.register(models)