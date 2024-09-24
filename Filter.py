
import re


def Filter(text,name,RenderArray):
    ObjectsArray = [['Nombre emisor:','Folio:','RFC receptor:','Nombre receptor:','Código postal del\nreceptor:','Régimen fiscal\nreceptor:','Uso CFDI:',
    'No. de serie del CSD:','Serie:','Código postal, fecha y hora de\nemisión:','Efecto de comprobante:','Régimen fiscal:','Exportación:','Conceptos'], ['Moneda:','Forma de pago:','Método de pago:','Subtotal','\nDescuento ','Impuestos trasladados IVA','Total','Sello digital del CFDI:']]


    ObjectsArray2 = [['basio','bosio']]
    FilterArray = []
    FilterArray.append(['Nombre del archivo',name.split('/')[1].split('.')[0]])

    for ItemArray in ObjectsArray:
        for i in range(len(ItemArray)):
            ItemArrayEnd = ItemArray[1:]
            ItemArrayEnd.append('')
            Item = ItemArray[i]
            ItemEnd = ItemArrayEnd[i]

            RegularExprecion = rf'{Item}([\s\S]*?)\s*{ItemEnd}'
            RegualarValue = re.search(RegularExprecion, text)

            if RegualarValue:
                


                FilterArray.append([Item.replace('\n'," "), RegualarValue.group(1)])
            else:
                FilterArray.append([Item,'NO SE PUDO EXTRAER CORRECTAMENTE'])


        FilterArray.pop()

    return FilterArray
    # print(FilterArray)
    # print("fieuiu\n\n")


            