# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:50:44 2017

@author: Akshaykumar.Kore
"""



import pandas as pd

datsetTrans=pd.read_csv("C:/Users/akshaykumar.kore/Downloads/machine learning/Code Gladiators-Invesco-DataSet/Code-Gladiators-Transaction.csv")
datsetAum=pd.read_csv("C:/Users/akshaykumar.kore/Downloads/machine learning/Code Gladiators-Invesco-DataSet/Code-Gladiators-AUM.csv")
datsetInesExp=pd.read_csv("C:/Users/akshaykumar.kore/Downloads/machine learning/Code Gladiators-Invesco-DataSet/Code-Gladiators-InvestmentExperience.csv")
datsetActivity=pd.read_csv("C:/Users/akshaykumar.kore/Downloads/machine learning/Code Gladiators-Invesco-DataSet/Code-Gladiators-Activity.csv")

transAum_dataset=pd.merge(datsetTrans,datsetAum,how='inner',left_on=['Unique_Advisor_Id','Unique_Investment_Id','Month'], right_on=['Unique_Advisor_Id','Unique_Investment_Id','Month'])
transauminverexp_datset=pd.merge(transAum_dataset,datsetInesExp,how="inner",left_on=['Unique_Investment_Id','Month'],right_on=['Unique_Investment_Id','Month'])
transauminesexpactivity_dataset=pd.merge(transauminverexp_datset,datsetActivity,how="inner",left_on=['Unique_Advisor_Id','Month'],right_on=['Unique_Advisor_Id','Month'])
#transauminesexpactivity_dataset = transauminesexpactivity_dataset.drop(transauminesexpactivity_dataset['Month'] == '2016/12')
transauminesexpactivity_dataset.to_csv("transauminesexpactivity.csv")