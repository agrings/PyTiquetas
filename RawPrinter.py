import os, sys
import platform

if "Windows" in platform.platform():
  import win32print #Window$
else:
  import cups #Linux: Pycups (https://pypi.python.org/pypi/pycups/)

class RawPrinter():

    def __init__(self, printer_name=None):
       if printer_name is None:
         self.printer_name = win32print.GetDefaultPrinter()
       else:
         self.printer_name= printer_name
       self.hPrinter = win32print.OpenPrinter (self.printer_name)
       
    def  printerList(self):
       names=[]
       for (a,b,name,d) in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL+
                                            win32print.PRINTER_ENUM_CONNECTIONS):
         names.append(name)
       return names
       
    def printLineLF(self, texto):
       if sys.version_info >= (3,):
         raw_data = bytes (texto+"\n", "utf-8")
       else:
         raw_data = texto+"\n"
       win32print.WritePrinter(self.printer,raw_data)
 
    def printLine(self, texto):
       #verifica versao do Python (usa utf-8 se >= 3)
       raw_data = bytes (texto, "utf-8") if sys.version_info >= (3,) else texto
       win32print.WritePrinter(self.printer,raw_data)
  
    def __del__(self):
       win32print.ClosePrinter(self.hPrinter)
       #print "Fechei o barraco"
       
    def printDoc(self,file_name):  
       hPrinter = self.hPrinter
       try:
         hJob = win32print.StartDocPrinter (hPrinter, 1, (file_name, None, "RAW"))
         try:
           with open(file_name) as f:
             lines = f.readlines()
           win32print.StartPagePrinter (hPrinter)
           for line in lines:
             self.printLine(hPrinter,line)
           win32print.EndPagePrinter (hPrinter)
         finally:
           win32print.EndDocPrinter (hPrinter)
       except:
         print "Deu merda"
  

if __name__ == "__main__":
  rp=RawPrinter()
  print rp.printerList()
  print "Estou usando: %s" %(rp.printer_name)
  #rp.doPrint("Isto eh um teste")
  

