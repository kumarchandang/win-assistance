from win10toast_click import ToastNotifier 


def show_notification( title = 'Notification', message = 'Open', callback = ''):
    toaster = ToastNotifier()

    # showcase
    toaster.show_toast(
        title,
        message,
        icon_path=None, # 'icon_path' 
        duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
        callback_on_click=callback # click notification to run function 
    )
