import custlibs

while True:
    #usr = custlibs.stt()
    usr = input("Enter text intent: ") 
    intent = custlibs.intentret(usr)
    if intent == 'music':
        custlibs.playsongyt(usr)
    elif intent == 'change song':
        custlibs.changesongyt(usr)
    elif intent == 'timer':
        custlibs.timer(usr)
    elif intent == 'date':
        custlibs.dt()
    elif intent == 'time':
        custlibs.tm()
    elif intent == 'search':
        custlibs.google_search(usr)
        