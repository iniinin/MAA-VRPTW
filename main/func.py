import numpy as np
import pandas as pd

df1 = pd.DataFrame(pd.read_excel('D:\input_alldata_fea_0-649998.xlsx'))
df2 = pd.DataFrame(pd.read_excel('D:\input_alldata_fea_649999-end.xlsx'))
df=df1.append(df2)
df=df.set_index("ID", drop=False)
#������excel�ϲ�����dataframe

while(1):
    button=int(input("Press 1 to continue or 0 to exit:"))
    if button==0: break
    fn=int(input("Please enter from node:"))
    tn=int(input("Please enter to node:"))
    #���������ָ����
    if tn > fn:
        id = 1100 * fn + tn - 1
    elif tn < fn:
        id = 1100 * fn + tn
    else:
        id = 'Error: From_node should be different from to_node.'
    #��ȷ����from node��to node����Ӧ��ID
    if id!='Error: From_node should be different from to_node.':
        if(df.iloc[id,5]==0):
            distance=df.iloc[id,3]
            spend_tm=df.iloc[id,4]
        else:
            distance=-1
            spend_tm=-1
        print("ID: "+str(id))
        print("Distance: "+str(distance)+'\n'+"Spend_time: "+str(spend_tm)+'\n')
    else:
        print(str(id))
    #��ӡID�������ʱ�����