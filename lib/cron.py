import schedule
from typing import Callable
import time
import logging


def cron(job : Callable):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    def job_with_logging():
        logger.info('Executing scheduled task...')
        job()
        logger.info('Task execution completed.')

    schedule.every().tuesday.at("00:00").do(job_with_logging)
    schedule.every().tuesday.at("09:00").do(job_with_logging)
    schedule.every().thursday.at("00:00").do(job_with_logging)
    schedule.every().thursday.at("09:00").do(job_with_logging)

    minutes = 60
    while True:
        last_log_time = time.time()

        if time.time() - last_log_time >= minutes * 60:
            logger.info('Cron mode active, checking for scheduled tasks...')
            last_log_time = time.time()
        schedule.run_pending()
        time.sleep(10)