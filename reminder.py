import schedule
import time
from notification import show_notification
from jobs.weeklymeet import send_weeklymail
 
# Functions setup
def weekly_mail():
    show_notification(
        title = 'Weekly Mail',
        message = 'You have to send the weekly mail',
        callback = send_weeklymail
    )
 

schedule.every(2).days.do(weekly_mail)
 

def start():
    weekly_mail()