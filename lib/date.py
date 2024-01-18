from datetime import datetime, timedelta

class DateCalculator:
    @staticmethod
    def get_next_tuesday():
        # Calculate the number of days until the next Tuesday
        days_to_next_tuesday = (1 - datetime.now().weekday() + 7) % 7

        # Calculate the total number of days until the Tuesday of the week after next
        total_days_tuesday = days_to_next_tuesday + 7 if days_to_next_tuesday != 0 else 14

        # Get the date of the Tuesday of the week after next
        two_weeks_tuesday : datetime = datetime.now() + timedelta(days=total_days_tuesday)

        return two_weeks_tuesday.replace(microsecond=0)

    @staticmethod
    def get_next_thursday():
        # Calculate the number of days until the next Thursday
        days_to_next_thursday = (3 - datetime.now().weekday() + 7) % 7

        # Calculate the total number of days until the Thursday of the week after next
        total_days_thursday = days_to_next_thursday + 7 if days_to_next_thursday != 0 else 14

        # Get the date of the Thursday of the week after next
        two_weeks_thursday : datetime = datetime.now() + timedelta(days=total_days_thursday)

        return two_weeks_thursday.replace(hour=9, minute=0, second=0, microsecond=0)


a = DateCalculator.get_next_tuesday()
b = DateCalculator.get_next_thursday()


class DateAdapter:
    def __init__(self, date : datetime):
        self.date = date
        
    def start(self):
        return self.date.replace(hour=9, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
        pass
    
    
    def finish(self, custom_end : datetime = None):
        if custom_end:
            return self.date.replace(hour=17, minute=0, second=0, microsecond=0) + custom_end
            pass
            
        else:
            return self.date.replace(hour=17, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
