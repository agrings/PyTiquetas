import cups

conn = cups.Connection ()

#Obtem lista de impressoras
printers = conn.getPrinters ()
for printer in printers:
    print(printer,"::",printers[printer]["device-uri"])

#Substitua pelo nome de sua impressora
printer_name = "Epson-LX-300+"
conn.printFile(printer_name, 'arquivo_teste.raw', 'Nome do Job', {})
