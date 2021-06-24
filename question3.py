with open('emailaddress.txt', 'w') as fw:
    fw.write("""dioncools@gmail.com
corbinong@gmail.com
sepokbiki@gmail.com
watsonnyambek@gmail.com""")

with open('emailaddress.txt', 'r') as fr:
    with open('emailaddress_copy.txt', 'w') as fw:

        
        reader = fr.readlines()
        rd = ''
        for line in reader:
            rd += str(line).replace('\n', ';')

        fw.write(rd)
        print(rd) 