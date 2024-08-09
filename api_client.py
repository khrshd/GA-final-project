import http.client
import json

class weather_api_client:
    def __init__(self):
        self.api_url_base = 'api.openweathermap.org/data/2.5/'
        self.api_key = '623af9cc19f6aab782588ed432ed3434'
    
    def get_weather(self, city_name):
        
        # https://api.openweathermap.org/data/2.5/weather?q=Boston,US&appid=623af9cc19f6aab782588ed432ed3434

        api_url = '{0}weather?q={1}&appId={2}'.format(self.api_url_base, city_name, self.api_key)
                
        connection = http.client.HTTPSConnection(self.api_url_base, 80, timeout=10)
              
        headers = {'Content-Type': 'application/json'}
                
        connection.request("GET", api_url, json.dumps(headers))

        response = connection.getresponse()

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return response.content

    def get_forecast(self, city_name):
        
        # https://api.openweathermap.org/data/2.5/forecast?q=Boston,US&appid=623af9cc19f6aab782588ed432ed3434

        api_url = '{0}forecast?q={1}&appId={2}'.format(self.api_url_base, city_name, self.api_key)
                
        connection = http.client.HTTPSConnection(self.api_url_base, 80, timeout=10)
              
        headers = {'Content-Type': 'application/json'}
                
        connection.request("GET", api_url, json.dumps(headers))

        response = connection.getresponse()

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return response.content