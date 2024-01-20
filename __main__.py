from lib.booking import BookingAutomation
from tqdm import tqdm
import time

def main():
    booking = BookingAutomation()

    # Call the methods in the desired order
    booking.load_page()
    
    for i in tqdm(range(20)):
        time.sleep(1)
    
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
    
    
if __name__ == '__main__':
    main()