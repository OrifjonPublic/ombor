from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import IceCream, ActionLog

@receiver(post_save, sender=IceCream)
def log_icecream_save(sender, instance, created, **kwargs):
    user = getattr(instance, '_log_user', None)
    action = 'create' if created else 'update'
    old_quantity = getattr(instance, '_old_quantity', instance.quantity)
    new_quantity = instance.quantity
    delta = abs(new_quantity - old_quantity)

    ActionLog.objects.create(
        user=user,
        action=action,
        object_name=instance.name,
        object_id=instance.code,
        object_repr=f"Miqdor {old_quantity} dan {new_quantity} ga o'zgardi." if not created else f"{instance.quantity} ta yaratildi",
        quantity=delta
    )

@receiver(post_delete, sender=IceCream)
def log_icecream_delete(sender, instance, **kwargs):
    user = getattr(instance, '_log_user', None)
    ActionLog.objects.create(
        user=user,
        action='delete',
        object_name=instance.name,
        object_id=instance.code,
        object_repr=f"{instance.quantity} ta mahsulot o‘chirildi",
        quantity=instance.quantity
    )
