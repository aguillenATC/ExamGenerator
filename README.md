# ExamGenerator
Exams generator for Ingeniería de Servidores and its integration with SWAD

It takes an ODS sheet with the questions and a CSV for the students in the class and generates an ad-hoc exam in latex and an html document with the corresponding mapping between the student's ID and the hashed exam ID (for legal protection of data).

To run:
 1) create a virtual environment: python3 -m venv ExamGen-env
 2) activate it: source activate ExamGen-env/bin/activate
 3) install dependencies: pip install -r requirements
