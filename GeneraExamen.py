import pandas as pd
import subprocess
import os
import random
from pandas_ods_reader import read_ods


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


#read the questions (they should be in the sheet 1)
questions = read_ods("PreguntasISE.ods", 1) 

#TODO read solutions
#solutions = read_ods("Preguntas.ods", 2) 


tex_body = r'''

'''


html_body = ""

base_url = "https://ugr.es/~aguillen/examenISE/"

for alumn in listado.to_numpy():
    
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
        #f.write("Nombre alumno" + str(alumn))

		#for each question set
        for i in range(questions.shape[1]):
            
            # get metadata about the question
            q_params_str = questions.iloc[0][i]
            

            # Process metadata about the question
            # string to dictionary 
            q_params = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in q_params_str.split(', '))) 
   

            #get one question randomly (the first row contains metadata about the question)
            q = random.randint(1,questions.shape[0]-1)
            while (questions.iloc[q][i] == None):
                q = random.randint(1,questions.shape[0]-1)
			
            f.write('\n' + r''' \noindent \textbf{Pregunta''' + str(i+1) +r''' (''' + str(q_params['Points']) + ''' Punto/s ) :} '''+'\n \n')
            f.write(questions.iloc[q][i])
            f.write(' \n \n'+ r''' \vspace{1cm} ''' + ' \n ')



    #Insert the end of the document
    with open(file_name+'.tex','a') as f:
        f.write('\n ' + tex_tail)
    
    # Generate PDF
    cmd = ['pdflatex', '-interaction', 'nonstopmode', file_name+'.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        #os.unlink(file_name+'.pdf')
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