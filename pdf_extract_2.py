import subprocess

bashCommand = "ls *.txt"

process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

txt_files = output.decode().split('\n')

txt_files = list(filter(lambda x: 'txt' in x, txt_files))
txt_files = list(filter(lambda x: not('test' in x), txt_files))
txt_files = list(filter(lambda x: not('layout' in x), txt_files))

print("State,District,Schools,Class,Subject,Boys,Girls,Rural,Urban,SC,ST,OBC,GEN,Boys Math,Girls Math,Rural Math,Urban Math,SC Math,ST Math,OBC Math,GEN Math")

for txt_file in txt_files:
    fileobj = open(txt_file, 'r')
    lines = fileobj.readlines()
    layoutfileobj = open(txt_file[:-4] + " layout.txt", 'r')
    layout_lines = layoutfileobj.readlines()
    # State
    state = lines[4].split(':')[1].strip()
    # District
    district = lines[6].split(':')[1].strip()

    # Schools
    schools = lines[12].split(':')[1].strip()

    # Class
    student_class = lines[8].split(':')[1].strip()

    # Subject
    subject = lines[10].split(':')[1].strip()

    # # Participation
    # boys = lines[32].strip()
    # girls = lines[36].strip()

    # # rural and urban
    # rural = lines[51].strip()
    # urban = lines[55].strip()

    # # sc st obc gen
    # sc = lines[89].strip()
    # st = lines[93].strip()
    # obc = lines[97].strip()
    # gen = lines[101].strip()

    # # Average Score
    # boys_marks = lines[176].strip()
    # girls_marks = lines[178].strip()
    # rural_marks = lines[180].strip()
    # urban_marks = lines[182].strip()

    # if(lines[196].strip == "" or lines[196].strip() == "OBC"):
    #     sc_marks = lines[194].strip().split()[0]
    #     st_marks = lines[194].strip().split()[1]
    #     obc_marks = lines[200].strip()
    #     gen_marks = lines[202].strip()
    # else:
    #     sc_marks = lines[196].strip().split()[0]
    #     st_marks = lines[196].strip().split()[1]
    #     obc_marks = lines[196].strip().split()[2]
    #     gen_marks = lines[199].strip()

    # rural urban
    rural = layout_lines[24].split()[0]
    urban = layout_lines[24].split()[2]

    # sc st obc gen
    sc = layout_lines[31].split()[0]
    st = layout_lines[31].split()[2]
    obc = layout_lines[31].split()[4]
    gen = layout_lines[31].split()[6]

    # average marks
    boys_marks = layout_lines[56].split()[1]
    girls_marks = layout_lines[56].split()[2]
    rural_marks = layout_lines[56].split()[3]
    urban_marks = layout_lines[56].split()[4]
    sc_marks = layout_lines[56].split()[5]
    st_marks = layout_lines[56].split()[6]
    obc_marks = layout_lines[56].split()[7]
    gen_marks = layout_lines[56].split()[8]

    boys = layout_lines[16].split()[0]
    girls = layout_lines[16].split()[2]

    print(state + "," + 
    district + "," + 
    schools + "," + 
    student_class + "," + 
    subject + "," + 
    boys + "," + 
    girls + "," + 
    rural + "," + 
    urban + "," + 
    sc + "," + 
    st + "," + 
    obc + "," + 
    gen + "," + 
    boys_marks + "," + 
    girls_marks + "," + 
    rural_marks + "," + 
    urban_marks + "," + 
    sc_marks + "," + 
    st_marks + "," + 
    obc_marks + "," + 
    gen_marks)