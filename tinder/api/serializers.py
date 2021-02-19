from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers
from message_match.models import Match, Message
from user_profile.models import UserProfile, UserImage, UserSubscription


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['first_user', 'second_user', 'first_like_second',
                  'second_like_first']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'match']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ['image']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['type_subscription', 'swipes', 'radius']


class ProfileSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subscription = SubscriptionSerializer()
    link = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'description', 'image', 'latitude', 'longitude',
                  'subscription', 'link']

    def get_link(self, obj):
        uri = reverse('profiles-detail', kwargs={'pk': obj.pk})
        return self.context['request'].build_absolute_uri(uri)


class UserSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'link']

    def get_link(self, obj):
        uri = reverse('users-detail', kwargs={'pk': obj.pk})
        return self.context['request'].build_absolute_uri(uri)
