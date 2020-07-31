from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from useraccount.models import Profile, Addfriend

@receiver(post_save, sender=get_user_model())
def post_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Addfriend)
def post_add_friend_to_both(sender, instance, created, **kwargs):
    sender_ = instance.sender
    reciever_ = instance.reciever
    if instance.status == 'accepted':
        sender_.friends.add(reciever_.user)
        reciever_.friends.add(sender_.user)
        sender_.save()
        reciever_.save()
