from flask import Flask, render_template, request, redirect, session, flash, url_for
from google.cloud import bigquery
from google.oauth2 import service_account
import numpy as np
import pandas 
import requests
import json
import os
import re
import string
import matplotlib.pyplot as plt
from json_api import json_api 
import unittest
from verify_result import verify_result

app = Flask(__name__)

#########################------BQ------#########################

cred = service_account.Credentials.from_service_account_file(
	'blissful-mile-261203-2e1186bb53ea.json',
	scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(
	credentials=cred,
	project=cred.project_id,
)

payments = client.dataset('payments', project='blissful-mile-261203')

query = """
Select *
from `blissful-mile-261203.payments.payments`
order by int64_field_0
limit 50
"""

query_job= client.query(query)
result = query_job.result()

customerId = []
date = []
value = []
plan = []
month_value_list1 = []
month_value_list2 = []
month_value_list3 = []
month_value_list4 = []
month_value_list5 = []
month_value_list6 = []
month_value_list7 = []
month_value_list8 = []
month_value_list9 = []
month_value_list10 = []
month_value_list11 = []
month_value_list12 = []
month_year_list = []
values_month = []
nmrr_list = []
nmrr_list1 = []
nmrr_list2 = []
nmrr_list3 = []
nmrr_list4 = []
nmrr_list5 = []
nmrr_list6 = []
nmrr_list7 = []
nmrr_list8 = []
nmrr_list9 = []
nmrr_list10= []
nmrr_list11 = []
nmrr_list12 = []
year_list = []
metric = []
values = []
month_list_df = []

for row in result:
	customerId.append(row[0])
	date.append(row[1])
	value.append(row[2])
	plan.append(row[3]) 

	parcel_str = str(plan)[-3]
	price_str = str(value)[-9] + str(value)[-8] + str(value)[-7] + str(value)[-6] + str(value)[-5] + str(value)[-4] + str(value)[-3]
	price_str_1 = str(price_str).replace(",", ".")

	month_value = float(price_str_1) / int(parcel_str)
	init_month_1 = str(date)[-7] + str(date)[-6] + str(date)[-5] 
	init_month = str(init_month_1).replace(",", "")

	year_wr = str(date)[-14] + str(date)[-13] + str(date)[-12] + str(date)[-11] + str(date)[-10] + str(date)[-9]
	year0 = str(year_wr).replace("(", "")
	year1= str(year0).replace(",", "")
	year2= str(year1).replace("e", "")
	year = str(year2).replace(" ", "")
	year_list.append(year)

	#implementar lógica do cliente/ano
	if 1 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value1 = month_value
		month_year1 = "Jan/" + year
		month_value_list1.append(month_value1)
		month_year_list.append(month_year1)
		if 1 == int(init_month):
			new_mrr1 = month_value
			nmrr_list1.append(new_mrr1)

	elif 2 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value2 = month_value 
		month_year2 = "Fev/" + year
		month_value_list2.append(month_value2)
		month_year_list.append(month_year2)
		if 2 == int(init_month):
			new_mrr2 = month_value
			nmrr_list2.append(new_mrr2)

	elif 3 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value3 = month_value 
		month_year3 = "Mar/" + year
		month_value_list3.append(month_value3)
		month_year_list.append(month_year3)
		if 3 == int(init_month):
			new_mrr3 = month_value
			nmrr_list3.append(new_mrr3)

	elif 4 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value4 = month_value 
		month_year4 = "Abr/" + year
		month_value_list4.append(month_value4)
		month_year_list.append(month_year4)
		if 4 == int(init_month):
			new_mrr4 = month_value
			nmrr_list4.append(new_mrr4)

	elif 5 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value5 = month_value 
		month_year5 = "Mai/" + year
		month_value_list5.append(month_value5)
		month_year_list.append(month_year5)
		if 5 == int(init_month):
			new_mrr5 = month_value
			nmrr_list5.append(new_mrr5)
		
	elif 6 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value6 = month_value
		month_year6 = "Jun/" + year
		month_value_list6.append(month_value6)
		month_year_list.append(month_year6)
		if 6 == int(init_month):
			new_mrr6 = month_value
			nmrr_list6.append(new_mrr6)
		
	elif 7 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value7 = month_value 
		month_year7 = "Jul/" + year
		month_value_list7.append(month_value7)
		month_year_list.append(month_year7)
		if 7 == int(init_month):
			new_mrr7 = month_value
			nmrr_list7.append(new_mrr7)
		
	elif 8 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value8 = month_value 
		month_year8 = "Ago/" + year
		month_value_list8.append(month_value8)
		month_year_list.append(month_year8)
		if 8 == int(init_month):
			new_mrr8 = month_value
			nmrr_list8.append(new_mrr8)
					
	elif 9 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value9 = month_value 
		month_year9 = "Set/" + year
		month_value_list9.append(month_value9)
		month_year_list.append(month_year9)
		if 9 == int(init_month):
			new_mrr9 = month_value
			nmrr_list9.append(new_mrr9)
		
	elif 10 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value10 = month_value 
		month_year10 = "Out/" + year
		month_value_list10.append(month_value10)
		month_year_list.append(month_year10)
		if 10 == int(init_month):
			new_mrr10 = month_value
			nmrr_list10.append(new_mrr10)
		
	elif 11 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value11 = month_value 
		month_year11 = "Nov/" + year
		month_value_list11.append(month_value11)
		month_year_list.append(month_year11)
		if 11 == int(init_month):
			new_mrr11 = month_value
			nmrr_list11.append(new_mrr11)
			
	elif 12 in range (int(init_month), int(init_month)+int(parcel_str)):
		month_value12 = month_value 
		month_year12 = "Dez/" + year
		month_value_list12.append(month_value12)
		month_year_list.append(month_year12)
		if 12 == int(init_month):
			new_mrr12 = month_value
			nmrr_list12.append(new_mrr12)			
	else:
		#treat for others months
		month_value13 = 0




#		if month_value1 > month_value12
##			exp_mrr1 = month_value - month_value12
#			exp_list1.append(exp_mrr1)
#
#		if month_value2 > month_value1
#			exp_mrr2 = month_value2 - month_value1
#			exp_list2.append(exp_mrr2)
#
#		if month_value3 > month_value2
#			exp_mrr3 = month_value3 - month_value2
#			exp_list3.append(exp_mrr3)
##
##		if month_value4 > month_value3
#			exp_mrr4 = month_value4 - month_value3
#			exp_list4.append(exp_mrr4)	
#
#		if month_value5 > month_value4
##			exp_mrr5 = month_value5 - month_value4
#			exp_list5.append(exp_mrr5)
#
#		if month_value6 > month_value5
#			exp_mrr6 = month_value6 - month_value5
#			exp_list6.append(exp_mrr6)
#
#		if month_value7 > month_value6
#			exp_mrr7 = month_value7 - month_value6
#			exp_list7.append(exp_mrr7)
#
#		if month_value8 > month_value7
#			exp_mrr8 = month_value8 - month_value7
#			exp_list8.append(exp_mrr8)
#
#		if month_value9 > month_value8
#			exp_mrr9 = month_value9 - month_value8
#			exp_list9.append(exp_mrr9)
#				
#		if month_value10 > month_value9
#			exp_mrr10 = month_value10 - month_value9
#			exp_list10.append(exp_mrr10)
##			
#		if month_value11 > month_value10
#			exp_mrr11 = month_value11 - month_value10
#			exp_list11.append(exp_mrr11)
#
	#	if month_value12 > month_value11
	#		exp_mrr12 = month_value12 - month_value11
	#		exp_list12.append(exp_mrr12)
 



for month in set(month_year_list):

	if month == month_year1:
		mrr = sum(month_value_list1)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list1)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year2:
		mrr = sum(month_value_list2)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list2)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year3:
		mrr = sum(month_value_list3)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list3)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year4:
		mrr = sum(month_value_list4)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list4)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year5:
		mrr = sum(month_value_list5)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list5)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year6:
		mrr = sum(month_value_list6)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list6)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year7:
		mrr = sum(month_value_list7)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list7)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year8:
		mrr = sum(month_value_list8)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list8)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year9:
		mrr = sum(month_value_list9)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list9)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)
		
	elif month == month_year10:
		mrr = sum(month_value_list10)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)
		
		newnmrr = sum(nmrr_list10)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)

	elif month == month_year11:
		mrr = sum(month_value_list11)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)

		newnmrr = sum(nmrr_list11)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)

	else:
		mrr = sum(month_value_list12)
		values.append(mrr)
		metric.append("MRR")
		month_list_df.append(month)


		newnmrr = sum(nmrr_list12)
		values.append(newnmrr)
		metric.append("New MRR")
		month_list_df.append(month)




df = pandas.DataFrame({
	'Métrica':metric,
	'Mês/Ano':month_list_df,
	'Valor':values,
})

class VerifyTests(unittest.TestCase):
	def test_return_true_when_have_content(self):
		result_is_ok = verify_result(result)
		self.assertTrue(result_is_ok)

	def test_return_false_when_have_content(self):
		result_is_ok = verify_result(result)
		self.assertFalse(result_is_ok)

#########################------JSON------#########################

json_api()

#########################------WEB------#########################
app.secret_key = 'flask'

#Rotas
@app.route('/')
def index():
    return render_template('index.html', titulo='Métricas - Minha Empresa')

@app.route('/mensal')
def mensal():
    return render_template('mensal.html', titulo='Métricas Mensais', tables=[df.to_html(classes='data')])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

