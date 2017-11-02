import sys
import telnetlib

HOST = "192.168.1.254"
PORT = "23"
user = "lutron"
password = "integration"

class LutronDevice:


	session = None

	def __init__(self):
	    connection = False
	    self.session = telnetlib.Telnet(HOST, PORT)
	    while connection is False:
	        print 'Attempting to connect to Lutron Hub'
	        self.session.read_until("login:")
	        self.session.write('lutron\r\n')
	        self.session.read_until("password")
	        self.session.write('integration\r\n')
	        prompt = self.session.read_until('GNET')
	        connection = True
	    print "Successfully Logged in to Lutron Hub"

	def set_power_level(self,device_id,state):
		"""
		Return the status of a device
		:param session: telnetlib.Telnet authenticated session
		:return:
		"""
		if isinstance(device_id, int):
		    device_id = str(device_id)
		print "Getting Status for device_id={}".format(device_id)
		self.session.write('#OUTPUT,{},1,{}\r\n'.format(device_id,state))

# def main():
# 	light = LutronDevice()
# 	light.set_power_level(2,100)

# if __name__ == "__main__":
# 	main()