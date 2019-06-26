# RedditNotification
Real time native notification for reddit using windows toast notifications.
# Pre-requisites
* Python 3.6
* Windows 7 or above, and notifications enabled (Through action center or otherwise)
# How to setup
1. Install requirements.txt by using `pip install -r requirements.txt`
2. [Create a bot](https://www.reddit.com/prefs/apps/) on your reddit account if you haven't already. This reddit account should be **the reddit account that you want to monitor notifications**. If you don't know how to create a bot (script) then please Google it.
3. Enter your bot information on the info.txt as prompted. Each information should be seperated by a new line. **Please beware of extra spaces at the end of each line**. **Do not put a new line after the last line**
4. Run the bot using `python notification.py` and you should be good to go. 
# Errors and FAQs.
* I have some sort of error related to PRAW.

It is most likely because you haven't entered your information in correctly. Remember, **beware of extra space and no new line after the last line**. Or your internet connection have some problems.
* Package not found errors

You most likely haven't installed the modules correctly. Please install the modules by going `pip install -r requirements.txt`
* Can't find windows notifications popping up.

You probably disabled the notifications. For Windows 10, go to "Action Center", and enable notifications. 
