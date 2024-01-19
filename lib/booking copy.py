import time
import undetected_chromedriver as uc
import logging
from tqdm import tqdm

from date import DateCalculator, DateAdapter

class BookingAutomation:
    def __init__(self):
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.bookingInfo = {}

        # Set up chrome profile (Use Default)
        self.logger.info('Creating Google Chrome Driver')
        options = uc.ChromeOptions()
        print('a')
        self.driver = uc.Chrome()
        print('a')
        # Maximize the window
        self.logger.info('Maximizing window...')
        self.driver.maximize_window()
        
    def delay(self):
        time.sleep(50000)  # Adding a delay to ensure the page loads before further actions


if __name__ == "__main__":
    # Create an instance of the class
    booking = BookingAutomation()

    booking.delay()