import csv

f = open('/Users/aitorcalero/Downloads/data.csv','r')
d = [i for i in csv.reader(f)]
f.close()
for i in range(1,10):
    print(d[i])

d[0].append('Last Name')
d[0].append('First Name')

print(d[0])

for row in d[1:]:
    if len(row[2].split()) == 2:
        first,last = row[2].split()
        row.append(last)
        row.append(first)


for i in range(1,10):
    print(d[i])


f = open('/Users/aitorcalero/Downloads/data_out.csv','w')
fw = csv.writer(f)
fw.writerows(d)
f.close()