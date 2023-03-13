#
# Example from https://gist.github.com/iverasp/9349dffa42aeffb32e48a0868edfa32d
#

from PySide6.QtWidgets import QWidget, QGridLayout
import pyqtgraph as pg
import datetime
import time

def timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%H:%M") for value in values]

    
class TimeSeriesPlotWidget(QWidget):
    def __init__(self, parent=None, title="Example Plot", labels={'left':"Reading / mV"}):
        QWidget.__init__(self, parent)
        self.plot = pg.PlotWidget(
            title=title,
            labels=labels,
            axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        )
        self.plot.setXRange(timestamp(), timestamp() + 100)
        self.plot.showGrid(x=True, y=True)
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.plot, 0, 0)

        self.plotCurve = self.plot.plot(pen='y')

        self.plotData = {'x': [], 'y': []}

    def updatePlot(self, newValue):
        self.plotData['y'].append(newValue)
        self.plotData['x'].append(timestamp())
        self.plotCurve.setData(self.plotData['x'], self.plotData['y'])
