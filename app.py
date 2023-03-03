import streamlit as st
import requests
from datetime import datetime
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
#st.write('date and time', date_and_time)
#st.write('pickup longitude', pickup_longitude)
#st.write('pickup latitude', pickup_latitude)
#st.write('dropoff longitude', dropoff_longitude)
#st.write('dropoff latitude ', dropoff_latitude )
#st.write('passenger count ', passenger_count )

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
pickup_longitude = st.number_input('pickup longitude',value=-73.950655)
pickup_latitude = st.number_input('pickup latitude',value=40.783282)
dropoff_longitude = st.number_input('dropoff longitude',value=-73.984365)
dropoff_latitude = st.number_input('dropoff latitude', value=40.769802)
passenger_count = st.number_input('passenger count', value=1)
datetime_str_input = st.text_input("Date and time (YYYY-MM-DD HH:MM:SS)", value="2013-07-06 17:18:00")
# Convert the datetime string to a datetime object
#datetime_obj = datetime.strptime(datetime_str_input, "%Y-%m-%d %H:%M:%S")
params = dict(pickup_datetime=datetime_str_input,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count
              )

url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(url, params=params)
prediction = response.json()
results = prediction['fare']
if st.button('predict'):
    st.write(f'prediction result:{results}')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
