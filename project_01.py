import pywhatkit

phone_number = "+923246387114"
message = "Hi! this is an automated message sent using python!"

hour = 10     # 24-hour format
minute = 30   # minutes

pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
