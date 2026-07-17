import csv

f = open("csv_file.csv")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")
f.close()


#Generating a CSV file
hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)



def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

def contents_of_file(filename):
  return_string = ""

  create_file(filename)

  with open(filename) as file:
    rows = csv.reader(file)
    next(rows) #skip over the first row, which is the header row
    for row in rows:
      name, color, type = row

      return_string += "a {} {} is {}\n".format(color, name, type)
  return return_string

print(contents_of_file("flowers.csv"))