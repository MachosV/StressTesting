from Master import Master
import time,httplib,sys
from threading import Lock

def run():
		start=time.time()
		#self.conn = httplib.HTTPConnection("localhost")
		conn = httplib.HTTPConnection("localhost")
		print "Connected"		
		conn.request('GET', '/index.php',headers={"Connection":" keep-alive"})
		r1 = conn.getresponse()
		r1.read()
		if r1.status!=200:
				r1.status()
		with Lock():
			sys.stdout.flush()
			xronos="{0:.2f}".format(time.time()-start)		
			print "ok",xronos

		
def main():
	master=Master()
	master.start()	
	master.join()
	#run()
	print "Server is dead"	
	return 0

if __name__ == '__main__':
	main()

