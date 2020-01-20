from bs4 import BeautifulSoup
from settings import search_settings
import requests
import re
import calendar_engine


class CalendRu:
    def __init__(self):
        self.date = calendar_engine.Calendar().get_date_locale_en_us()
        self.address = f"https://calend.ru/day/{self.date}/"
        self.folk_holidays = []
        self.main_holidays = []
        self.all_holidays_titles = set()
        self.secondary_holidays = []
        self.birthdays = []
        self.birthdays_as_dict = {}
        self.main_holidays_text = {}
        self.folk_holidays_text = {}

    def load_birthdays(self, brief_results=search_settings['brief results']):
        response = requests.get(self.address)
        source = response.text
        soup = BeautifulSoup(source, features="html.parser")
        for element in soup.find_all('li', class_='block_name'):
            element = element.text.strip()
            if brief_results:
                name = element.split(' ')[0]
                self.birthdays.append('<li>'+name+'</li>')
            else:
                key = element.split(' ')[0]
                value = ' '.join(element.split(' ')[1:])
                self.birthdays_as_dict[key] = value

    def load_folk_holidays(self):
        response = requests.get(self.address)
        source = response.text
        soup = BeautifulSoup(source, features="html.parser")
        for link in soup.select('.homiesCal > .itemsNet > .three-three > a'):
            self.folk_holidays.append(link['href'])

    def load_main_holidays(self):
        response = requests.get(self.address)
        source = response.text
        soup = BeautifulSoup(source, features="html.parser")
        for link in soup.select('.itemsNet > .three-three > .caption > .title > a'):
            self.main_holidays.append(link['href'])

    def load_secondary_holidays(self):
        response = requests.get(self.address)
        source = response.text
        soup = BeautifulSoup(source, features="html.parser")
        for link in soup.select('.holidays > .itemsNet > .one-three > .caption > .title > a'):
            self.secondary_holidays.append(link['href'])

    def generate_text_for_main_holidays(self, dataset=None, dictionary=None, html=False):
        self.load_main_holidays()
        if not dictionary:
            dictionary = self.main_holidays_text
        if not dataset:
            dataset = self.main_holidays
        for link in dataset:
            response = requests.get(link)
            source = response.text
            soup = BeautifulSoup(source, features="html.parser")
            title = soup.find('h1', itemprop='name headline')
            self.all_holidays_titles.add(title)
            main_text = soup.find_all('div', class_='maintext')
            result = ""
            for paragraph in main_text:
                paragraph = re.sub(r'(?:\(.*}\);)|(?:\(Фото:\s.*\))', '', paragraph.text)
                result += paragraph
            dictionary[title] = result
        if html:
            return self.dict_to_html(dictionary)

    def generate_text_for_folk_holidays(self, html=False):
        self.load_folk_holidays()
        self.generate_text_for_main_holidays(dataset=self.folk_holidays, dictionary=self.folk_holidays_text, html=html)
        # for link in self.folk_holidays:
        #     response = requests.get(link)
        #     source = response.text
        #     soup = BeautifulSoup(source, features="html.parser")
        #     title = soup.find('h1', itemprop='name headline')
        #     self.all_holidays_titles.add(title)
        #     main_text = soup.find_all('div', class_='maintext')
        #     result = ""
        #     for paragraph in main_text:
        #         paragraph = re.sub(r'(?:\(.*}\);)|(?:\(Фото:\s.*\))', '', paragraph.text)
        #         result += paragraph
        #     self.folk_holidays_text[title] = result
        # if html:
        #     return self.dict_to_html(self.folk_holidays_text)

    @staticmethod
    def dict_to_html(dictionary):
        string = ""
        for key, value in dictionary.items():
            string += f"<h3>{key}</h3><p>{value}</p>"
        return string

    def get_list_of_all_holidays(self):
        string = ""
        for element in self.all_holidays_titles:
            this_soup = BeautifulSoup(str(element), features='html.parser')
            element = this_soup.text
            string += f"<li>{element}</li>"
        return string
