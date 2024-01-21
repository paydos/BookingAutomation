import logging

from lib.booking import BookingAutomation
from lib.setup import AutoInstaller  # noqa: F401
from lib.date import today
from lib.cron import cron


def job():
    try:
        booking = BookingAutomation(day=today) # Use day = 1 or day = 3 for testing
        # Call the methods in the desired order
        booking.load_page()
                
        # Make a reservation
        booking.make_reservation()
        
        # Change the location
        booking.change_location()
        
        # Type the location
        booking.type_location()
        
        # Choose the floor
        booking.choose_floor()
        
        # Choose the starting time
        booking.choose_starting_time()
        
        # Choose the finish time
        booking.choose_finish_time()

        # Search for available slots
        booking.search()
        
        # Apply filters
        booking.filters()
        
        # Book the seat
        booking.book_seat()
        
        # Introduce a delay
        booking.delay()
        
        # Close driver to avoid RAM garbage
        booking.close()

    except:   # noqa: E722
        logging.exception("Today's not Tuesday or Thursday. Going back to Cron mode.")
    
        
        

    
def main():
    logging.basicConfig(force=True, filename='BookingAutomation.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info('Booking automation service initialised.')
    cron(job=job)



if __name__ == '__main__':
    main()