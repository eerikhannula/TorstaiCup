import sys
import ac
import acsys

APPNAME = "TorstaiCup"

DRIVERS = ["Pinche", "AroPupu", "TatuEno"]
UI_x = 10
UI_y = 30

timer = 0

currentLapLabel = 0

def acMain(ac_version):

    try:
        appWindow = ac.newApp(APPNAME)
        ac.setSize(appWindow, 200, 600)

        setDriverList(appWindow)
        setLapCount(appWindow)

        ac.log("log started")
        ac.console("log started")

        return APPNAME
    except Exception as e:
        ac.log("error")
        ac.console("error")
        ac.log("Exception: " + e.message)
        ac.console("Exception: " + e.message)
        return APPNAME

def acUpdate(delta_t):
    global timer
    global currentLap
    global currentLapLabel

    timer += delta_t

    if timer > 0.1:
        currentLap = ac.getCarState(0, acsys.CS.LapTime)
        #currentLapValueSeconds = (currentLap / 1000) % 60
		#currentLapValueMinutes = (currentLap // 1000) // 60
        #currentLap += 1
        ac.setText(currentLapLabel, "{:06.3f}".format(currentLap))
        #ac.setText(currentLapLabel, str(currentLap))
    
        timer = 0

def setDriverList(appWindow):
    global UI_x
    global UI_y
    for d in DRIVERS:
        button = ac.addButton(appWindow, d)
        ac.setSize(button, 180, 30)
        ac.setPosition(button, UI_x, UI_y)
        UI_y = UI_y + 30
    return

def setLapCount(appWindow):
    global UI_x
    global UI_y
    global currentLapLabel

    UI_y = UI_y + 30
    currentLapLabel = ac.addLabel(appWindow, "Current: ")
    ac.setPosition(currentLapLabel, UI_x, UI_y)
    UI_y = UI_y + 30
    return