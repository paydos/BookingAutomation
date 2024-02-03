import os

log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log', 'BookingAutomation.log')
requirements_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'requirements.txt')
install_log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log', 'Installation.log')
parameters_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'parameters', 'params.py')
cron_check_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'parameters', 'cron_checker.txt')


log_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log')
scripts_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'scripts')
parameters_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'parameters')
