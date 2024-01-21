import subprocess
import sys
import logging
import getpass
import os

from lib.paths import requirements_file_path


class AutoInstaller:
    def __init__(self):
        self.requirements_file = requirements_file_path
        self.logger = logging.getLogger(__name__)
        
        self.USER_NAME = getpass.getuser()
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'scripts')

    def install(self):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', self.requirements_file])
        
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
