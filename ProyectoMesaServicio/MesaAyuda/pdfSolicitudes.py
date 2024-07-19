from fpdf import FPDF
from datetime import datetime

class Pdf(FPDF):
    def header(self):
        self.image('static/imagenes/Logo_sena.jpg',10,8,33)
        self.set_font('Arial','B',15)
        self.ln()
        self.cell(60)
        self.cell(80,10,'MESA SERVICIOS CTPI - CAUCA',0,0,'C')
        self.ln()
        self.cell(60)
        self.cell(80,10,'REPORTE SOLICITUDES',0,0,'C')
        self.ln(30)
        return super().header()
    def footer(self) :
        self.set_y(-15)
        self.set_font('Arial','I',8)
        self.cell(0,10,'Page'+str(self.page_no())+'/{nb}',0,0,'C')
        
        
        return super().footer()
    
    def mostrarDatos(self):
        self.cell(30,10,'Fecha')
        fecha=datetime.now()
        self.cell(40,10,str(fecha.day)+'/'+str(fecha.month)+'/'+str(fecha.year))
        