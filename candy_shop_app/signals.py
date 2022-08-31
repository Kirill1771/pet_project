from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

from .models import Production


@receiver(pre_delete, sender=Production)
def product_pre_delete_receiver(sender, instance, **kwargs):
    instance.is_active = False


@receiver(post_delete, sender=Production)
def product_post_delete_receiver(sender, instance, **kwargs):
    instance.save()