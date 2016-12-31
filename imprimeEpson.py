import os, sys
import re
import win32print
#printer_name = "\\\ARTEMIS\ArgoxPrd" #Win32print.GetDefaultPrinter () #'\\\MORGANA\Epson LX-300+'

def substituiEscP(naString):
  naString=re.sub(r"\[\[",(chr(27)+'W'+'1'),naString) #Largura dupla
  naString=re.sub(r"\]\]",(chr(27)+'W'+'0'),naString) #Cancela largura dupla
  naString=re.sub(r"\>\>",(chr(27)+'E'),naString) #Negrito
  naString=re.sub(r"\<\<",(chr(27)+'F'),naString) #Cancela negrito

  return naString
  
def imprime(impressora, texto):

  texto=substituiEscP(texto)
  if sys.version_info >= (3,):
    raw_data = bytes (texto, "utf-8")
  else:
    raw_data = texto
  win32print.WritePrinter(impressora,raw_data)

#Espera dois argumentos: nome da impressora e nome do arquivo a imprimir (formato PPLA)  
if len(sys.argv) == 3:  
  printer_name=sys.argv[1]
  file_name=sys.argv[2]
else:
   print "Imprime arquivo texto em impressora EPSON"
   print "Uso:"
   print "imprimeEpson.py <Impressora> <Arquivo>"
   print ""
   sys.exit(0)
   
print "Arquivo: %s Impressora: >>%s<<" % (file_name, printer_name)
hPrinter = win32print.OpenPrinter (printer_name)
try:
  hJob = win32print.StartDocPrinter (hPrinter, 1, ("ETIQUETA", None, "RAW"))
  try:
    with open(file_name) as f:
      lines = f.readlines()
    win32print.StartPagePrinter (hPrinter)
    imprime(hPrinter,chr(13)+"") #Volta o carro pro inicio da linha
    for line in lines:
      imprime(hPrinter,line)
    imprime(hPrinter,""+chr(12)) #Pula pagina (form feed)
    win32print.EndPagePrinter (hPrinter)
  finally:
    win32print.EndDocPrinter (hPrinter)
finally:
  win32print.ClosePrinter (hPrinter)
