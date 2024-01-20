import subprocess
import sys
import logging



class AutoInstaller:
    def __init__(self, requirements_file):
        self.requirements_file = requirements_file
        self.logger = logging.getLogger(__name__)
        
        

    def install(self):
        self.logger.info('Starting module installation/check process...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', self.requirements_file])
        self.logger.info('Installation/check completed successfully.')
        
installer = AutoInstaller('requirements.txt')
installer.install()