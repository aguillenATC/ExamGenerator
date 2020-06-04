import pandas as pd
import subprocess
import os

from templates import *

listado = pd.read_csv("/home/alberto/ListaGIADE-19-20.txt")

#create hash code for each DNI
for (idx,dni) in listado['DNI'].items():
	listado.loc[idx,'HASH'] = str(abs(hash(str(dni))))

print(listado)

#CHECK REPLCIATERD DNIs OR HASH
if any(listado['DNI'].duplicated()) or any(listado['HASH'].duplicated()):
	print("DNI or HASH duplicated")
	exit("DNI or HASH duplicated")



tex_body = r'''

'''


html_body = ""

base_url = "https://ugr.es/~aguillen/examenISE/"

for alumn in listado.as_matrix():
    
    print(alumn)

    file_name = str(alumn[3]) 

	#add alumn to html list
    html_body += html_row.format(DNI = alumn[0], URL = base_url + file_name +'.pdf')



	#fill data specific header
    kv = {'xApellidos' : str(alumn[1]), 'xNombre' : str(alumn[2]), 'xDNI' : str(alumn[0])[3:7]}
    tex_subheader_filled = tex_subheader
    for key, value in kv.items():
        tex_subheader_filled = tex_subheader_filled.replace('$'+key+'$', value)

    #Open file and inser header
    with open(file_name+'.tex','w') as f:
        f.write(tex_header+
		tex_subheader_filled+
		tex_body)


    #Insert specific part of the exam
    with open(file_name+'.tex','a') as f:
        f.write("Nombre alumno" + str(alumn))

    #Insert the end of the document
    with open(file_name+'.tex','a') as f:
        f.write(tex_tail)
    
    # Generate PDF
    cmd = ['pdflatex', '-interaction', 'nonstopmode', file_name+'.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink(file_name+'.pdf')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

    #os.unlink(file_name+'.tex')
    #os.unlink(file_name+'.aux')
    #os.unlink(file_name+'.log')

os.system('rm *.tex')
os.system('rm *.aux')
os.system('rm *.log')

#Write html file
with open('ListadoExamenes.html', 'w') as f:
	f.write(html_code + html_body + html_code_end)