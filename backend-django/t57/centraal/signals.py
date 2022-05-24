from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from centraal.models import Food

## custom user mdoel
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.authtoken.models import Token

from .tasks import add_food_item

@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    print('post-save USER: Create Token')
    if created:
        token = Token.objects.create(user=instance)
        print(token.key)

@receiver(post_save, sender=Food)
def add_food_details(sender, instance, created, **kwargs):
    print('post-save Food Item')
    if created:
        add_food_item.delay(instance.pk)

# @receiver(pre_delete, sender=Url)
# def delete_from_trello(sender, instance, **kwargs):
#     print('pre-delete')
#     remove_url_from_trello.delay(instance.u_owner.pk, instance.u_trello_card_id)
