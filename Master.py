from threading import Thread
from User import User
import time,threading

class Master(Thread):
	def __init__(self):
		super(Master, self).__init__()
		self.daemon = True
		self.flag=True
        
	def acc_flag(self):
		return self.flag
			
	def set_flag(self,flag):
		self.flag=flag
	
	def run(self):
		while self.flag:
			self.spawn_user()
		self.kill_users()
		return self.users

	def spawn_user(self):
		user=User(self)
		user.start()
		
	def kill_users(self):
		print "kill users called"
		users=threading.enumerate()[2:]
		for i in threading.enumerate()[2:]:
				i.die()
		print "Server died",users
		
