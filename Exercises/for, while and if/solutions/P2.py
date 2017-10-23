input_number = int(input("Enter withdrawal amount:"))                                                              
banknotes=[100,50,10,5,1]                                                                                 
nbanknote = 0                                                                                             
                                                                                                          
print(input_number, "TL = ")                                                                                       
for i in banknotes:                                                                                       
    nbanknote = input_number // i                                                                                  
    if nbanknote > 0:                                                                                     
        print(nbanknote,"X",i,"TL")                                                                       
        input_number = input_number - (i*nbanknote)