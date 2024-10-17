file_path = 'C:/OBLIG3/docs/barnehagedata.xlsx'
import pandas as pd
import altair as alt

df = pd.read_excel(file_path, sheet_name="sheet", header=2)

df.columns = ['Region', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

year_columns = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
df[year_columns] = df[year_columns].apply(pd.to_numeric, errors='coerce')

kommune = 'Longyearbyen'
kommune_data = df[df['Region'] == kommune]

# gjør om dataen for altair
kommune_data_long = kommune_data.melt(id_vars='Region', value_vars=year_columns, 
                                      var_name='År', value_name='Prosent')

chart = alt.Chart(kommune_data_long).mark_bar().encode(
    x=alt.X('År:N', title='År'),  # Years as nominal values on x-axis
    y=alt.Y('Prosent:Q', title='Prosent'),  # Prosent on y-axis
    color=alt.Color('År:N', title='År'),  # Different colors for each year
    tooltip=['År', 'Prosent']
).properties(
    title=f'Prosentandel av barn i ett- og to-årsalderen i barnehagen for {kommune} (2015-2023)'
)

# Gjør diagrammet til en HTML fil for å visualisere den
output_html = 'C:/OBLIG3/docs/Oppgave_G_horizontal.html'
chart.save(output_html)

print(f"Diagram lagret som {output_html}.")

########### Siste Oppgave ############

#fikk problemer med den første raden som hadde årstall så fjerner den
df = df.drop(0)

df_clean = df.dropna(subset=year_columns)

# Beregn prosent for alle kommunene
df_clean['average_prosent'] = df_clean[year_columns].mean(axis=1)

# sorterer dem og setter de 10 øverste opp
top_10_kommuner = df_clean.nlargest(10, 'average_prosent')

# gjør om dataen så det kan brukes med altair
top_10_long = top_10_kommuner.melt(id_vars='Region', value_vars=year_columns,
                                         var_name='År', value_name='Prosent')

# Lage en barchart, ChatGPT gjorde dete
chart = alt.Chart(top_10_long).mark_bar().encode(
    x=alt.X('Region:N', title='Kommune', sort='-y'),
    y=alt.Y('Prosent:Q', title='Prosentandel (%)'),
    color='År:N',
    tooltip=['År', 'Prosent']
).properties(
    title='Gjennomsnittlig prosentandel av barn i ett- og to-årsalderen i barnehagen (2015-2023) for topp 10 kommuner'
)

# Lagres i en HTML fil som Oppgave_H_HTML
output_html = 'C:/OBLIG3/docs/Oppgave_H.html'
chart.save(output_html)

print(f"Diagram lagret som {output_html}")
