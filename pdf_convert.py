import subprocess

bashCommand = "ls *.pdf"

process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

file_list = output.decode().split('\n')

pdf_list = list(filter(lambda x: 'pdf' in x, file_list))

# bashCommand = "pdftotext \"bilaspur (h.p.) Class - 3 (Mathematics)  Report Card.pdf\" -layout"

# process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
for file in pdf_list:
    bashCommand = "pdftotext \"" + file + "\""
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    bashCommand = "pdftotext \"" + file + "\" \"" + file[:-4] + " layout.txt\" -layout"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    
print(len(file_list) - len(pdf_list))
