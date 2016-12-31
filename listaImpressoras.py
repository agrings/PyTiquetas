import os, sys
import win32print


def imprime(impressora, texto):
  if sys.version_info >= (3,):
    raw_data = bytes (texto+"\n", "utf-8")
  else:
    raw_data = texto+"\n"
  win32print.WritePrinter(impressora,raw_data)
  
def listaImpressoras():
  print "Lista de impressoras"
  for (a,b,name,d) in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL+
                                            win32print.PRINTER_ENUM_CONNECTIONS):
    print(name)


listaImpressoras()
