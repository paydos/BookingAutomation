from lib.date import DateAdapter, DateCalculator

class BookingAutomation:
    def __init__(self):
        # date convention = 2024-01-17 15:30:00
        self.date = DateCalculator.get_next_thursday()
        self.start_time = DateAdapter(self.date).start()
        self.finish_time = DateAdapter(self.date).finish()


    def choose_starting_time(self):
        # Choose starting date
        print(self.start_time)
        

    def choose_finish_time(self):
        print(self.finish_time)
        



# Create an instance of the class
booking = BookingAutomation()

# Call the methods in the desired order

booking.choose_starting_time()
booking.choose_finish_time()
