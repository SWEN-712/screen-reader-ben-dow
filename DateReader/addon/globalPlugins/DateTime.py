import globalPluginHandler
import datetime
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    
    abbreviatedDate = False
    militaryTime = False

    def getDate(self):
        if self.abbreviatedDate:
            return datetime.datetime.now().strftime( "%m / %d / %Y")
        else:
            return datetime.datetime.now().strftime("%B, %d %Y")

    def getTime(self):
        if self.militaryTime:
            return datetime.datetime.now().strftime("%H %M")
        else:
            return datetime.datetime.now().strftime("%I %M %p")

    def script_DateTime(self, gesture):
        ui.message("It is " + self.getDate() + " at " + self.getTime())

    def script_Date(self, gestrue):
        ui.message(self.getDate())

    def script_Time(self, gesture):
        ui.message(self.getTime())

    
    def script_DateStyle(self,gesture):
        self.abbreviatedDate = not self.abbreviatedDate
        if self.abbreviatedDate:
            ui.message("Abbreviated Date")
        else:
            ui.message("Full Date")

    def script_TimeStyle(self, gesture):
        self.militaryTime = not self.militaryTime
        if self.militaryTime:
            ui.message("24 Hour Time")
        else:
            ui.message("12 Hour Time")


    __gestures={
        "kb:NVDA+h": "DateTime",
        "kb:NVDA+d": "Date",
        "kb:NVDA+a": "Time",
        "kb:NVDA+x": "DateStyle",
        "kb:NVDA+alt+x": "TimeStyle"
    }
