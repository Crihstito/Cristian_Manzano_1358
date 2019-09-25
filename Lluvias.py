import xlrd
for anio in range(1985,2020):
    path = "./Precipitacion/"+str(anio)+"Precip.xls"
    #print(path)
    archivo = xlrd.open_workbook(filename=path)
    hoja=archivo.sheet_by_index(0)
    print(hoja.cell_value(2,1))
