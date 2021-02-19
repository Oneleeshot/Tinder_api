from django.contrib.auth.models import User
from django.db import models


class Match(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='second_user')
    first_like_second = models.BooleanField(default=False)
    second_like_first = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.first_like_second and self.second_like_first:
            super().save(force_insert=force_insert, force_update=force_update,
                         using=using,
                         update_fields=update_fields)
        else:
            raise Exception('Likes are not mutual ')


class Message(models.Model):
    text = models.TextField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
