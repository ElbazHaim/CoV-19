import pandas as pd
import plotly.express as px

df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country=str(input('Welcome to CoV-19 Data by country!\nDefault = Israel\nlist for country list\nEnter country:\n'))
if country == '' :
    country = 'Israel'
elif country == 'list':
    print(list(df_confirmed['Country/Region']))

isr=df_confirmed[df_confirmed['Country/Region'] == country] # get only data about israel
id_num = int(str(isr.index)[((str(isr.index).find('[')))+1:str(isr.index).find(']')])
isr_T=isr.transpose()                                        # transpose our matrix
isr_T=isr_T.drop(isr_T.index[:4])                            # drop the first lines that aren'y dates.
isr_T=isr_T.rename(columns={id_num: "cases"})                # change the name
isr_T['status']='Infected'
#print(isr_T)

isr_d=df_deaths[df_deaths['Country/Region'] == country] # get only data about israel
id_num_d = int(str(isr_d.index)[((str(isr_d.index).find('[')))+1:str(isr_d.index).find(']')])
isr_d_T=isr_d.transpose()                                        # transpose our matrix
isr_d_T=isr_d_T.drop(isr_d_T.index[:4])                            # drop the first lines that aren'y dates.
isr_d_T=isr_d_T.rename(columns={id_num_d: "cases"})                # change the name
isr_d_T['status']='Dead'
#print(isr_d_T)


isr_r=df_recovered[df_recovered['Country/Region'] == country] # get only data about israel
id_num_r = int(str(isr_r.index)[((str(isr_r.index).find('[')))+1:str(isr_r.index).find(']')])
isr_r_T=isr_r.transpose()                                        # transpose our matrix
isr_r_T=isr_r_T.drop(isr_r_T.index[:4])                            # drop the first lines that aren'y dates.
isr_r_T=isr_r_T.rename(columns={id_num_r: "cases"})                # change the name
isr_r_T['status']='Recovered'
#print(isr_r_T)


for_plotly= pd.concat([isr_T,isr_d_T,isr_r_T])
for_plotly['date'] = for_plotly.index
#print(for_plotly)
fig = px.line(for_plotly, x="date", y="cases", color='status',title=('CoV-19 Data for '+country))
fig.show()