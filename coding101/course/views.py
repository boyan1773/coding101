from django.shortcuts import render
import pandas as pd
# Create your views here.
def course(request):
    list=read_excel()
    print(list)
    return render(request,'index.html',locals())

def read_excel():
    data=pd.read_excel('data.xlsx')
    one_row_keys=data.keys()
    row_keys=[i for i in one_row_keys]
    sum_rows = data.index.values
    df_list=[]
    for i in sum_rows:
        row_dict=data.loc[i,row_keys].to_dict()
        df_list.append(row_dict)
    return df_list