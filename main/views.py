from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def order_value(request):
    """
    This function calculates the total order value based on items, distance and offer.
    """
    request_data = request.data

    check_fields(request_data)
    
    items_cost = 0
    offer_val = 0

    # items cost
    for i in request_data['order_items']:
        items_cost += i['quantity'] * i['price']

    # delivery cost
    distance = request_data['distance']
    if distance < 0 or distance > 500000:
        response = {
            "status": False,
            "message": "Invalid distance!"
        }
        return Response(response)

    delivery_cost = get_delivery_cost(distance)

    # offer value
    if 'offer' in request_data:
        if request_data['offer']['offer_type'] == 'FLAT':
            offer_val = request_data['offer']['offer_val']
        elif request_data['offer']['offer_type'] == 'DELIVERY':
            offer_val = delivery_cost
        else:
            response = {
                "status": False,
                "message": "Invalid offer!"
            }
            return Response(response)

        if offer_val > items_cost:
            response = {
                "status": False,
                "message": "Offer value is greater than order value!"
            }
            return Response(response)

    order_value = items_cost + delivery_cost - offer_val

    response = {
        "order_value": order_value
    }

    return Response(response)

def get_delivery_cost(distance):
    """
    This function calculates the delivery cost based on the distance. The distance is in meters and the cost should be in paisa.
    """
    delivery_cost = 0 
    if 0 < distance <= 10000:
        delivery_cost = 5000
    elif 10000 < distance <= 20000:
        delivery_cost = 10000
    elif 20000 < distance <= 50000:
        delivery_cost = 50000
    elif 50000 < distance <= 500000:
        delivery_cost = 100000

    return delivery_cost

def check_fields(request_data):
    """
    This function checks if any mandatory fields are missing. If any mandatory fields are missing, it returns a response.
    """
    mandatory_fields = ['order_items', 'distance']
    
    for field in mandatory_fields:
        if field not in request_data:
            response = {
                "status": False,
                "error": {
                    "code": 400,
                    "message": "mandatory fields missing"
                }
            }
        
            return Response(response)