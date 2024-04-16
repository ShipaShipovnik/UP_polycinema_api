from django.contrib import admin
from .models import Position,Comment


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Position, PositionAdmin)
admin.site.register(Comment)