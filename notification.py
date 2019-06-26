from win10toast import ToastNotifier
import praw


notification = ToastNotifier()
information = []
#Reading info.txt
read = open("info.txt", "r")
line = read.readlines()
for info in line:
    information.append(info)
#Storing info into strings
id = information[2].replace('\n', '')
secret = information[3].replace('\n', '')
username = information[0].replace('\n', '')
password = information[1].replace('\n', '')
#Logging in
reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=password,
                     user_agent='modules bot',
                     username=username)

notification.show_toast("Congratulations!", "This notification means you have correctly installed the notification module")

for message in reddit.inbox.stream():
    if message.was_comment:
        notification.show_toast("Comment from " + str(message.author), str(message.body), duration=10)
    else:
        notification.show_toast("Message from " + str(message.author), str(message.subject) + "\n" + "\n" + str(message.body), duration=10)