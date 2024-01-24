import subprocess
import sys
import logging
import getpass
import os

from lib.paths import requirements_file_path, parameters_file_path

# AutoInstaller class is responsible for installing the necessary dependencies, 
# setting up the application to run at startup, and managing the parameters for the booking.
class AutoInstaller:
    def __init__(self):
        self.requirements_file = requirements_file_path
        self.logger = logging.getLogger(__name__)
        
        self.USER_NAME = getpass.getuser()
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'scripts')

    # This method installs the necessary dependencies from the requirements file.
    def install(self):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', self.requirements_file])
        
    # This method adds the application to the system startup.
    def add_to_startup(self):
        try:
            bat_file_path = os.path.join(self.file_path, 'BookingAutomation.bat')
            vbs_path = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\BookingAutomation.vbs')
            with open(bat_file_path, "w+") as bat_file:
                bat_file.write(r'python "%s"' % os.path.join(os.path.dirname(self.file_path), '__main__.py'))
            
            with open(vbs_path, "w+") as vbs_file:
                vbs_file.write('Set WshShell = CreateObject("WScript.Shell")\n')
                vbs_file.write('WshShell.Run chr(34) & "' + bat_file_path + '" & Chr(34), 0, False\n')
                vbs_file.write('Set WshShell = Nothing\n')
        except Exception as e:
            self.logger.error('Failed to add script to startup: ' + str(e.__class__.__name__))

    # This method sets the parameters for the booking.
    def parameters(self, **kwargs):
        if not kwargs.get("location") or not kwargs.get("floor"):
            raise ValueError("Both location and floor must be provided.")
        with open(parameters_file_path, 'w') as params_file:
            params_file.write(f'location="{kwargs["location"]}"\n')
            params_file.write(f'floor={kwargs["floor"]}\n')
            params_file.write(f'monitor={kwargs["monitor"]}\n')
            params_file.write(f'heightdesk={kwargs["heightdesk"]}\n')
    
    # This method removes the application from the system startup and deletes all related files.
    def remove(self, arg):
        if arg:
            try:
                os.remove(self.requirements_file)
                os.remove(os.path.join(self.file_path, 'BookingAutomation.bat'))
                os.remove(os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\BookingAutomation.vbs'))
                os.remove(os.path.join(os.path.dirname(self.file_path), '__main__.py'))
                self.logger.info('All files removed successfully.')
            except Exception as e:
                self.logger.error('Failed to remove files: ' + str(e.__class__.__name__))
                
    def reinstall(self, reinstall):
        if reinstall:
            try:
                # Remove old VBS
                os.remove(os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\BookingAutomation.vbs'))
                
                # Remove .bat file
                os.remove(os.path.join(self.file_path, 'BookingAutomation.bat'))
                
                # Maybe add a git pull and discard changes?
                # Pull from main, overwrite everything and delete if necessary
                os.system('git fetch origin')
                os.system('git reset --hard origin/main')
                os.system('git clean -fd')

                
            except Exception as e:
                self.logger.error('Failed to remove reinstall the BookingAutomation service: ' + str(e.__class__.__name__))

