#Atlantis
import random
import hub

app = None

shark = False

#called by main
def run(a):
    global app
    app = a
    if (app.has_item('Oxygen Tank')):
        app.update_console('You put on your oxygen tank and admire the vibrant blue water and magestic city.\n')
        start()
    else:
        app.update_console('You can\'t survive this world unless you have an oxygen tank', tag='r')
        hub.run(app)
    

def start():
    pass