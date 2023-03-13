from widgets import TimeSeriesPlotWidget

devices = [ "GPS1",
            "GPS2",
            "GYRO",
            "Temp",
            "IVME",
            "HIZ",
            "NEM",
            "TEZYIQ",
            "HATALAR",
            "SAAT" ]

class Instrument:
    def __init__(self, name, maxnum = 100):
        self.numbers = []
        self.name = name
        self.maxnum = maxnum
        
    def add(self, newnumber):
        if len(self.numbers) >= self.maxnum:
            self.numbers= self.numbers[1:]
        self.numbers.append(newnumber)
        print(self.name, newnumber)

class Satellite:
    def __init__(self, name, parent=None):
        self.name = name
        self.plots = {
            "Temp": TimeSeriesPlotWidget(parent=parent.frame1, title="Temperature"),
            "HIZ": TimeSeriesPlotWidget(parent=parent.frame2, title="Speed"),
            "IVME": TimeSeriesPlotWidget( title="Acceleration"),
            "NEM": TimeSeriesPlotWidget( title="Humidity"),
            "GPS1": TimeSeriesPlotWidget( title="Gps1"),
            "GPS2": TimeSeriesPlotWidget( title="Gps2")
        }
        
        self.instruments = {
            "GPS1" : Instrument("GPS1"),
            "GPS2" : Instrument("GPS2"),
            "GYRO" : Instrument("GYRO"),
            "Temp" : Instrument("Temp"),
            "IVME" : Instrument("IVME"),
            "HIZ" : Instrument("HIZ"),
            "NEM" : Instrument("NEM"),
            "TEZYIQ" : Instrument("TEZYIQ"),
            "HATALAR" : Instrument("HATALAR"),
            "SAAT" : Instrument("SAAT")
        }

    def new_data(self, json_data):
        for device in devices:
            if device in ["GYRO", "TEZYIQ", "HATALAR", "SAAT"]:
                #burada coklu veri var. ona gore isleyecegiz her birini ayri ayri
                pass
            else:
                self.instruments[device].add(json_data[device])
                self.plots[device].updatePlot(json_data[device])
