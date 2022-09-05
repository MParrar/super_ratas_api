import datetime


class DateFormat():

    @classmethod
    def convert_date(self, date):
        if date != None:
            return datetime.datetime.strftime(date, '%d/%m/%Y')
