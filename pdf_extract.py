import subprocess

bashCommand = "ls *.txt"

process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

txt_files = output.decode().split('\n')

txt_files = list(filter(lambda x: 'txt' in x, txt_files))
txt_files = list(filter(lambda x: not('test' in x), txt_files))

print("State,District,Schools,Class,Subject,Boys,Girls,Rural,Urban,SC,ST,OBC,GEN,Boys Math,Girls Math,Rural Math,Urban Math,SC Math,ST Math,OBC Math,GEN Math")

for txt_file in txt_files:
    fileobj = open(txt_file, 'r')
    lines = fileobj.readlines()

    #State
    state = lines[5].split()[1]
    # District
    try:
        district = lines[5].split()[4]
    except:
        district = lines[5].split()[3]

    # No of Schools
    schools = lines[7].split()[1]

    # Class
    student_class = lines[6].split()[1]

    #subject
    subject = lines[6].split()[3]

    # rural urban
    rural = lines[24].split()[0]
    urban = lines[24].split()[2]

    # sc st obc gen
    sc = lines[31].split()[0]
    st = lines[31].split()[2]
    obc = lines[31].split()[4]
    gen = lines[31].split()[6]

    # average marks
    boys_math = lines[56].split()[1]
    girls_math = lines[56].split()[2]
    rural_math = lines[56].split()[3]
    urban_math = lines[56].split()[4]
    sc_math = lines[56].split()[5]
    st_math = lines[56].split()[6]
    obc_math = lines[56].split()[7]
    gen_math = lines[56].split()[8]

    values = lines[16].split()
    print(state + "," + district + "," + schools + "," + student_class + "," + subject + "," + values[0] + "," + values[2] + "," + rural + "," + urban
         + "," + sc + "," + st + "," + obc + "," + gen + "," + 
         boys_math + "," +
         girls_math + "," +
         rural_math + "," +
         urban_math + "," +
         sc_math + "," +
         st_math + "," +
         obc_math + "," +
         gen_math)
