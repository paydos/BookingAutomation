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
        options.add_argument("--user-data-dir=/home/ruiz/.config/google-chrome/") # Change the path according to your system
        options.add_argument("--profile-directory=Profile 1") # Change to Profile 1 for testing 
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
        time.sleep(1)

    def type_location(self):
        # Type in location
        self.logger.info('Typing in location...')
        address = 'Madrid, Castellana 85'
        address_box = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/input')
        address_box.send_keys(address)
        time.sleep(1)
        address_box.send_keys(Keys.ENTER)
        time.sleep(2)


    def choose_floor(self):
        # Choose floor
        time.sleep(1.5)
        self.logger.info('Choosing floor...')
        self.floorNumber = '05'
        floor = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[2]/div/div/a/span[1]')
        floor.click()
        time.sleep(1)

        floor_box = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/input')
        floor_box.send_keys(self.floorNumber)
        time.sleep(1.5)
        floor_box.send_keys(Keys.ENTER)
        time.sleep(0.2)

    

    def choose_starting_time(self):
        # Choose starting date
        self.logger.info(f'Start time default to {self.start_time} ')
        start_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[3]/div[2]/div[1]/input')
        start_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
        time.sleep(0.1)
        start_time_box.send_keys('2024-01-19 00:00:00')
        time.sleep(0.5)

    def choose_finish_time(self):
        # Choose finish date
        self.logger.info(f'Finish time default to {self.finish_time}')
        finish_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[4]/div/div[1]/input')
        finish_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
        time.sleep(0.1)
        finish_time_box.send_keys('2024-01-19 01:00:00')  # Insert the finish time
        time.sleep(0.5)
        
    def init_search(self):
        self.logger.info('Searching...')
        time.sleep(0.7)
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[2]/div/div[2]/div/div/button')
        search.click()
        time.sleep(0.5)
        
    def filters(self):
        self.logger.info(f'Applying filters\n   - High Resolution monitor: {self.HighResolutionMonitor}\n   - Adjustable Height Desk: {self.AdjustableHeightDesk}')
        
        # Check if High Resolution Monitor is selected
        if self.HighResolutionMonitor:
            try:
                time.sleep(4)
                self.logger.info('Selecting High Resolution Monitor')
                
                # Find the monitor element
                monitor = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[1]/iwms-wsd-reservable-filter/div/div[4]/ul/li[2]/div/label')
                
                # Check if the monitor text matches 'High Resolution Monitor'
                if monitor.text == 'High Resolution Monitor':
                    # Click the monitor element
                    monitor.click()
                    time.sleep(1)
                    self.logger.info('High Resolution Monitor selected')
                    
                # Check if the monitor text matches 'Adjustable Height Desk' in case order is inverted. Check if option is chosen.
                elif monitor.text == 'Adjustable Height Desk' and self.AdjustableHeightDesk:
                    
                    monitor.click()
                    time.sleep(1)
                    
                    self.logger.info('Adjustable Height Desk selected')
                    
                else:
                    # Log an error if the selected element does not correspond to High Resolution Monitor nor Adjustable Height Desk
                    self.logger.error('The selected element does not correspond to High Resolution Monitor')
                
            except Exception as e: # noqa: E722
                
                self.logger.warning('Unable to select High Resolution Monitor: Probably not available')
            
        if self.AdjustableHeightDesk:
            try:
                time.sleep(4)
                self.logger.info('Selecting Adjustable Height Desk')
                time.sleep(1)
                desk = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[1]/iwms-wsd-reservable-filter/div/div[4]/ul/li[1]/div/label')
                if desk.text == 'Adjustable Height Desk':
                    desk.click()
                    time.sleep(1)
                    self.logger.info('Adjustable Height Desk selected')
                elif desk.text == 'High Resolution Monitor' and self.HighResolutionMonitor:
                    desk.click()
                    time.sleep(1)
                    self.logger.info('High Resolution Monitor selected')
                else:
                    self.logger.warning('The selected element does not correspond to Adjustable Height Desk nor High Resolution Monitor')
                
            except:  # noqa: E722
                
                self.logger.error('Unable to select Adjustable Height Desk: Probably not available')
        time.sleep(1)
        
        self.logger.info('Applying filters...')
        try:
            
            applyFilters = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[1]/iwms-wsd-reservable-filter/div/div[4]/a')
            applyFilters.click()
            time.sleep(0.1)
            self.logger.info('Filters applied')
            
        except Exception as e:  # noqa: E722
            self.logger.error(f'Unable to apply filters: {e.__class__.__name__}')
        

            
    def search(self):
        time.sleep(2)
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[2]/div/div[2]/div/div/button')
        search_button.click()
        time.sleep(4)

    def book_seat(self):
        
        self._seat_info()
        print("Desk Location: ", self.bookingInfo['Desk Location'])
        print("Floor and Address: ", self.bookingInfo['Floor and Address'])
        
        time.sleep(2)
        
        # Click to add to the "shopping basket"
        try:
            add = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/iwms-wsd-horizontal-card/div/div[3]/div/button')
            add.click()
            time.sleep(5)
            self.logger.info('Added to shopping basket')
        except Exception as e:
            self.logger.error(f'Failed to add to shopping basket: {e.__class__.__name__}')
            
            
        # Click to go to booking screen
        try:
            bookButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]')
            bookButton.click()
            time.sleep(3)
            self.logger.info('Navigated to booking screen')
        except Exception as e:
            self.logger.error(f'Failed to navigate to booking screen: {e.__class__.__name__}')
        
        # Reservation type
        try:
            res_type = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div/sp-page-row/div/div/span/div/div/section/iwms-wsd-reservation/div/div[1]/div[1]/div[2]/form/div[4]/div/div/div/div/div[1]/a')
            res_type.click()
            time.sleep(1)
            self.logger.info('Reservation type selected')
        except Exception as e:
            self.logger.error(f'Failed to select reservation type: {e.__class__.__name__}')
        
        # Choose reservation type: Workspace
        try:
            res_type_box = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/input')
            res_type_box.send_keys('Workspace')
            time.sleep(0.3)
            res_type_box.send_keys(Keys.ENTER)
            time.sleep(0.2)
            self.logger.info('Workspace reservation type entered')
        except Exception as e:
            self.logger.error(f'Failed to enter Workspace reservation type: {e.__class__.__name__}')
        
        # Click book
        try:
            book_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[2]/div/sp-page-row/div/div/span/div/div/section/iwms-wsd-reservation/div/div[2]/div/div[1]/div/div[2]/div/button[1]')
            book_button.click()
            self.logger.info('Book button clicked')
        except Exception as e:
            self.logger.error(f'Failed to click book button: {e.__class__.__name__}')
        


        
    
        
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