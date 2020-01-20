# Here the data is processed.
import calendar_engine
import kalendar_365
import calendru
import wikipedia


class Article:
    def __init__(self):

        # Instances.
        self.calendar_object = calendar_engine.Calendar()
        self.kalendar_365_object = kalendar_365.Kalendar365()
        self.calend_ru_object = calendru.CalendRu()
        self.wikipedia_object = wikipedia.Wikipedia()

        # Current date information.
        self.month = self.calendar_object.get_this_month_in_cyrillic()
        self.day = self.calendar_object.day
        self.date = str(self.day) + ' ' + self.month

        # Variables for formatted strings.
        self.orthodox_events = self.kalendar_365_object.get_orthodox_events()
        self.orthodox_events = '\n'.join(self.orthodox_events)

        self.whose_birthday = self.calend_ru_object.load_birthdays()
        self.whose_birthday = ''.join(self.calend_ru_object.birthdays)

        self.what_happened = self.wikipedia_object.get_events(li=True)
        self.who_was_born = self.wikipedia_object.get_birthdays(li=True)

        self.folk_events = self.calend_ru_object.generate_text_for_folk_holidays(html=True)
        self.main_holidays = self.calend_ru_object.generate_text_for_main_holidays(html=True)

        self.all_holidays = self.calend_ru_object.get_list_of_all_holidays()

        # Email template.
        self.as_html = f"""
        <html>
        <head>
        </head>
        <body style="font-size: 1.3rem">
        <h3>{self.date}: какой сегодня праздник в России и мире - события из календаря</h3>
            <p>
            {self.main_holidays}
            </p>
        <h3>Какой праздник {self.date}</h3>
            <ul>
            {self.all_holidays}
            </ul>
        <h3>Что произошло {self.date}</h3>
            <ul>
        {self.what_happened}
            </ul>
        <h3>Кто из известных людей родился {self.date}</h3>
            <ul>
        {self.who_was_born}
            </ul>
        <h3>Дата {self.date} в церковном календаре</h3>
            <h4>Православный календарь</h4>
            <ul>
        {self.orthodox_events}
            </ul>
            <h4>Народный календарь</h4>
            <ul>
        {self.folk_events}
            </ul>
        <h3>Кто празднует именины {self.date}</h3>
            <ul>
        {self.whose_birthday}
            </ul>
        </body>
        </html>
        """
