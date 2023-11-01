from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order, Notification


@receiver(post_save, sender=Order)
def send_order_creation_notification(sender, instance, created, **kwargs):
    if created:  # Check if the instance is newly created
        # Compose the email message
        subject = 'New Order Created'
        message = f"A new order with ID {instance.id} has been created."
        send_mail(subject, message, 'dryzz.official@gmail.com', [instance.user.email])

        notification = Notification()
        notification.order = Order.objects.get(id=instance.id)
        notification.save()
