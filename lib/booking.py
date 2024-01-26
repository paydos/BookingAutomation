from lib.date import DateCalculator, DateAdapter

from undetected_chromedriver import By
from selenium.webdriver.common.keys import Keys
from parameters.params import location, floor, monitor, heightdesk

import undetected_chromedriver as uc

import logging
import os
import time

class BookingAutomation:
    def __init__(self, day:int):
        
        # Logging
        self.logger = logging.getLogger(__name__)

        
        # Date parameters - Day selector
        self.date = DateCalculator()
        if day == 1:
            self.date = self.date.get_next_tuesday()
        elif day == 3:
            self.date = self.date.get_next_thursday()
        else:
            raise ValueError()
        
        # Time parameters - Time selector
        self.adapter = DateAdapter(self.date)
        self.start_time = self.adapter.start()
        self.finish_time = self.adapter.finish()    
        
        # Custom Parameters
        self.HighResolutionMonitor = monitor
        self.AdjustableHeightDesk = heightdesk
        self.location = location
        self.floor = floor

        #* TODO: FIX FEATURE TO INDICATE THE USER THE BOOKED PLACE
        #* To do this we could instead of getting the info before booking, do it once it's been booked: Screen's cleaner and could be easier.
        self.bookingInfo = {
            'Desk Location': None,
            'Floor and Address': None
        }

        # Set up chrome profile (Use Default)
        self.logger.info('Creating Google Chrome Driver')
        options = uc.ChromeOptions()
        options.add_argument("--no-first-run")  # Suppress the first run dialog
        options.add_argument("--no-default-browser-check")  # Skip the default browser check
        options.add_argument("--verbose")
        options.add_argument("--headless")
        
        # For Linux - testing
        #options.add_argument("--user-data-dir=/home/ruiz/.config/google-chrome/") # Change the path according to your system
        #options.add_argument("--profile-directory=Profile 1") # Change to Profile 1 for testing 
        
        # For Windows
                
        user_data_dir = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data')
        options.add_argument(f"--user-data-dir={user_data_dir}")  # Path updated to use the current Windows user's profile
        options.add_argument("--profile-directory=Default")  # Change to Profile 1 for testing
        self.driver = uc.Chrome(options=options, version_main=120)

        # Maximize the window
        self.logger.info('Maximizing window...')
        self.driver.maximize_window()

    def load_page(self):
        try:
            # Access the booking webpage (sleep=10 to allow it to properly load)
            self.logger.info('Loading page...')
            self.driver.get('https://support-places.accenture.com/places')
            time.sleep(8)
        except Exception as e:
            self.logger.error(f'Failed to load page: {e.__class__.__name__}')

    def make_reservation(self):
        try:
            # Make a reservation
            self.logger.info('Making a reservation...')
            button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/section[1]/div/div[3]/a[1]')
            button.click()
            time.sleep(4)
        except Exception as e:
            self.logger.error(f'Failed to make reservation: {e.__class__.__name__}')

    def change_location(self):
        try:
            # Change to Castellana
            self.logger.info(f'Changing location to {self.location}...')
            location = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[1]/div/div/div/div[1]/div/a/span[1]')
            location.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error(f'Failed to change location: {e.__class__.__name__}')

    def type_location(self):
        try:
            # Type in location
            self.logger.info('Typing in location...')
            address = self.location
            address_box = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/input')
            address_box.send_keys(address)
            time.sleep(1)
            address_box.send_keys(Keys.ENTER)
            time.sleep(2)
        except Exception as e:
            self.logger.error(f'Failed to type location: {e.__class__.__name__}')

    def choose_floor(self):
        try:
            # Choose floor
            time.sleep(1.5)
            self.logger.info(f'Choosing floor {self.floor}...')
            self.floorNumber = self.floor
            floor = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[2]/div/div/a/span[1]')
            floor.click()
            time.sleep(1)

            floor_box = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/input')
            floor_box.send_keys(self.floorNumber)
            time.sleep(1.5)
            floor_box.send_keys(Keys.ENTER)
            time.sleep(1)
        except Exception as e:
            self.logger.error(f'Failed to choose floor: {e.__class__.__name__}')

    def choose_starting_time(self):
        try:
            # Choose starting date
            self.logger.info(f'Start time default to {self.start_time} ')
            start_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[3]/div[2]/div[1]/input')
            start_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
            time.sleep(1)
            start_time_box.send_keys(self.start_time)
            time.sleep(0.5)
        except Exception as e:
            self.logger.error(f'Failed to choose starting time: {e.__class__.__name__}')

    def choose_finish_time(self):
        try:
            # Choose finish date
            self.logger.info(f'Finish time default to {self.finish_time}')
            finish_time_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[1]/div/div/div[2]/div[4]/div/div[1]/input')
            finish_time_box.send_keys(Keys.CONTROL + "a")  # Select all text in the box
            time.sleep(1)
            
            #!! There is a big in the finish_time (Should enter 17:00:00 and persist, yet it enters 10:00:00)
            finish_time_box.send_keys(self.finish_time)  # Insert the finish time
            time.sleep(0.5)
        except Exception as e:
            self.logger.error(f'Failed to choose finish time: {e.__class__.__name__}')
        
    def init_search(self):
        try:
            self.logger.info('Searching...')
            time.sleep(0.7)
            search = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[2]/div/div[2]/div/div/button')
            search.click()
            time.sleep(0.5)
        except Exception as e:
            self.logger.error(f'Failed to initialize search: {e.__class__.__name__}')
        
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
                
                self.logger.warning(f'Unable to select High Resolution Monitor: {e.__class__.__name__} ')
            
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
        try:
            time.sleep(2)
            search_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[1]/iwms-wsd-search-filter/div[3]/div[1]/div/section[2]/div/div[2]/div/div/button')
            search_button.click()
            time.sleep(4)
        except Exception as e:
            self.logger.error(f'Failed to search: {e.__class__.__name__}')

    def book_seat(self):
        
        self._seat_info()
        print("Desk Location: ", self.bookingInfo['Desk Location'])
        print("Floor and Address: ", self.bookingInfo['Floor and Address'])
        
        time.sleep(2)
        
        # Click to add to the "shopping basket"
        try:
            time.sleep(2)
            add = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/iwms-wsd-horizontal-card/div/div[3]/div/button')
            add.click()
            time.sleep(5)
            self.logger.info('Added to shopping basket')
        except Exception as e:
            self.logger.error(f'Failed to add to shopping basket: {e.__class__.__name__}')
            
            
        # Click to go to booking screen
        try:
            self.logger.info('Locating booking screen...')
            time.sleep(3)
            bookButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/sp-page-row/div/div/span/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]')
            bookButton.click()
            time.sleep(3)
            self.logger.info('Navigated to booking screen')
        except Exception as e:
            self.logger.error(f'Failed to navigate to booking screen: {e.__class__.__name__}')
        
        # Reservation type
        try:
            self.logger.info('Clicking on reservation type...')
            time.sleep(4)
            res_type = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[3]/div/sp-page-row/div/div/span/div/div/section/iwms-wsd-reservation/div/div[1]/div[1]/div[2]/form/div[4]/div/div/div/div/div[1]/a')
            res_type.click()
            time.sleep(1)
            self.logger.info('Reservation type selected')
        except Exception as e:
            self.logger.error(f'Failed to select reservation type: {e.__class__.__name__}')
        
        # Choose reservation type: Workspace
        try:
            self.logger.info('Choosing reservation type...')
            res_type_box = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/input')
            res_type_box.send_keys('Workspace')
            time.sleep(0.3)
            res_type_box.send_keys(Keys.ENTER)
            time.sleep(1)
            self.logger.info('Reservation type entered')
        except Exception as e:
            self.logger.error(f'Failed to enter reservation type: {e.__class__.__name__}')
        
        time.sleep(5)
        # Click book
        try:
            book_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div[3]/div/sp-page-row/div/div/span/div/div/section/iwms-wsd-reservation/div/div[2]/div/div[1]/div/div[2]/div/button[1]')
            book_button.click()
            self.logger.info('Book button clicked')
        except Exception as e:
            self.logger.error(f'Failed to click book button: {e.__class__.__name__}') 
        
        time.sleep(2)  # Wait for the booking to process
       
          
    def _seat_info(self):
        
        self.logger.info('Saving desk information...')
        time.sleep(2)
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
         
    def close(self):
        time.sleep(20)
        self.driver.close()
        self.logger.info('Webdriver shut down. The service is now passive.')
    

    
        
    def delay(self):
        time.sleep(2000)  # Adding a delay to ensure the page loads before further actions

