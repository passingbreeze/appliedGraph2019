
from pylab import *

def click(event):
   """If the left mouse button is pressed: draw a little square. """
   tb = get_current_fig_manager().toolbar
   if event.button==1 and event.inaxes and tb.mode == '':
       x,y = event.xdata,event.ydata
       print("Position= ", x,y)
       plot([x],[y],'rs')
       draw()

plot((arange(100)/99.0)**3)
gca().set_autoscale_on(False)
connect('button_press_event',click)
show()
