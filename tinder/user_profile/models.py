from django.contrib.auth.models import User
from django.db import models

TYPE_SUBSCRIPTIONS = (
    ('standard', 'standard'),
    ('vip', 'vip'),
    ('premium', 'premium')
)
OPTIONS_SUBSCRIPTIONS = {
    'standard': {'swipes': 20,
                 'radius': 10},
    'vip': {'swipes': 100,
            'radius': 25}
}


class UserSubscription(models.Model):
    type_subscription = models.CharField(max_length=100,
                                         choices=TYPE_SUBSCRIPTIONS,
                                         default='standard')
    swipes = models.IntegerField(null=True)
    radius = models.IntegerField(null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.type_subscription == 'standard' and self.type_subscription == 'vip':
            self.swipes = OPTIONS_SUBSCRIPTIONS[self.type_subscription][
                'swipes']
            self.radius = OPTIONS_SUBSCRIPTIONS[self.type_subscription][
                'radius']
        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)

    def __str__(self):
        return self.type_subscription


class UserImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ForeignKey(UserImage, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    subscription = models.OneToOneField(UserSubscription,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
