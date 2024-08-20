import pywhatkit
pywhatkit.sendwhatmsg_instantly()
num_list = ["+2349082449613", "+234######34", "+2348#####6", "+2348146019577"]
for i in num_list:
    pywhatkit.sendwhatmsg_instantly(i, "This message was sent directly with python")
    print("sent")

# pywhatkitit.sendwhatmsg("+2349082449613", "This was sent with python again", 12, 23)
#