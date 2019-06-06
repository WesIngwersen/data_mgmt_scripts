# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:52:06 2019

@author: ALarger

Cal Pesticide Residues 1996
"""

import camelot
import pandas as pd

chemName = []

tables = (camelot.read_pdf(r'L:\Lab\HEM\ALarger\Actor Automated Extraction\California\Cal Pesticide Residues\document_1359544.pdf',pages='1327-1768', flavor='stream')) 

for table in tables: 
    df = table.df
    chemName.extend(df.iloc[:,0])

m = len(chemName) 
while m > 0: #Go backwards through chemical name list so that the indexing does not get messed up when one is deleted
    m-=1
    chemName[m] = chemName[m].strip()
    if chemName[m] == '' or chemName[m] == 'NONE' or chemName[m] == 'chem code':
        del chemName[m]
  
nIngredients = len(chemName)
msdsDate = ['1996']*nIngredients
recUse = ['']*nIngredients
catCode = ['']*nIngredients
descrip = ['']*nIngredients
code = ['']*nIngredients 
sourceType = ['ACToR Assays and Lists']*nIngredients
casN = ['']*nIngredients
prodID = [1359544]*nIngredients
templateName = ['Cal_Pesticide_Residues_1996_orig.pdf']*nIngredients
    
df = pd.DataFrame({'data_document_id':prodID, 'data_document_filename':templateName, 'doc_date':msdsDate, 'raw_category':recUse, 'raw_cas':casN, 'raw_chem_name':chemName, 'cat_code':catCode, 'description_cpcat': descrip, 'cpcat_code':code, 'cpcat_sourcetype':sourceType})
df=df.drop_duplicates()
df.to_csv(r'L:\Lab\HEM\ALarger\Actor Automated Extraction\California\Cal Pesticide Residues\Cal Pest Residues 1996.csv',index=False, header=True)