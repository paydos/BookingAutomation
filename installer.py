from lib.setup import AutoInstaller
from lib.paths import install_log_path, log_folder, scripts_folder, parameters_folder

import logging
import argparse
import os


parser = argparse.ArgumentParser(description='This script automates the installation of required modules and adds the application to the system startup.')
parser.add_argument('--location', type=str, required=False, help='Specify the location for the booking. This is a required argument.')
parser.add_argument('--floor', type=int, required=False, help='Specify the preferred floor number for the booking. This is a required argument.')
parser.add_argument('--heightdesk', type=bool, default=False, help='Optional argument. If set to True, it will book an adjustable height desk. Default is False.')
parser.add_argument('--monitor', type=bool, default=False, help='Optional argument. If set to True, it will book a high resolution monitor. Default is False.')
parser.add_argument('--remove', type=bool, default=False, help='Optional argument. If set to True, it will remove the service from startup and delete all related files. Default is False.')
parser.add_argument('--reinstall', type=bool, default=False, help='Optional argument. If set to True, it will reinstall the application. Default is False.')
parser.add_argument('--upgrade', type=bool, default=False, help='Optional argument. If set to True, it will upgrade the application to the latest version. Default is False.')

args = parser.parse_args()

location = args.location
floor = args.floor
remove = args.remove 
monitor = args.monitor
heightdesk = args.heightdesk
reinstall = args.reinstall
upgrade = args.upgrade



# Check if log folder exists
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    logging.info('Log folder created at {}'.format(log_folder))
else:
    logging.info('Log folder already exists at {}'.format(log_folder))

# Configure logging
logging.basicConfig(filename=install_log_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

#* All the mkdirs should be moved as a private method to make it cleaner (No need to have it here)
# Check if the other folders exist
if not os.path.exists(scripts_folder):
    os.makedirs(scripts_folder)
    logging.info('Scripts folder created at {}'.format(scripts_folder))
else:
    logging.info('Scripts folder already exists at {}'.format(scripts_folder))

if not os.path.exists(parameters_folder):
    os.makedirs(parameters_folder)
    logging.info('Parameters folder created at {}'.format(parameters_folder))
else:
    logging.info('Parameters folder already exists at {}'.format(parameters_folder))
    




# Create an instance of the AutoInstaller class
installer = AutoInstaller()

# Check for upgrade
if upgrade:
    installer.upgrade()

# Check if user wants to uninstall
installer.remove(arg=remove)

# Install required modules
logging.info('Starting installation of required modules.')

# Check if user wants to reinstall

# Install otherwise
if reinstall:
    installer.reinstall(reinstall)

installer.install()
    
logging.info('Installation of required modules completed.')

# Add the application to the system startup
logging.info('Adding application to system startup.')
installer.add_to_startup()
logging.info('Application added to system startup successfully.')

logging.info('Setting parameters: location - {}, floor - {}'.format(location, floor))
installer.parameters(location=location, floor=floor, monitor=monitor, heightdesk=heightdesk)
logging.info('Parameters set successfully.')