# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:53:05 2021

@author: Directo
"""

import pandas as pd
import matplotlib.pyplot as plt

#***********************SIP*******************
cpct=pd.read_csv('coppelcat29112021.csv')

cpctSIP=cpct.drop(['Country','Customer','LMC','CustSIPDefinition','TotalMinutes','AnsweredCalls',
                    'ASR','ABR','ACD','PDD','AnsweredCalls','TotalMinutes'], axis=1)

cpctSIP['CustSIPCause']=cpctSIP['CustSIPCause'].replace([0,500,408,400,403,410,415,433,484,486,488,501,502,504,603,606,604],503)

cpctSIP.set_index('CustSIPCause',inplace=True)

sipTotal=cpctSIP['Attempts'].sum()

sip200=(cpctSIP.loc[[200],['Attempts']].sum())
porce200=(sip200/sipTotal*100)

sip480=(cpctSIP.loc[[480],['Attempts']].sum())
porce480=(sip480/sipTotal*100)

sip487=(cpctSIP.loc[[487],['Attempts']].sum())
porce487=(sip487/sipTotal*100)

sip404=(cpctSIP.loc[[404],['Attempts']].sum())
porce404=(sip404/sipTotal*100)

sipOtras=(cpctSIP.loc[[503],['Attempts']].sum())
porceOtras=(sipOtras/sipTotal*100)

porceSipTotal=porce200+porce480+porce487+porce404+porceOtras

sipData= {'CAUSA SIP':['200 Conectada','480 Fuera de servicio','487 Abandonada','404 No existe','Otras causas','Total general'],
          'INTENTOS':[int(sip200),int(sip480),int(sip487),int(sip404),int(sipOtras),int(sipTotal)],
          'PORCENTAJE':[float(round(porce200,2)),float(round(porce480,2)),float(round(porce487,2)),float(round(porce404,2)),float(round(porceOtras,2)),float(round(porceSipTotal))]}

sipCause=pd.DataFrame(sipData)
#sipCause.to_csv('CoppelCatSIP.csv', index=False)

traficSip = ['200 Conectada','480 Fuera de servicio','487 Abandonada','404 No existe','Otras causas']
Inten = [int(sip200),int(sip480),int(sip487),int(sip404),int(sipOtras)]
colores = ['#3498db','#e74c3c','#a9a9a9','#ffcc00','#009933']
plt.pie(x=Inten, labels=None, colors = colores, explode = (0.1,0.1,0.1,0.1,0.1), 
        startangle=90, radius=1.2, autopct='%1.2f%%', shadow=True)
plt.legend(traficSip,bbox_to_anchor=(1.5, 0.65))
plt.title('Causas SIP Globales', weight='bold', size=14)
#plt.savefig('TraficoSIP'+'.png')
plt.show()
