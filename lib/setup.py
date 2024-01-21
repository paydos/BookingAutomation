import subprocess
import sys
import logging
import getpass
import os



class AutoInstaller:
    def __init__(self, requirements_file):
        self.requirements_file = requirements_file
        self.logger = logging.getLogger(__name__)
        
        self.USER_NAME = getpass.getuser()
        self.file_path= ""

        
        

    def install(self):
        self.logger.info('Starting module installation/check process...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', self.requirements_file])
        self.logger.info('Installation/check completed successfully.')
        

    def add_to_startup(self):
        try:
            if self.file_path == "":
                self.file_path = os.path.dirname(os.path.realpath(__file__))
                print(self.file_path)
            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % self.USER_NAME
            self.logger.info('Adding BookingAutomation to run on startup')
            with open(bat_path + '\\' + "BookingAutomation.bat", "w+") as bat_file:
                bat_file.write(r'python "%s"' % self.file_path)
            self.logger.info('Script succesfully atttached to boot.')
        except Exception as e:
            self.logger.error('Failed to add script to startup: ' + str(e.__class__.__name__))
        
installer = AutoInstaller('requirements.txt')
installer.install()
installer.add_to_startup()