import schedule
from typing import Callable
import time
import logging
import os
from datetime import datetime
from lib.paths import cron_check_file_path



class Cron():
    
    def __init__(self) -> None:
        
        self.today = datetime.now()
        self.cron_path = cron_check_file_path
        # Ensure the cron check file exists
        if not os.path.exists(self.cron_path):
            with open(self.cron_path, 'w') as f:
                f.write('1970-01-01 00:00:00\n')
                f.close()
    
    
    
    def _recordRun(self):
    
        # Generate the last run date & time
        
        now = datetime.now()
        last_run_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        # Save to file
        with open(self.cron_path, 'w') as f:
            f.write(f'{last_run_datetime}\n')
    
    def runChecker(self, task_time):
          
        if os.path.exists(self.cron_path):
            
            with open(self.cron_path, 'r') as file:
                
                # Obtain from file
                last_run_date_str, last_run_time_str = file.read().split()
                
                # Convert to datetime
                last_run_date = datetime.strptime(last_run_date_str, '%Y-%m-%d').date()
                last_run_time = datetime.strptime(last_run_time_str, '%H:%M:%S').time().strftime("%H:%M")
                
                print(last_run_time, last_run_date)
                
            
            
            # If last time run was today after the trigger time then it was run.
            if last_run_date == self.today.date() and last_run_time >= task_time:
                
                return True
            
            # If not it wasn't and must be run
            else:
                return False    
            
            


    def cron(self, job : Callable):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        def job_with_logging():
            if not self.runChecker(datetime.now().time()):
                logger.info('Executing scheduled task...')
                job()
                self._recordRun()
                logger.info('Task execution completed.')
            else:
                logger.info('Scheduled task already run today.')
        
        task_times = ['00:00','09:15','09:30', '09:05', '08:50', '']
        
        for taskTime in task_times:
            schedule.every().tuesday.at(taskTime).do(job_with_logging)
            schedule.every().thursday.at(taskTime).do(job_with_logging)
                
        
        minutes = 60
        
        while True:
            
            last_log_time = time.time()

            
            if time.time() - last_log_time >= minutes * 60:
                logger.info('Cron mode active, checking for scheduled tasks...')
                last_log_time = time.time()
            schedule.run_pending()
            time.sleep(5)