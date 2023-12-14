import requests
from bs4 import BeautifulSoup
from datetime import date

class Parser(object):
    def __init__(self):
        self.url = 'https://weather.com/uk-UA/weather/today/l/aef1ae844a5a6d6514dd32c8f723d7cd1ad4e49f08085207b5c0b336a9d0116d'
        self.today = str(date.today())
        self.resp = requests.get(self.url)
        self.today_weather = []

    def __str__(self):
        return f'Посилаючись на {self.url}, станом на {self.today} {self.today_weather}'

    def run(self):
        soup = BeautifulSoup(self.resp.text, 'lxml')
        values = soup.find('ul', class_='WeatherTable--columns--6JrVO WeatherTable--wide--KY3eP').findAll('li',
                                                                                                          class_='''Column--column--3tAuz''')
        for value in values:
            time = value.find('a').find('h3')
            degree = value.find('a').find('div', attrs={'data-testid': 'SegmentHighTemp'})
            data = [self.today, {time.text: degree.text}]
            string = f'{list(data[1].keys())[0]} - {list(data[1].values())[0]}'
            self.today_weather.append(string)
        return ''.join([self.today_weather[a]+'\n' for a in range(len(self.today_weather))])

Parser().run()
