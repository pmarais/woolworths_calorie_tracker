import requests
from bs4 import BeautifulSoup
import json
import re

# Create your tasks here

from celery import shared_task
import os

@shared_task
def add_food_item(pk):
    from centraal.models import Food

    food = Food.objects.get(pk=pk)

    print(food)

    ## Checking if the web object was saved to string in JSON via a previous collect
    if food.f_json_dumps:
        product = json.loads(food.f_json_dumps)
    ## If not, collect
    else:
        url = food.f_url
        html_data = requests.get(url).text
        data = re.search(r'window\.__INITIAL_STATE__ = ({.*})', html_data).group(1)
        data = json.loads(data)

        productCollection = data['pdp']['productInfo']
        nutritional = data['pdp']['productInfo']['multiAttributes']

        image_url = productCollection['colourSKUs'][0]['images'][0]['external']
        ingredients = productCollection['textualAttributes']['INGREDIENTS'] if productCollection['textualAttributes'] else ''
        displayname = data['pdp']['productInfo']['displayName']
        url = "https://www.woolworths.co.za%s"%data['pdp']['productInfo']['productURL']
        productInfo = { item['text']: {'val': item['element1'], 'unit': item['element3']} for item in nutritional if item['text'] in ['Sodium', 'Carbohydrate', 'Energy', 'Dietary fibre#', 'Energy', 'Protein', 'Total fat', 'polyunsaturated fat', 'monounsaturated fat', 'Cholesterol', 'total sugar', 'trans fat', 'saturated fat']}

        product = {
            'displayname': displayname,
            'ingredients': ingredients,
            'image_url': image_url,
            'url': url,
            'info': productInfo,
        }

        ## Filter out all nonumeric characters except "."
        non_decimal = re.compile(r'[^\d.]+')

        for key, value in product['info'].items():
            res = non_decimal.sub('', product['info'][key]['val'])
            product['info'][key]['val'] = res

        ## Store to model in Text Format (for SQLite)
        food.f_json_dumps = json.dumps(product)
        food.save()

    # print(product)

    ## Build the product dict
    food.f_name = product['displayname'] if 'displayname' in product else ''
    food.f_image_url = product['image_url'] if 'image_url' in product else ''
    food.f_ingredients = product['ingredients'] if 'ingredients' in product else ''
    if 'info' in product:
        food.f_total_fat = float(product['info']['Total fat']['val']) if 'Total fat' in product['info'] else 0
        food.f_sat_fat = float(product['info']['saturated fat']['val']) if 'saturated fat' in product['info'] else 0
        food.f_trans_fat = float(product['info']['trans fat']['val']) if 'trans fat' in product['info'] else 0
        food.f_mono_fat = float(product['info']['monounsaturated fat']['val']) if 'monounsaturated fat' in product['info'] else 0
        food.f_poly_fat = float(product['info']['polyunsaturated fat']['val']) if 'polyunsaturated fat' in product['info'] else 0
        food.f_chol_fat = float(product['info']['Cholesterol']['val']) if 'Cholesterol' in product['info'] else 0
        food.f_fibre = float(product['info']['Dietary fibre#']['val']) if 'Dietary fibre#' in product['info'] else 0
        food.f_kj = float(product['info']['Energy']['val']) if 'Energy' in product['info'] else 0
        food.f_kcal = food.f_kj/4.1868 if food.f_kj else 0
        food.f_sodium = float(product['info']['Sodium']['val']) if 'Sodium' in product['info'] else 0
        food.f_protein = float(product['info']['Protein']['val']) if 'Protein' in product['info'] else 0
        food.f_carb = float(product['info']['Carbohydrate']['val']) if 'Carbohydrate' in product['info'] else 0
        food.f_sugar = float(product['info']['total sugar']['val']) if 'total sugar' in product['info'] else 0
    food.save()
    

# add_url_to_trello.delay(url.pk)
# @shared_task
# def remove_url_from_trello(user_pk, u_trello_card_id):
#     # from centraal.utils import connect_to_trello_retieve_card
#     # card = connect_to_trello_retieve_card(u_trello_card_id)
#     # card.delete()
#     from centraal.models import User
#     from centraal.utils import TrelloClientClass
#     user = User.objects.get(pk=user_pk)
#     tc = TrelloClientClass(user)
#     card = tc.connect_to_trello_retieve_card(u_trello_card_id)
#     card.delete()
#     