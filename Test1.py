import csv
with open('file.csv','w') as file:
    writer = csv.writer(file)

    writer.writerow(['Luciano','Maria','Carlos'])
    writer.writerow(['Maria', 'Ana'])
    writer.writerow(['Joao', 'Roberto'])