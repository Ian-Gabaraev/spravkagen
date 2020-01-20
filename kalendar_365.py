from bs4 import BeautifulSoup
import requests
import calendar_engine


class Kalendar365:
    def __init__(self):
        self.day = calendar_engine.Calendar().day
        self.year = calendar_engine.Calendar().year
        self.month = calendar_engine.Calendar().get_this_month_in_english()
        self.address = f"https://kalendar-365.ru/orthodox/{self.year}/{self.month}/{self.day}"
        self.events = set()

    def load_events(self):
        response = requests.get(self.address)
        source = response.text
        soup = BeautifulSoup(source, features="html.parser")
        for element in soup.find_all('span', class_='cl'):
            self.events.add('<li>'+element.text.replace('\n','')+'</li>')

    def get_orthodox_events(self):
        self.load_events()
        return list(self.events)
