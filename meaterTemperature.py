
__all__ = ['Temperature']
 
class Temperature:
   def __init__(self, tempBytes):
      self._tip = Temperature.bytesToInt(tempBytes[0], tempBytes[1])
      self._ambient = Temperature.convertAmbient(tempBytes)
       
   @staticmethod
   def bytesToInt(byte0, byte1):
      return byte1*256+byte0

   @staticmethod
   def convertAmbient(array): 
      tip = Temperature.bytesToInt(array[0], array[1])
      ra  = Temperature.bytesToInt(array[2], array[3])
      oa  = Temperature.bytesToInt(array[4], array[5])
      return int(tip+(max(0,((((ra-min(48,oa))*16)*589))/1487)))
      
   @staticmethod
   def toCelsius(value):
      return (float(value)+8.0)/16.0

   @staticmethod
   def toFahrenheit(value):
      return ((Temperature.toCelsius(value)*9)/5)+32.0

   def getTip(self):
      return self._tip

   def getTipF(self):
      return Temperature.toFahrenheit(self._tip)

   def getTipC(self):
      return Temperature.toCelsius(self._tip)

   def getAmbientF(self):
      return Temperature.toFahrenheit(self._ambient)

   def getAmbient(self):
      return self._ambient

   def getAmbientC(self):
      return Temperature.toCelsius(self._ambient)

