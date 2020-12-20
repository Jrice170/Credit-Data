import numpy as np
import pandas as pd
import math
from scipy.stats import chi2_contingency
from scipy.stats import chi2
from scipy.stats import spearmanr
from sklearn.decomposition import PCA
import yaml
from pomegranate import *

file_object = open('basyan_out.txt','w')


df = pd.read_csv('credit.csv')





atribute_list = list(df.columns)


df[atribute_list[0]] = df[atribute_list[0]].replace(["?"],str("Los Angeles, CA"))
X = df[atribute_list[0]].copy()
print(df[atribute_list[0]].value_counts())
df[atribute_list[0]].value_counts().to_csv('location.csv')




df[atribute_list[1]] = df[atribute_list[1]].replace(["?"],"California")





df[atribute_list[2]] = df[atribute_list[2]].replace(["?"],"0")

df[atribute_list[2]] = pd.to_numeric(df[atribute_list[2]])




#print(df[atribute_list[3]])


#df[atribute_list[3]] = df[atribute_list[3]].astype(int)
#df.loc[df.duration<=10,"duration"] = 1
##df.loc[df[atribute_list[3]] = 10,:] = 1


df.loc[df[atribute_list[3]] == "?",atribute_list[3]] = 0


df[atribute_list[3]] = pd.to_numeric(df[atribute_list[3]])
MEAN = df.loc[df[atribute_list[3]] != 0,atribute_list[3]].mean()
MEAN = int(np.floor(MEAN))
df.loc[df[atribute_list[3]] == 0,atribute_list[3]] = MEAN

df[atribute_list[3]].to_csv("location.csv")




print(atribute_list[4])
print(df[atribute_list[4]])
df[atribute_list[4]] = df[atribute_list[4]].replace(["?"],str('no credit history'))
df[atribute_list[4]].value_counts().to_csv('credit_history')





df[atribute_list[5]] = df[atribute_list[5]].replace(["?"],"Unknown")
df[atribute_list[5]].value_counts().to_csv('purpose')



df.loc[df[atribute_list[6]] == "?",atribute_list[6]] = 0
df[atribute_list[6]] = pd.to_numeric(df[atribute_list[6]])
MEAN = df.loc[df[atribute_list[6]] != 0, atribute_list[6]].mean()

df.loc[df[atribute_list[6]]==0,atribute_list[6]] = int(MEAN)

df[atribute_list[6]].value_counts().to_csv('creditamount')


df[atribute_list[7]] = df[atribute_list[7]].replace(["?"],'0')
df[atribute_list[7]] = pd.to_numeric(df[atribute_list[7]])

df[atribute_list[7]].value_counts().to_csv("saveings")



df[atribute_list[8]] = df[atribute_list[8]].replace(["?"],"Unknown")
df[atribute_list[8]].value_counts().to_csv("employ")


df[atribute_list[9]] = df[atribute_list[9]].replace(["?"],"0")
df[atribute_list[9]] = pd.to_numeric(df[atribute_list[9]])
df[atribute_list[9]].value_counts().to_csv("installment_commitment")



df[atribute_list[10]] = df[atribute_list[10]].replace(["?"],'Unknown')
df[atribute_list[10]].value_counts().to_csv("personal_status")



df[atribute_list[11]] = df[atribute_list[11]].replace(["?"],"Unknown")
df[atribute_list[11]].value_counts().to_csv("other_parties")


df[atribute_list[12]] = df[atribute_list[12]].replace(["?"],"0")
df[atribute_list[12]].value_counts().to_csv("residence_since")



df[atribute_list[13]] = df[atribute_list[13]].replace(["?"],"Other")
df[atribute_list[13]].value_counts().to_csv("property_magnitude")


df[atribute_list[14]] = df[atribute_list[14]].replace(["?"],'0')

df[atribute_list[14]] = pd.to_numeric(df[atribute_list[14]])

