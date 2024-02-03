import subprocess
import sys
import logging
import getpass
import os

from lib.paths import requirements_file_path, parameters_file_path

class AutoInstaller:
    """
    AutoInstaller class is responsible for installing the necessary dependencies, 
    setting up the application to run at startup, and managing the parameters for the booking.
    """
    def __init__(self):
        """
        Initializes the AutoInstaller class with the necessary attributes.
        """
        self.requirements_file = requirements_file_path
        self.logger = logging.getLogger(__name__)
        
        self.USER_NAME = getpass.getuser()
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'scripts')

    def install(self):
        """
        This method installs the necessary dependencies from the requirements file.
        It does not return anything.
        """
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', self.requirements_file])
        
    def add_to_startup(self):
        """
        This method adds the application to the system startup.
        It does not return anything.
        """
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

    def parameters(self, **kwargs):
        """
        This method sets the parameters for the booking.
        It takes in keyword arguments for location, floor, monitor, and heightdesk.
        It does not return anything.
        """
        if not kwargs.get("location") or not kwargs.get("floor"):
            raise ValueError("Both location and floor must be provided.")
        with open(parameters_file_path, 'w') as params_file:
            params_file.write(f'location="{kwargs["location"]}"\n')
            params_file.write(f'floor={kwargs["floor"]}\n')
            params_file.write(f'monitor={kwargs["monitor"]}\n')
            params_file.write(f'heightdesk={kwargs["heightdesk"]}\n')
    
    def remove(self, arg):
        """
        This method removes the application from the system startup and deletes all related files.
        It takes in a boolean argument to determine whether to remove the files.
        It does not return anything.
        """
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
        """
        This method reinstalls the application.
        It takes in a boolean argument to determine whether to reinstall the application.
        It does not return anything.
        """
        if reinstall:
            try:
                os.remove(os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\BookingAutomation.vbs'))
                os.remove(os.path.join(self.file_path, 'BookingAutomation.bat'))
            except Exception as e:
                self.logger.error('Failed to remove reinstall the BookingAutomation service: ' + str(e.__class__.__name__))
    
    @staticmethod
    def upgrade():
        """
        This method upgrades the application to the latest version.
        It does not return anything.
        """
        os.system('git fetch origin')
        os.system('git reset --hard origin/main')
        os.system('git clean -fd')
        print("Update successful")
        sys.exit(0)
