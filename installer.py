from lib.setup import AutoInstaller
from lib.paths import install_log_path
import logging

# Configure logging
logging.basicConfig(filename=install_log_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Create an instance of the AutoInstaller class
installer = AutoInstaller()

# Install required modules
logging.info('Starting installation of required modules.')
installer.install()
logging.info('Installation of required modules completed.')

# Add the application to the system startup
logging.info('Adding application to system startup.')
installer.add_to_startup()
logging.info('Application added to system startup successfully.')