MEAN = df.loc[(df[atribute_list[14]] <= 75) & (df[atribute_list[14]] != 0),atribute_list[14]].mean()
df.loc[(df[atribute_list[14]] > 75) | (df[atribute_list[14]] == 0),atribute_list[14]] = int(MEAN)
df.loc[(df[atribute_list[14]] <0),atribute_list[14]] = int(MEAN)
df[atribute_list[14]].value_counts().to_csv("age")



df[atribute_list[15]] = df[atribute_list[15]].replace(["?"],"Other")
df[atribute_list[15]].value_counts().to_csv("other_payment_plans")


df[atribute_list[16]] = df[atribute_list[16]].replace(["?"],"Other")

df[atribute_list[16]].value_counts().to_csv("housing")



df[atribute_list[17]] = df[atribute_list[17]].replace(["?"],"0")
df[atribute_list[17]].value_counts().to_csv("existing_credits")



df[atribute_list[18]] = df[atribute_list[18]].replace(["?"],"Other")
df[atribute_list[18]].value_counts().to_csv("job")



df.loc[(df[atribute_list[19]] != '1') & (df[atribute_list[19]] != '2'),atribute_list[19]] = "Unknown"
df[atribute_list[19]].value_counts().to_csv("num_dependents")





df[atribute_list[20]] = df[atribute_list[20]].replace(["?"],"no")
df[atribute_list[20]].value_counts().to_csv('own_telephone')


