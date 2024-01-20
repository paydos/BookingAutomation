import time
from undetected_chromedriver import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import logging

from tqdm import tqdm

from lib.date import DateCalculator, DateAdapter



class BookingAutomation:
    def __init__(self):
        # date coSnvention = 2024-01-17 15:30:00
        self.date = DateCalculator()
        self.date = self.date.get_next_tuesday()
        self.adapter = DateAdapter(self.date)
        self.start_time = self.adapter.start()
        self.finish_time = self.adapter.finish()    
        
        # Custom Parameters
        self.HighResolutionMonitor = True
        self.AdjustableHeightDesk = True

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.bookingInfo = {
            'Desk Location': None,
            'Floor and Address': None
        }

        # Set up chrome profile (Use Default)
        self.logger.info('Creating Google Chrome Driver')
        options = uc.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument("--allow-file-access-from-files")  # Added this line
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--user-data-dir=/home/ruiz/.config/google-chrome/") # Change the path according to your system
        options.add_argument("--profile-directory=Profile 1") # Change to Profile 1 for testing 
        self.driver = uc.Chrome(options=options)

        # Maximize the window
        self.logger.info('Maximizing window...')
        self.driver.maximize_window()

    def load_page(self):
        # Access the booking webpage (sleep=10 to allow it to properly load)
        self.logger.info('Loading page...')
        self.driver.get('file:///test/Make a Reservation - Places.html')        

   
    def book_seat(self):
        
        self._seat_info()
        print("Desk Location: ", self.bookingInfo['Desk Location'])
        print("Floor and Address: ", self.bookingInfo['Floor and Address'])

        
    
        
        time.sleep(2)  # Wait for the booking to process
       
       
    
    def _seat_info(self):
        
        self.logger.info('Saving desk information...')
        
        try:
            time.sleep(2)
            self.bookingInfo['Desk Location'] = self.seat.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/iwms-wsd-horizontal-card/div/div[2]/div/h4').text
            self.logger.info(f'Desk location: {self.bookingInfo["Desk Location"]}')
            
        except Exception as e:
            self.logger.error(f'Unable to fetch Desk Location: {e.__class__.__name__}')   
        
        try:
            time.sleep(2)
            self.bookingInfo['Floor and Address'] = self.seat.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/iwms-wsd-horizontal-card/div/div[2]/div/div[1]').text
            self.logger.info(f'Floor and Address: {self.bookingInfo["Floor and Address"]}')
            
        except Exception as e:
            self.logger.error(f'Unable to fetch Floor and Address: {e.__class__.__name__}')         
        
        return
         
    
    
        
    def delay(self):
        time.sleep(50000)  # Adding a delay to ensure the page loads before further actions


if __name__ == "__main__":
    # Create an instance of the class
    booking = BookingAutomation()

    # Call the methods in the desired order
    booking.load_page()
    
    for i in tqdm(range(20)):
        time.sleep(1)
    booking.make_reservation()
    booking.change_location()
    booking.type_location()
    booking.choose_floor()
    booking.choose_starting_time()
    booking.choose_finish_time()
    booking.search()
    booking.filters()
    booking.book_seat() 
    booking.delay()