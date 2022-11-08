import pandas as pd
import numpy as np

def fillgrade(data):
    mahasiswa = data
    n = mahasiswa.shape[0]
    for i in range(n):  
        if mahasiswa['GRADE'][i] != 'F':
            if mahasiswa['NILAI'][i]  >= 85 : 
                mahasiswa['GRADE'][i]  = 'A'
            elif mahasiswa['NILAI'][i]  >= 80 : 
                mahasiswa['GRADE'][i]  = 'A-'
            elif mahasiswa['NILAI'][i]  >= 75 :
                mahasiswa['GRADE'][i]  = 'B+'
            elif mahasiswa['NILAI'][i]  >= 70 :
                mahasiswa['GRADE'][i]  = 'B'
            elif mahasiswa['NILAI'][i]  >= 65 :
                mahasiswa['GRADE'][i]  = 'B-'
            elif mahasiswa['NILAI'][i]  >= 60 :
                mahasiswa['GRADE'][i]  = 'C+'
            elif mahasiswa['NILAI'][i]  >= 55 :
                mahasiswa['GRADE'][i]  = 'C'
            elif mahasiswa['NILAI'][i]  >= 45 :
                mahasiswa['GRADE'][i]  = 'D'
            else:
                mahasiswa['GRADE'][i]  = 'E'
        else:
            continue
    return mahasiswa

    

    
