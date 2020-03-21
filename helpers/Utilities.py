from datetime import datetime


class TimeHelper:
    @staticmethod
    def getCurrentTimeStamp():
        today = datetime.now()
        str_date = today.strftime("%m/%d/%y %H:%M")
        return str_date