df[atribute_list[21]] = df[atribute_list[21]].replace(['N'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['No'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['NO'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['n'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Yes'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['YES'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['1'],'Unknown')
df[atribute_list[21]] = df[atribute_list[21]].replace(['?'],'Unknown')
df[atribute_list[21]].value_counts().to_csv('foreign_worker')


df[atribute_list[22]] = df[atribute_list[22]].replace(['GOOD'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['good'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['G'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['bad'],'Bad')
df[atribute_list[22]] = df[atribute_list[22]].replace(['B'],'Bad')
df[atribute_list[22]] = df[atribute_list[22]].replace(['?'],'Good')
df[atribute_list[22]].value_counts().to_csv("class")




df[atribute_list[25]] = df[atribute_list[25]].replace(['N'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['No'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['NO'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['n'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['Yes'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['YES'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['y'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['Y'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['1'],'Unknown')
df[atribute_list[25]] = df[atribute_list[25]].replace(['?'],'Unknown')
print(df[atribute_list[25]].value_counts())
df[atribute_list[25]].value_counts().to_csv('work_outside_US')


df = df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,25]].copy()



def Chi_square_test(data_frame):
  ##dof = (row-1)*(cols-1)
  sig = 0.05
  chi, pval, dof, exp = chi2_contingency(data_frame)
  p = 1 - sig
  critical_value = chi2.ppf(p,dof)
  if(chi > critical_value):

      return "N"

  else:

      return "I"


atribut_list = ['location','state','credit_history','purpose','employment','installment_commitment',\
'personal_status','other_parties','residence_since','property_magnitude','housing','job',\
'num_dependents','foreign_worker','class',]

Chi_fram = pd.DataFrame( columns = atribut_list, index=atribut_list)

X = df.copy()
V = []
for i in range(0,len(atribut_list)):

   for j in range(i+1,len(atribut_list)):

        Add_list = X.groupby([atribut_list[i],atribut_list[j]])[[atribut_list[j]]].count().unstack().fillna(0)
        V.append(Add_list)

count = 0;
for i in range(0,len(atribut_list)):

   for j in range(i+1,len(atribut_list)):



        Chi_fram.iloc[i,j] = Chi_square_test(V[count])
        count = count + 1


Chi_fram.to_csv('I_test.csv')

def spear_val(row_index, col_index,DataFrame_1,list_value):

    X1 =  DataFrame_1.loc[:,list_value[row_index]].values.reshape(-1,1)
    Y1 =  DataFrame_1.loc[:,list_value[col_index]].values.reshape(-1,1)
    corr, p_value = spearmanr(X1,Y1)





    if((np.abs(corr) >= 0.8)):


        return "N"


    else:


        return "I"


atribut_list2 = ['checking_amt','duration','credit_amount','savings','age']
spear_fram = pd.DataFrame(columns = atribut_list2, index=atribut_list2)

for i in range(0,len(atribut_list2)):

    for j in range(i+1,len(atribut_list2)):

        spear_fram.iloc[i,j] = spear_val(i,j,X,atribut_list2)



print(spear_fram)
spear_fram.to_csv("spea_fram.csv")



df.to_csv('cleaned_credit.csv')


New_List = ['state','credit_history',\
	'purpose','employment',	\
    	'personal_status','other_parties','property_magnitude','age','other_payment_plans','housing'\
        	,'job','num_dependents','foreign_worker','class','works_outside_US']
nominal_only = df.loc[:,New_List].copy()
print(nominal_only)




def map_value(df,atribute_str):

    dix = {}
    for i in df[atribute_str]:
        dix[i] = i


    return list(dix)

def Condition_prob(df,atribute1,value1,atribute2,value2,k_value,lambda1):

    Top = df.loc[(df[atribute1] == value1) & (df[atribute2]==value2),:].index.size
    Botton = df.loc[(df[atribute1] == value1),:].index.size

    return (Top + lambda1)/(Botton + k_value*lambda1)


def Create_bayesian_network(data_fram,lambdaa=1,title=''):
    N = data_fram.index.size
    DiscreatDistribution_list = []
    atribute_list = list(data_fram.columns)

    model = BayesianNetwork(title)

    Decision_atrbute_str = atribute_list[len(atribute_list) - 1]
    Dictionary1 = {}
    for each in map_value(data_fram,Decision_atrbute_str):
        K = len(map_value(data_fram,Decision_atrbute_str))
        Dictionary1[each] = ((data_fram.loc[data_fram[Decision_atrbute_str]==each,:]\
        .index.size)+(lambdaa))/(N+K*lambdaa)

    DiscreatDistribution_list.append(DiscreteDistribution(Dictionary1))



    for i in range(0,len(atribute_list)-1):
        list2 = []
        for k in map_value(data_fram,Decision_atrbute_str):
            for j in map_value(data_fram,atribute_list[i]):
                list2.append([k,j,Condition_prob(data_fram,Decision_atrbute_str,k,\
                atribute_list[i],j,\
                len(map_value(data_fram,atribute_list[i])),lambdaa)])

        G = ConditionalProbabilityTable(list2,[DiscreatDistribution_list[0]])

        DiscreatDistribution_list.append(G)

    model = BayesianNetwork(title)
    S1 = Node(DiscreatDistribution_list[0],name=Decision_atrbute_str)
    model.add_state(S1)


    ##model.add_states(DiscreatDistribution_list[0])
    ##model.add_edge(DiscreatDistribution_list[0],DiscreatDistribution_list[1])



    for i in range(1,len(DiscreatDistribution_list)):


        S = Node(DiscreatDistribution_list[i],name=atribute_list[i-1])

        model.add_state(S)

        model.add_edge(S1,S)


    model.bake()
    return model
"""
New_List = ['state','credit_history',\
	'purpose','employment',	\
    	'personal_status','other_parties','property_magnitude','age','other_payment_plans','housing'\
        	,'job','num_dependents','foreign_worker','class','works_outside_US']

"""
nominal_only.to_csv("H.csv")

new_model = Create_bayesian_network(nominal_only,1,"name of ......")


value_list = []
for i in New_List:

    value_list.append(map_value(nominal_only,i))



for j in value_list[0]:   ### state

    for n in value_list[1]:



        #print("input: ",[i,None,j,n,None,None,k,None,None,None,None,None,None,None,None,None,None])
        file_object.write(str([None,j,n,None,None,None,None,None,None,None,None,None,None,None,None,None]))
        file_object.write("\n")
        #print(new_model.predict([[i,None,j,n,None,None,k,None,None,None,None,None,None,None,None,None]]))
        file_object.write(str(new_model.predict([[None,j,n,None,None,None,None,None,None,None,None,None,None,None,None]])))

        file_object.write("\n")
