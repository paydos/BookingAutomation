from lib.setup import AutoInstaller
from lib.paths import install_log_path, log_folder, scripts_folder

import logging
import os




if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    logging.info('Log folder created at {}'.format(log_folder))
else:
    logging.info('Log folder already exists at {}'.format(log_folder))

if not os.path.exists(scripts_folder):
    os.makedirs(scripts_folder)
    logging.info('Scripts folder created at {}'.format(scripts_folder))
else:
    logging.info('Scripts folder already exists at {}'.format(scripts_folder))



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

