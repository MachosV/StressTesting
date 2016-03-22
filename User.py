from threading import Lock,Thread
import time,httplib,sys,threading

class User(Thread):
    def __init__(self,master):
        super(User, self).__init__()
        self._stop = threading.Event()
        self.master=master
        self.daemon = True
        self.dead = False
        self.conn = None
        
    def run(self):
		start=time.time()
		self.conn = httplib.HTTPConnection("localhost")
		print "Connected",self		
		self.conn.request('GET', '/index.php',headers={"Connection":" keep-alive"})
		r1 = self.conn.getresponse()
		r1.read()
		#print r1.status
		if r1.status!=200:
				self.master.set_flag(False)
				self.die()
		with Lock():
			sys.stdout.flush()
			xronos="{0:.2f}".format(time.time()-start)		
			print "ok",xronos
		self.conn.close()
			
	
    def die(self):
		self.conn.close()
		self._stop.set()
