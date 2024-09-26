from lxml import etree as ET
import subprocess
from PyPDF2 import PdfMerger

dict_patos={'1':'Chikungunya',
       '2':'COVID-19',
       '3':'Dengue',
       '4':'Influenza_A',
       '5':'RSV'}

                    # FUNCIONES COMPLETAS #

#################################################################
##################### Exportar SVG a PDF ########################
#################################################################

def export_svg_to_pdf(svg_file, pdf_file):
    # Define el comando de Inkscape
    command = ["/Applications/Inkscape.app/Contents/MacOS/inkscape", "--pipe", f"--export-filename={pdf_file}"]

    # Abre el archivo SVG y pasa su contenido al comando de Inkscape
    try:
        with open(svg_file, 'rb') as svg_content:
            subprocess.run(command, input=svg_content.read(), check=True)
        print(f"Archivo '{svg_file}' exportado exitosamente a PDF como '{pdf_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al exportar '{svg_file}' a PDF: {e}")
    except FileNotFoundError:
        print(f"El archivo '{svg_file}' no se encontró.")
'''
#################################################################
# Uso del programa
raiz='/Users/galmarod/Documents/PruebasBASH/'
export_svg_to_pdf(raiz+"P2_1-temp.svg", raiz+"P2_1-temp.pdf")
#################################################################
'''
#################################################################
########################## Unir PDF #############################
#################################################################

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()
'''
#################################################################
# Ejemplo de uso
raiz='/Users/galmarod/Documents/PruebasBASH/'
pdfs = [raiz+"P1-temp.pdf", raiz+"P2_1-temp.pdf"]
output = raiz+"archivo_unido.pdf"
#merge_pdfs(pdfs, output)
print(f"PDFs unidos en: {output}")
#################################################################
'''
#################################################################
####################### Plantilla P1 ############################
#################################################################

def modify_svg_1(new_text):
    # Definir los espacios de nombres utilizados en el archivo SVG
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    tspan_id_text = 'tspan2'
    #Definir los documentos de entrada (in) y salida (exp-temp.svg y exp-temp.pdf )
    p1in='/Users/galmarod/Documents/GrupoT4/PABLO/Branding/P1.svg'
    p1exp='/Users/galmarod/Documents/PruebasBASH/P1-temp.svg'
    p1pdf='/Users/galmarod/Documents/PruebasBASH/P1-temp.pdf'
    # Cargar el archivo SVG
    tree = ET.parse(p1in)
    root = tree.getroot()
    # Encontrar el tspan Título con el id especificado utilizando los espacios de nombres
    tspan_text = root.find(f".//svg:tspan[@id='{tspan_id_text}']", namespaces)
    if tspan_text is not None:
        # Modificar el texto del tspan
        tspan_text.text = new_text
    else:
        print(f"No se encontró el elemento tspan con id '{tspan_id_text}'")
    # Guardar los cambios en un nuevo archivo
    tree.write(p1exp)
    export_svg_to_pdf(p1exp,p1pdf)
    print("P1-temp.pdf completado")

################## Prueba de funcionamiento #####################
# Variables de Prueba
text_portada= "Generación de sistema de diagnóstico por IA de "
new_text = (text_portada + 'Patógeno X')
modify_svg_1(new_text)
#################################################################
