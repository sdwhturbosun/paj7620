import paj7620
import time
g=paj7620.gesture()
g.init()
while True:
	g.print_gesture()
	time.sleep(0.1)