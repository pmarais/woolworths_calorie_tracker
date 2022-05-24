from statistics import mode
from django.db import models

## for importing custom user model
from django.conf import settings
## custom user mdoel import as User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models import Sum
import datetime


# Create your models here.
class Food(models.Model):
    f_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_foods', on_delete=models.CASCADE, null=True, blank=True)
    f_name = models.CharField(max_length=255, default='', blank=True, null=True)
    f_url = models.CharField(max_length=255, default='', blank=True, null=True)
    f_image_url = models.CharField(max_length=255, default='', blank=True, null=True)
    f_ingredients = models.TextField(default='', blank=True, null=True)
    f_total_fat = models.FloatField(default=0, blank=True, null=True)
    f_sat_fat = models.FloatField(default=0, blank=True, null=True)
    f_trans_fat = models.FloatField(default=0, blank=True, null=True)
    f_mono_fat = models.FloatField(default=0, blank=True, null=True)
    f_poly_fat = models.FloatField(default=0, blank=True, null=True)
    f_chol_fat = models.FloatField(default=0, blank=True, null=True)
    f_fibre = models.FloatField(default=0, blank=True, null=True)
    f_kj = models.FloatField(default=0, blank=True, null=True)
    f_kcal = models.FloatField(default=0, blank=True, null=True)
    f_sodium = models.FloatField(default=0, blank=True, null=True)
    f_protein = models.FloatField(default=0, blank=True, null=True)
    f_carb = models.FloatField(default=0, blank=True, null=True)
    f_sugar = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return "%s) %s [%s]"%(self.pk, self.f_name, self.f_kcal)


class Portion(models.Model):
    p_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_portions', on_delete=models.CASCADE, null=True, blank=True)
    p_food = models.ForeignKey(Food, related_name='food_portions', on_delete=models.CASCADE, null=True, blank=True)
    p_dry_weight = models.FloatField(default=0, blank=True, null=True)
    p_date = models.DateTimeField(blank=True, null=True)
    p_total_fat = models.FloatField(default=0, blank=True, null=True)
    p_sat_fat = models.FloatField(default=0, blank=True, null=True)
    p_trans_fat = models.FloatField(default=0, blank=True, null=True)
    p_mono_fat = models.FloatField(default=0, blank=True, null=True)
    p_poly_fat = models.FloatField(default=0, blank=True, null=True)
    p_chol_fat = models.FloatField(default=0, blank=True, null=True)
    p_fibre = models.FloatField(default=0, blank=True, null=True)
    p_kj = models.FloatField(default=0, blank=True, null=True)
    p_kcal = models.FloatField(default=0, blank=True, null=True)
    p_sodium = models.FloatField(default=0, blank=True, null=True)
    p_protein = models.FloatField(default=0, blank=True, null=True)
    p_carb = models.FloatField(default=0, blank=True, null=True)
    p_sugar = models.FloatField(default=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.p_dry_weight:
            return
        ratio = self.p_dry_weight/100.0
        self.p_total_fat = self.p_food.f_total_fat * ratio
        self.p_sat_fat = self.p_food.f_sat_fat * ratio
        self.p_trans_fat = self.p_food.f_trans_fat * ratio
        self.p_mono_fat = self.p_food.f_mono_fat * ratio
        self.p_poly_fat = self.p_food.f_poly_fat * ratio
        self.p_chol_fat = self.p_food.f_chol_fat * ratio
        self.p_fibre = self.p_food.f_fibre * ratio
        self.p_kj = self.p_food.f_kj * ratio
        self.p_kcal = self.p_food.f_kcal * ratio
        self.p_sodium = self.p_food.f_sodium * ratio
        self.p_protein = self.p_food.f_protein * ratio
        self.p_carb = self.p_food.f_carb * ratio
        self.p_sugar = self.p_food.f_sugar * ratio
        super(Portion, self).save(*args, **kwargs)
    

    def __str__(self):
        return "%s) %s [%s]"%(self.pk, self.p_food, self.p_dry_weight)


def get_todays_tally(date=None):
    thisdate = date if date else datetime.date.today()
    portions = Portion.objects.filter(p_date__contains=thisdate)
    total = {
        'kcal': 0,
        'carbs': 0,
        'fat': 0,
        'protein': 0,
        'fibre': 0,
    }
    for portion in portions:
        total['kcal'] = total['kcal'] + portion.p_kcal
        total['carbs'] = total['carbs'] + portion.p_carb
        total['fat'] = total['fat'] + portion.p_fa
        total['protein'] = total['kcal'] + portion.p_kcal
        total['fibre'] = total['kcal'] + portion.p_kcal
    return total
