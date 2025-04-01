import schedule
import time


def job1():
    print("Job 1: Running the first scheduled task.")

def job2():
    print("Job 2: Running the second scheduled task.")

def job3():
    print("Job 3: Running the third scheduled task.")


def schedule_jobs():
    
    schedule.every(2).seconds.do(job1)
    
  
    schedule.every(1).minute.do(job2)
    
 
    schedule.every().day.at("09:00").do(job3)


def run_scheduler():
    while True:
        schedule.run_pending()  
        time.sleep(1)  


if __name__ == "__main__":
    schedule_jobs()
    print("Scheduler is running. Press Ctrl+C to stop.")
    run_scheduler()
