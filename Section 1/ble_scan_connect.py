from bluepy.btleimport Peripheral, UUID
from bluepy.btleimport Scanner, DefaultDelegate
class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)
	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev:
			print "Discovered device", dev.addr
		elif isNewData:
			print "Received new data from", dev.addr
	def handleNotification(self, cHandle, data):
                print("hahahaha")


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
for dev in devices:
	print "%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi)
	n += 1
	for (adtype, desc, value) in dev.getScanData():
		print "  %s = %s" % (desc, value)
'''
number = input('Enter your device number: ')
print('Device', number)
print(devices[number].addr)
'''

print "Connecting..."
dev = Peripheral('f2:a4:7d:5a:a1:38', 'random')

print "Services..."
for svc in dev.services:
	print str(svc)
try:
        testService = dev.getServiceByUUID(UUID(0xa000))
        for ch in testService.getCharacteristics():
                print str(ch)
        ch = dev.getCharacteristics(uuid=UUID(0xa001))[0]
        while True:
                if(ch.supportsRead()):
                        print(ch.read())

finally:
	dev.disconnect()
