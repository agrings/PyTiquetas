import os, sys
import re
from RawPrinter import RawPrinter


class EpsonLx350Printer(RawPrinter):

  def __init__(self, printer_name=None):
    RawPrinter.__init__(self,printer_name)
  
  def substituiEscP(self, naString):
    naString=re.sub(r"\[\[",(chr(27)+'W'+'1'),naString) #Largura dupla
    naString=re.sub(r"\]\]",(chr(27)+'W'+'0'),naString) #Cancela largura dupla
    naString=re.sub(r"\>\>",(chr(27)+'E'),naString) #Negrito
    naString=re.sub(r"\<\<",(chr(27)+'F'),naString) #Cancela negrito
    return naString
  
  def printLine(self, texto):
    texto=self.substituiEscP(texto)
    super(self.__class__,self).printLine(texto)

  
if __name__ == "__main__":
  #Espera dois argumentos: nome da impressora e nome do arquivo a imprimir (formato PPLA)  
  if len(sys.argv) == 3:  
    printer_name=sys.argv[1]
    file_name=sys.argv[2]
    rp=EpsonLx350Printer(printer_name)
    rp.printDoc(file_name)
  else:
     print "Imprime arquivo texto em impressora EPSON"
     print "Uso:"
     print "imprimeEpson.py <Impressora> <Arquivo>"
     print ""
     rp=EpsonLx350Printer()
     print "Impressoras disponiveis:"
     for printer in rp.printerList():
        print printer
     sys.exit(0)
   
  
