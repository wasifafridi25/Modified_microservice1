from flask import Flask, request
import requests

app = Flask(__name__)
@app.route('/cityweather', methods=['GET'])
def get_city_weather():
    city = request.args.get('city')
    state = request.args.get('state')
    
    # Call the first microservice to get the zip code
    zip_code_url = f"https://www.zipwise.com/webservices/citysearch.php?key=jb49u2fszhvghy74&format=json&string={city}&state={state}"
    zip_code_response = requests.get(zip_code_url)
    zip_code_data = zip_code_response.json()
    
    
    zip_code = zip_code_data['results'][0]['zip']
    #calling the second microservice which is listening on port 8001. 
    weather_url = f'http://localhost:8001/weather/{zip_code}'
    response = requests.get(weather_url)
    weather_data = response.json()
    weather_condition = weather_data['weather'][0]['main']
    
    return f"<h1>Zip Code: {zip_code}</h1><br><h1>Weather condition: {weather_condition}</h1>"
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)


#address - http://localhost:8000/cityweather?city=Fremont&state=CA    




