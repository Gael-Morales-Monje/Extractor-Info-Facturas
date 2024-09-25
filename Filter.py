import re


def Filter(text,name,RenderArray):
    ObjectsArray = [['Nombre emisor:','Folio:','RFC receptor:','Nombre receptor:','Código postal del\nreceptor:','Régimen fiscal\nreceptor:','Uso CFDI:',
    'No. de serie del CSD:','Serie:','Código postal, fecha y hora de\nemisión:','Efecto de comprobante:','Régimen fiscal:','Exportación:','Conceptos'], ['Moneda:','Forma de pago:','Método de pago:','Subtotal','\nDescuento ','Impuestos trasladados IVA','Total','Sello digital del CFDI:']]


    ObjectsArray2 = [['Nombre emisor:','Folio:','RFC receptor:','Nombre receptor:','Código postal del\nreceptor:', 'Régimen fiscal\nreceptor:','Uso CFDI:','Folio fiscal:','No. de serie del CSD:','Serie:','Código postal, fecha y hora de\nemisión:','Efecto de comprobante:','Régimen fiscal:','Exportación:','Conceptos'],['Moneda:','Forma de pago:','Método de pago:','Subtotal','Impuestos trasladados IVA','Total','Sello digital del CFDI:']]


    SuperArray = [ObjectsArray,ObjectsArray2,'']

    FilterArray = []
    FilterArray.append(['Nombre del archivo',name.split('/')[1].split('.')[0]])


    # ReadArray = ObjectsArray
    Count = 0
    while True:
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
                    if Count > 1:
                        FilterArray.append([Item.replace('\n'," "), 'No se pudo'])
                    else:
                        Count += 1
                        break

            
            FilterArray.pop()
            ObjectsArray = SuperArray[Count]
            continue

        break


    return FilterArray
#     # print(FilterArray)
#     # print("fieuiu\n\n")


            