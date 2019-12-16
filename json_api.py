import numpy as np
import pandas 
import requests
import json
import matplotlib.pyplot as plt

#########################------API------#########################
def json_api():
	response = requests.get("https://demo4417994.mockable.io/clientes/")

	text = response.json()

	id = []
	razao_social = []
	cidade = []
	uf = []
	segmento=[]
	cityValues=[]

	for i in text:
		 aux = i['cidade']
		 cidade.append(aux)

	a_dict = {'code 1': cidade, 'code 2': cidade}
	a_list = [*a_dict.values()]
	i_len = sum(len(x) for x in a_list)


	#for r in text:
	#	 aux2 = r['razao_social']
	#	 razao_social.append(aux2)

	#for c in text:
	#	 aux3 = c['cidade']
	#	 cidade.append(aux3)

	#for u in text:
	#	 aux4 = u['uf']
	#	 uf.append(aux4)

	#for s in text:
	#	 aux5 = s['segmento']
	#	 segmento.append(aux5)
