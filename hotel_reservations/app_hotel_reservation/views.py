import pickle as pkl

import pandas as pd
from django.shortcuts import render

cls = pkl.load(open(
    'app_hotel_reservation/models/pipe_etc.pkl', 'rb'))
cls1 = pkl.load(open(
    'app_hotel_reservation/models/pipe_GBC.pkl', 'rb'))
cls2 = pkl.load(open(
    'app_hotel_reservation/models/pipe_KNN.pkl', 'rb'))


def home(request):
    return render(request, 'pages/home.html')


def form(request):
    return render(request, 'pages/form.html')


def formInfo(request):
    no_of_adults = request.GET['no_of_adults']
    no_of_children = request.GET['no_of_children']
    no_of_weekend_nights = request.GET['no_of_weekend_nights']
    no_of_week_nights = request.GET['no_of_week_nights']
    type_of_meal_plan = request.GET['type_of_meal_plan']
    required_car_parking_space = request.GET['required_car_parking_space']
    room_type_reserved = request.GET['room_type_reserved']
    lead_time = request.GET['lead_time']
    arrival_year = request.GET['arrival_year']
    arrival_month = request.GET['arrival_month']
    arrival_date = request.GET['arrival_date']
    market_segment_type = request.GET['market_segment_type']
    repeated_guest = request.GET['repeated_guest']
    no_of_previous_cancellations = request.GET['no_of_previous_cancellations']
    no_of_previous_bookings_not_canceled = request.GET['no_of_previous_bookings_not_canceled']
    avg_price_per_room = request.GET['avg_price_per_room']
    no_of_special_requests = request.GET['no_of_special_requests']

    d_dict = {'no_of_adults': [no_of_adults],
              'no_of_children': [no_of_children],
              'no_of_weekend_nights': [no_of_weekend_nights],
              'no_of_week_nights': [no_of_week_nights],
              'type_of_meal_plan': [type_of_meal_plan],
              'required_car_parking_space': [required_car_parking_space],
              'room_type_reserved': [room_type_reserved],
              'lead_time': [lead_time],
              'arrival_year': [arrival_year],
              'arrival_month': [arrival_month],
              'arrival_date': [arrival_date],
              'market_segment_type': [market_segment_type],
              'repeated_guest': [repeated_guest],
              'no_of_previous_cancellations': [no_of_previous_cancellations],
              'no_of_previous_bookings_not_canceled': [no_of_previous_bookings_not_canceled],
              'avg_price_per_room': [avg_price_per_room],
              'no_of_special_requests': [no_of_special_requests]}

    df = pd.DataFrame.from_dict(d_dict, orient='columns')
    paga = 0
    nao_paga = 0
    y_pred = cls.predict(df)
    y_pred1 = cls1.predict(df)
    y_pred2 = cls2.predict(df)
    if y_pred == 0:
        paga += 1
    else:
        nao_paga += 1
    if y_pred1 == 0:
        paga += 1
    else:
        nao_paga += 1
    if y_pred2 == 0:
        paga += 1
    else:
        nao_paga += 1

    if paga > nao_paga:
        outcome = 'Esse cliente vai ficar!! Aproveita para oferecer mais serviços.'
        imagem = 'services.png'
    else:
        outcome = 'Provável cancelamento!! Encaminhar para o setor de Telemarketing.'
        imagem = 'marketing.png'

    return render(request, 'pages/result.html', {'result': outcome, 'imagem': imagem})
