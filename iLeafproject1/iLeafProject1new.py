
import csv
with open('./AS.csv', 'rU') as csv_file:
    csv_reader = csv.reader(csv_file)
    # totalAmount = 0.00
    dict = {}
    for line in csv_reader:
        val = 0.00
        words = (line[6]).split("$")
        if len(words) >= 2:
            if words[0] == '-':
                val = -round(float(words[1]), 2)
            elif words[0] == '':
                val = round(float(words[1]), 2)
        if line[5] != 'Payment Detail':
            if line[5] in dict:
                dict[line[5]] += round(float(val))
            else:
                dict[line[5]] = round(float(val))

    print(dict)




