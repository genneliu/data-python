open_file = open("CupcakeInvoices.csv")
#print each row
for row in open_file:
    print(row)

open_file.seek(0)

#print each flavor
for line in open_file:
    line = line.rstrip('\n').split(',')
    cupcakes = line[2]
    print(cupcakes)

open_file.seek(0)

#print each invoice
for line in open_file:
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4]) #has decimals
    total = quantity * price
    print(total)


open_file.seek(0)
#print total invoice

total = 0 
for line in open_file:
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4]) #has decimals
    total += quantity * price

print(total)



open_file.close()