from django.contrib import admin

from message_match.models import Match, Message


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'first_user', 'second_user', 'first_like_second', 'second_like_first')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'match')
