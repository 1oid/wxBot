from utils.spider.mytoken import worker
from config import WORK_SLEEP
import schedule
import time

if __name__ == '__main__':
    worker()
    schedule.every(WORK_SLEEP).seconds.do(worker)

    # 定时
    while True:
        try:
            schedule.run_pending()
            time.sleep(WORK_SLEEP)
        except Exception as e:
            with open("err.log", 'a') as f:
                f.write("{}\n".format(e))
