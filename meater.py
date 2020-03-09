from bluepy import btle
import time
__all__ = ['MeaterProbe']
 
class MeaterProbe:
   def __init__(self, addr):
      self._addr = addr
      self.connect()
      self.update()
       
   @staticmethod
   def bytesToInt(byte0, byte1):
      return byte1*256+byte0

   @staticmethod
   def convertAmbient(array): 
      tip = MeaterProbe.bytesToInt(array[0], array[1])
      ra  = MeaterProbe.bytesToInt(array[2], array[3])
      oa  = MeaterProbe.bytesToInt(array[4], array[5])
      return int(tip+(max(0,((((ra-min(48,oa))*16)*589))/1487)))
      
   @staticmethod
   def toCelsius(value):
      return (float(value)+8.0)/16.0

   @staticmethod
   def toFahrenheit(value):
      return ((MeaterProbe.toCelsius(value)*9)/5)+32.0

   def getTip(self):
      return self._tip

   def getTipF(self):
      return MeaterProbe.toFahrenheit(self._tip)

   def getTipC(self):
      return MeaterProbe.toCelsius(self._tip)

   def getAmbientF(self):
      return MeaterProbe.toFahrenheit(self._ambient)

   def getAmbient(self):
      return self._ambient

   def getAmbientC(self):
      return MeaterProbe.toCelsius(self._ambient)

   def getBattery(self):
      return self._battery

   def getAddress(self):
      return self._addr

   def getID(self):
      return self._id

   def getFirmware(self):
      return self._firmware

   def connect(self):
      self._dev = btle.Peripheral(self._addr)

   def readCharacteristic(self, c):
      return bytearray(self._dev.readCharacteristic(c))

   def update(self):
      tempBytes = self.readCharacteristic(31)
      batteryBytes = self.readCharacteristic(35)
      self._tip = MeaterProbe.bytesToInt(tempBytes[0], tempBytes[1])
      self._ambient = MeaterProbe.convertAmbient(tempBytes)
      self._battery = MeaterProbe.bytesToInt(batteryBytes[0], batteryBytes[1])*10
      (self._firmware, self._id) = str(self.readCharacteristic(22)).split("_")
      self._lastUpdate = time.time()

   def __str__(self):
       return "%s %s probe: %s tip: %fF/%fC ambient: %fF/%fC battery: %d%% age: %ds" % (self.getAddress(), self.getFirmware(), self.getID(), self.getTipF(), self.getTipC(), self.getAmbientF(), self.getAmbientC(), self.getBattery(), time.time() - self._lastUpdate)
