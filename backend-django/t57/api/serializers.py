# from centraal.models import Url
from rest_framework import serializers
from centraal.models import *

# Serializers define the API representation.
class FoodSerializer(serializers.ModelSerializer):
    f_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Food
        # fields = ['url', 'username', 'email', 'is_staff']
        fields =  '__all__'
        read_only_fields = [ 'f_owner', 'f_name', 'f_image_url', 'f_ingredients', 'f_sat_fat', 'f_trans_fat', 'f_mono_fat', 'f_poly_fat', 'f_chol_fat', 'f_fibre', 'f_kj', 'f_kcal', 'f_sodium', 'f_protein', 'f_carb', 'f_sugar']


# Serializers define the API representation.
class PortionSerializer(serializers.ModelSerializer):
    p_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Portion
        # fields = ['url', 'username', 'email', 'is_staff']
        fields =  '__all__'
        # depth = 1
        read_only_fields = [ 'p_sat_fat', 'p_trans_fat', 'p_mono_fat', 'p_poly_fat', 'p_chol_fat', 'p_fibre', 'p_kj', 'p_kcal', 'p_sodium', 'p_protein', 'p_carb', 'p_sugar']