#coding=utf-8
import numpy as np
import pandas as pd
data_dirt_list=open("/Users/gavin/Library/Mobile Documents/com~apple~CloudDocs/G's/Prostgraduate in CityU_HK/Sememter B/COM5506 Social Network Analysis for Communication/COM5506_Coding& Data/GroupProject/DATA/RAW Data_SNAGroupProject.txt")
lines=data_dirt_list.readlines()
keywords=[]
for i in lines:
    if "K1" in i:
        K1_list=i.strip('K1')
        K1_list=K1_list.strip('\n')
        K1_list=K1_list.strip()
        K1_list=K1_list.split(';')
        keywords.append(K1_list)
p_k=pd.DataFrame(data=keywords)
p_k.to_csv("/Users/gavin/Library/Mobile Documents/com~apple~CloudDocs/G's/Prostgraduate in CityU_HK/Sememter B/COM5506 Social Network Analysis for Communication/COM5506_Coding& Data/GroupProject/DATA/k_p.csv",encoding='utf-8')
