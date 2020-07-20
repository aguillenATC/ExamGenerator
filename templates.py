
html_code = r'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 5.0.6.2 (Linux)"/>
	<meta name="author" content="Alberto "/>
	<meta name="created" content="2017-10-31T09:47:50.854997635"/>
	<meta name="changedby" content="Alberto "/>
	<meta name="changed" content="2017-10-31T09:51:14.420114484"/>
</head>
<body lang="es-ES" dir="ltr">
<p><br/>
<br/>

</p>
<table cellpadding="2" cellspacing="0">
	<col width="98">
	<col width="103">
	<col width="103">
	<col width="103">
	<col width="49">
	<col width="49">
	<col width="60">
	<col width="97">
	<tr valign="bottom">
		<td height="17" style="border: 1px solid #000000; padding: 0.05cm">
			<p align="center"><font face="Cambria"><b>DNI</b></font></p>
		</td>
		<td style="border: 1px solid #000000; padding: 0.05cm">
			<p align="center"><font face="Cambria"><b>URL del Examen</b></font></p>
		</td>
	</tr>
	'''
html_row = """
	<tr valign="bottom">
		<td height="18" style="border: 1px solid #000000; padding: 0.05cm" sdval="75575055" sdnum="3082;">
			<p align="center"><font face="Cambria">{DNI}</font></p>
		</td>
		<td style="border: 1px solid #000000; padding: 0.05cm">
			<p align="center"><font face="Cambria">{URL}</font>
			</p>
		</td>		
	</tr>
	"""

html_code_end = r"""	
</tr>
</table>
<p><br/>
<br/>

</p>
</body>
</html>
"""




tex_header = r'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\documentclass[a4paper,11pt]{article}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage{array}              % m
\usepackage{amsmath}            % texto en modo matemático
\usepackage[spanish]{babel}     % español
\usepackage{caption}            % captionof
\usepackage[ddmmyyyy]{datetime} % formato fecha (\today)
\usepackage{epsfig}             % epsfig
\usepackage{geometry}           % geometry
\usepackage{graphicx}           % includegraphics
\usepackage[utf8]{inputenc}     % tildes
\usepackage{listings}           % listado de fuentes
\usepackage{multicol}           % varias columnas
\usepackage{xcolor}             % gray
\usepackage{float}              % place floating objects

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\geometry{margin=8mm,top=16mm,bottom=16mm}

\lstset{
	alsoletter={\%},
	basicstyle=\ttfamily,
	breaklines=true,
	extendedchars=true,
	inputencoding=utf8,
	keepspaces=true,
	language=C++,
	literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
	         {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1
	         {à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1
	         {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1
	         {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1
	         {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1
	         {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1
	         {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1
	         {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1
	         {ű}{{\H{u}}}1 {Ű}{{\H{U}}}1 {ő}{{\H{o}}}1 {Ő}{{\H{O}}}1
	         {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1
	         {ñ}{{\~{n}}}1 {Ñ}{{\~{N}}}1 {€}{{\EUR}}1 {£}{{\pounds}}1,
	numberstyle=\tiny\color{gray},
	language=C++,
	showspaces=false,
	showstringspaces=false,
	showtabs=false,
	tabsize=2,
}

\lstdefinestyle{n}{numbers=left}
\lstdefinestyle{s}{basicstyle=\small\ttfamily}
\lstdefinestyle{fn}{basicstyle=\footnotesize\ttfamily}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
tex_subheader = r"""
\newcommand{\encabezado}{
\begin{center}
\bfseries 
\begin{tabular}{*{3}{p{0.5\textwidth}}}
	\epsfig{file=logotipos/ugr-logo.png,height=12mm} & \multicolumn{1}{c}{\epsfig{file=logotipos/etsiit-logo.png,height=12mm}} & \multicolumn{1}{r}{\epsfig{file=logotipos/atc-logo.png,height=12mm}} \\\\
	\\\\
	\multicolumn{3}{c}{Ingeniería de Servidores \hfill Examen: Julio 2020} \\\\
	\\\\
	\multicolumn{3}{l}{Nombre:} \scriptsize $xApellidos$, $xNombre$ \hfill DNI: ***$xDNI$* \hspace{1mm} \\\\
	\hline
\end{tabular}
\end{center}
\vspace{5mm}
}

\newenvironment{mfigure}
	{\par\medskip\noindent\minipage{\linewidth}}
	{\endminipage\par\medskip}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}
\pagenumbering{gobble}
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\encabezado
{\bfseries \noindent Calificación máxima 10 puntos, mínima 4 puntos. Porcentaje sobre el total 40\%. Intrucciones:}
\begin{itemize}
\item La duración del examen es de \textbf{2 horas y 30 minutos}
\item Muestre en cada respuesta el \textbf{desarrollo completo de todos los pasos} seguidos hasta alcanzar la solución.
\item Escriba las respuestas en \textbf{papel blanco} liso (sin cuadrículas o líneas) y use \textbf{bolígrafo azul o negro}.
\item Se tendrán en cuenta las \textbf{faltas de ortografía} en la calificación final y no especificar las unidades.
\item Asegúrese de que al escanear o fotografiar los folios (numerados) con las \textbf{respuestas}, las capturas son totalmente \textbf{legibles}. Se recomienda el uso de aplicaciones móviles como CamScanner o similar en caso de no disponer de escáner de sobremesa.
\end{itemize}


\vspace{1mm}
"""

tex_tail = r'''
    \end{document}
    '''
