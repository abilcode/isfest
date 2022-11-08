import pandas as pd
import numpy as np

def fillnilai(data):
    mahasiswa = data
    mahasiswa.NILAI.fillna(1,inplace=True)
    n = mahasiswa.shape[0]
    for i in range(n):   
        if mahasiswa['GRADE'][i] != 'F' and mahasiswa['GRADE'][i] != np.nan and mahasiswa['NILAI'][i] != np.nan :
            if  mahasiswa['GRADE'][i] == 'A':
                mahasiswa['NILAI'][i]  = 85. 
            elif mahasiswa['GRADE'][i]== 'A-' :
                 mahasiswa['NILAI'][i] = 80.  
            elif mahasiswa['GRADE'][i] == 'B+' :
                 mahasiswa['NILAI'][i] = 75.
            elif mahasiswa['GRADE'][i] == 'B':
                 mahasiswa['NILAI'][i] = 70.
            elif mahasiswa['GRADE'][i] == 'B-':
                 mahasiswa['NILAI'][i] = 65.
            elif mahasiswa['GRADE'][i] == 'C+':
                 mahasiswa['NILAI'][i] = 60. 
            elif mahasiswa['GRADE'][i] == 'C':
                 mahasiswa['NILAI'][i] = 55.
            elif mahasiswa['GRADE'][i]  == 'D' :
                 mahasiswa['NILAI'][i] = 45.
            else:
                mahasiswa['GRADE'][i]  = 'E'
        else:
            continue
    return mahasiswa

    

    
