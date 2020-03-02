import webbrowser
import schedule


def myinfo():
    print("I am Deepak.")
    # webbrowser.open('http://net-informations.com', new=2)
    # webbrowser.open('www.google.co.in', new=2)


schedule.every(5).seconds.do(myinfo)

flag = True
while flag == True:
    schedule.run_pending()

