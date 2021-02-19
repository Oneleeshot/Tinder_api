from django.contrib import admin
from user_profile.models import UserSubscription, UserImage, UserProfile


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('type_subscription', 'swipes', 'radius')


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'description', 'image', 'latitude', 'longitude',
        'subscription')
