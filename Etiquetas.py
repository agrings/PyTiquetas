import wx
import re  
import os

def preencheCampo(nomeCampo,valorCampo,naString):
  return re.sub(r"\["+nomeCampo+"\]",valorCampo,naString)
  
  
class Etiqueta(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Etiqueta, self).__init__(parent, title = title) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()     
      
   def buttonImprimirClick(self,event):
     with open('modelo.txt') as f:
       lines = f.read()
     lines=preencheCampo("CodigoProduto",self.tcCodigo.GetValue(),lines)
     lines=preencheCampo("NomeProduto",self.tcProduto.GetValue(),lines)
     lines=preencheCampo("Lote",self.tcLote.GetValue(),lines)
     lines=preencheCampo("Validade",self.tcValidade.GetValue(),lines)
     lines=preencheCampo("Copias","{0:0>4}".format(int(self.tcCopias.GetValue())),lines)
     lines=preencheCampo("NomeProduto",self.tcProduto.GetValue(),lines)
     print lines 
     with open('etiqueta.txt',"w") as f:
        f.write(lines)
     os.system('imprimeEtiqueta.py')
   
   def buttonCloseClick(self, event):
        """"""
        self.Close()
      
      
   def InitUI(self): 
       
      panel = wx.Panel(self) 
      sizer = wx.GridBagSizer(0,0)
      #----------------------------------------------------		
      text = wx.StaticText(panel, label = "CODIGO:") 
      sizer.Add(text, pos = (0, 0), flag = wx.ALL, border = 5)
		
      self.tcCodigo = wx.TextCtrl(panel) 
      sizer.Add(self.tcCodigo, pos = (0, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 5) 

      #----------------------------------------------------   
      text1 = wx.StaticText(panel, label = "DESCRICAO:")
      sizer.Add(text1, pos = (1, 0), flag = wx.ALL, border = 5) 
		
      self.tcProduto = wx.TextCtrl(panel,style = wx.TE_MULTILINE) 
      sizer.Add(self.tcProduto, pos = (1,1), span = (1, 3), flag = wx.EXPAND|wx.ALL, border = 5) 
      #----------------------------------------------------   
      text2 = wx.StaticText(panel,label = "LOTE:") 
      sizer.Add(text2, pos = (2, 0), flag = wx.ALL, border = 5) 
		
      self.tcLote = wx.TextCtrl(panel) 
      sizer.Add(self.tcLote, pos = (2,1), flag = wx.ALL, border = 5) 

      #----------------------------------------------------		
      text3 = wx.StaticText(panel,label = "VALIDADE:") 
      sizer.Add(text3, pos = (2, 2), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
		
      self.tcValidade = wx.TextCtrl(panel) 
      sizer.Add(self.tcValidade, pos = (2,3),flag = wx.EXPAND|wx.ALL, border = 5) 
         
      #----------------------------------------------------
      text4 = wx.StaticText(panel, label = "TEMPLATE:")
      sizer.Add(text4, pos = (3, 0), flag = wx.ALL, border = 5) 
		
      tc4 = wx.TextCtrl(panel,style =  wx.TE_MULTILINE) 
      sizer.Add(tc4, pos = (3,1), span = (1,3), flag = wx.EXPAND|wx.ALL, border = 5) 
      sizer.AddGrowableRow(3) 
         
      #----------------------------------------------------
      text5 = wx.StaticText(panel,label = "COPIAS:")
      sizer.Add(text5, pos = (4, 0), flag = wx.ALL, border = 5)

      self.tcCopias = wx.TextCtrl(panel)
      sizer.Add(self.tcCopias, pos = (4,1), flag = wx.ALL, border = 5)
      #----------------------------------------------------
      buttonImprimir = wx.Button(panel, label = "Imprimir") 
      buttonClose = wx.Button(panel, label = "Close" ) 
      buttonImprimir.Bind(wx.EVT_BUTTON, self.buttonImprimirClick)
      buttonClose.Bind(wx.EVT_BUTTON, self.buttonCloseClick)
      sizer.Add(buttonImprimir, pos = (5, 2),flag = wx.ALL, border = 5) 
      sizer.Add(buttonClose, pos = (5, 3), flag = wx.ALL, border = 5)
      panel.SetSizerAndFit(sizer)
    #----------------------------------------------------------------------

		
app = wx.App() 
Etiqueta(None, title = 'IMPRIME ETIQUETAS') 
app.MainLoop()


