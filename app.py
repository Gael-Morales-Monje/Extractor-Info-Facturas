import PyPDF2
from openpyxl import Workbook
from openpyxl.styles import Font
import tkinter as tk

from Path import ExtractPaths
from Filter import Filter

def main(path, Endfile):
    ArrayPath = ExtractPaths(f'{path}/')

    RenderArray = []

    for pdf in ArrayPath:
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(pdf)
            text = ''
            for pag in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[pag]
                text += page.extract_text()

            
            Array = Filter(text,pdf,RenderArray)
            RenderArray.append(Array)


    Book = Workbook()
    sheet = Book.active
    n = 1
    for Info in RenderArray:
        for I in range(len(Info)):
            sheet[f'A{n}'] = Info[I][0]
            if I == 0:
                sheet[f'A{n}'].font = Font(color='1201ff')
            else:
                sheet[f'A{n}'].font = Font(color='555555')
            sheet[f'B{n}'] = Info[I][1]
            n+=1
        n+=2

    Book.save(f'{Endfile}.xlsx')



main('pdf','aa')