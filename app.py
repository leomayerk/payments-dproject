from flask import Flask, render_template, request, redirect, session, flash, url_for
from google.cloud import bigquery
from google.oauth2 import service_account
import numpy as np
import pandas 


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

#------Customer------#
queryC = """
Select *
from `blissful-mile-261203.payments.payments`
order by int64_field_0 desc
limit 10

"""
query_job= client.query(queryC)
resultC = query_job.result()

customerId = []
month1 = []
month2 = []
month3 = []
month4 = []
metric = []

for row in resultC:
	customerId.append(row[0])
	month1.append(row[1])
	month2.append(row[2])
	month3.append(row[3])

df_c = pandas.DataFrame({
	'Cliente ID':customerId,
	'Jan/2019':month1,
	'Fev/2019':month2,
	'Mar/2019':month3,
	'Abr/2019':'',
	'Métricas':'',
})

#------Month------#
queryM = """
Select *
from `blissful-mile-261203.payments.payments`
order by int64_field_0 desc
limit 10

"""
query_job= client.query(queryM)
resultM = query_job.result()

metric = []
month = []
value = []

for row in resultM:
	metric.append(row[0])
	month.append(row[1])
	value.append(row[2])

df_m = pandas.DataFrame({
	'Métrica':metric,
	'Mês':month,
	'Valor':value,
})

#print(df_m.sort_values('customerId',ascending=False).head())

#########################------WEB------#########################
app = Flask(__name__)
app.secret_key = 'flask'

#Rotas
@app.route('/')
def index():
    return render_template('index.html', titulo='Métricas - Minha Empresa')

@app.route('/mensal')
def mensal():
    return render_template('mensal.html', titulo='Métricas Mensais', tables=[df_m.to_html(classes='data')])

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', titulo='Métricas por Cliente', tables=[df_c.to_html(classes='data')])


app.run(debug=True)
