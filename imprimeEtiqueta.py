import os, sys
import re
import win32print
#printer_name = "\\\ARTEMIS\ArgoxPrd" #Win32print.GetDefaultPrinter () #'\\\MORGANA\Epson LX-300+'

def substituiEscP(naString):
  naString=re.sub(r"\[\[",(chr(27)+'w'),naString)
  naString=re.sub(r"\]\]",(chr(27)+'w'),naString)
  
def imprime(impressora, texto):
  if sys.version_info >= (3,):
    raw_data = bytes (texto+"\n", "utf-8")
  else:
    raw_data = texto+"\n"
  win32print.WritePrinter(impressora,raw_data)

#Espera dois argumentos: nome da impressora e nome do arquivo a imprimir (formato PPLA)  
if len(sys.argv) == 3:  
  printer_name=sys.argv[1]
  file_name=sys.argv[2]
else:
  printer_name="\\\ARTEMIS\ArgoxPrd"
  file_name='etiqueta.txt'

print "Arquivo: %s Impressora: >>%s<<" % (file_name, printer_name)
hPrinter = win32print.OpenPrinter (printer_name)
try:
  hJob = win32print.StartDocPrinter (hPrinter, 1, ("ETIQUETA", None, "RAW"))
  try:
    with open(file_name) as f:
      lines = f.readlines()
    win32print.StartPagePrinter (hPrinter)
    for line in lines:
      imprime(hPrinter,line)
    win32print.EndPagePrinter (hPrinter)
  finally:
    win32print.EndDocPrinter (hPrinter)
finally:
  win32print.ClosePrinter (hPrinter)
