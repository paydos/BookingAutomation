import time
from undetected_chromedriver import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import logging
from tqdm import tqdm

from date import DateCalculator, DateAdapter

class BookingAutomation:
    def __init__(self):
        # date convention = 2024-01-17 15:30:00
        self.date = DateCalculator.get_next_tuesday()
        self.adapter = DateAdapter(self.date)
        self.start_time = self.adapter.start()
        self.finish_time = self.adapter.finish()    
        
        # Custom Parameters
        self.HighResolutionMonitor = True
        self.AdjustableHeightDesk = False

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.bookingInfo = {}

        # Set up chrome profile (Use Default)
        self.logger.info('Creating Google Chrome Driver')
        options = uc.ChromeOptions()
        options.add_argument("--user-data-dir=/home/ruiz/.config/google-chrome/") # Change the path according to your system
        options.add_argument("--profile-directory=Default") # Change to Profile 1 for testing 
        self.driver = uc.Chrome(options=options)

        # Maximize the window
        self.logger.info('Maximizing window...')
        self.driver.maximize_window()

    def load_page(self):
        # Access the booking webpage (sleep=10 to allow it to properly load)
        self.logger.info('Loading page...')
        self.driver.get('https://support-places.accenture.com/places')
        time.sleep(2)

    def make_reservation(self):
        # Make a reservation
        self.logger.info('Making a reservation...')
        button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/section[1]/div/div[3]/a[1]')
        button.click()
        time.sleep(2)

    def change_location(self):
        # Change to Castellana
        self.logger.info('Changing location to Castellana...')
        location = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div/a/span[1]')
        location.click()
        time.sleep(2)

    def type_location(self):
        # Type in location
        self.logger.info('Typing in location...')
        address = 'Madrid, Castellana 85'
        address_box = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/input')
        address_box.send_keys(address)
        time.sleep(2)

    def click_match(self):
        # Click on match
        self.logger.info('Clicking on address')
        match = self.driver.find_element(By.XPATH, '/html/body/div[6]/ul/li')
        match.click()
        time.sleep(0.5)

    def choose_floor(self):
        # Choose floor
        self.logger.info('Choosing floor...')
        self.floorNumber = '05'
        floor = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[2]/div/div/a/span[1]')
        floor.click()
        time.sleep(0.5)

        floor_box = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/input')
        floor_box.send_keys(self.floorNumber)
        time.sleep(0.5)
        floor_box.send_keys(Keys.ENTER)

    def click_floor_match(self):
        # Click on match
        self.logger.info(f'Clicking on match (Floor {self.floorNumber})...')
        match = self.driver.find_element(By.XPATH, '/html/body/div[7]/ul/li/div')
        match.click()
        time.sleep(0.5)

    def choose_starting_time(self):
        # Choose starting date
        self.logger.info(f'Start time default to {self.start_time} ')
        start_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[3]/div[2]/div[1]/input')
        start_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
        start_time_box.send_keys(Keys.DELETE)  # Delete all selected text
        time.sleep(0.1)
        start_time_box.send_keys(self.start_time)
        time.sleep(0.5)

    def choose_finish_time(self):
        # Choose finish date
        self.logger.info(f'Finish time default to {self.finish_time}')
        finish_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[4]/div/div[1]/input')
        finish_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
        finish_time_box.send_keys(Keys.DELETE)  # Delete all selected text
        time.sleep(0.1)
        finish_time_box.send_keys(self.finish_time)  # Insert the finish time
        time.sleep(0.5)
        
        
    def filters(self):
        self.logger.info(f'Applying filters\n   - High Resolution monitor: {self.HighResolutionMonitor}\n  \
            - Adjustable Height Desk:{self.AdjustableHeightDesk}')
        
        if self.HighResolutionMonitor:
            try:
                self.logger.info('Selecting High Resolution Monitor')
                monitor = self.driver.find_element(By.XPATH, '//*[@id="chk13b0c35f879269d03cc2ca64dabb350d"]')
                monitor.click()
                time.sleep(0.1)
                self.logger.info('High Resolution Montitor selected')
                
            except: # noqa: E722
                
                self.logger.error('Unable to select High Resolution Monitor')
            
        if self.AdjustableHeightDesk:
            try:
                self.logger.info('Selecting Adjustable Height Desk')
                desk = self.driver.find_element(By.XPATH, '//*[@id="chka690c35f879269d03cc2ca64dabb3504"]')
                desk.click()
                time.sleep(0.1)
                self.logger.info('Adjustable Height Desk selected')
                
            except:  # noqa: E722
                
                self.logger.error('Unable to select Adjustable Height Desk')

            
    def search(self):
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[2]/div/div[2]/div/div/button')
        search_button.click()
        time.sleep(0.2)

    def book_seat(self):
        # Find all available seats
        self.logger.info('Finding available seats...')
        try:
            seats = self.driver.find_elements(By.CLASS_NAME, 'horizontal-card__container b r-2x horizontal-card')
        except: # noqa: E722
        # If there are no available seats, log a message and return
            if not seats:
                self.logger.warning('No available seats found!')
                return

        # Otherwise, book the first available seat
        self.logger.info('Booking the first available seat...')
        self.seat = seats[0]
        book_button = self.seat.find_element(By.CLASS_NAME, 'btn btn-default horizontal-card__action-button form-control text-md text-overflow-ellipsis btn-add-card card-btn-secondary')
        book_button.click()
        
    
        
        time.sleep(2)  # Wait for the booking to process
       
       
    
    def _seat_info(self):
                
        self.bookingInfo['Desk Location'] = self.seat.find_element(By.CLASS_NAME, 'horizontal-card__title horizontal-card__truncate-in-two-lines text-md ng-binding ng-scope').text
        self.bookingInfo['Floor and Address'] = self.seat.find_element(By.CLASS_NAME, 'horizontal-card__subtitle text-muted text-overflow-ellipsis ng-binding ng-scope').text
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
    booking.click_match()
    booking.choose_floor()
    booking.click_floor_match()
    booking.choose_starting_time()
    booking.choose_finish_time()
    booking.filters()
    booking.search()
    booking.book_seat()
    booking.delay()