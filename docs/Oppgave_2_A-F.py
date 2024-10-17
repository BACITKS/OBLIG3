import gspread as gs
import pandas as pd
import altair as alt
import altair_viewer as altv


# Få tilgang til Google Cloud (gc)
gc = gs.api_key("AIzaSyBKrUqkbU3gsEujXEh8N3uQTN7fM0Dpg3I")
# Laste inn hele regnearket fra Google Drive i variabelen sh (spreadsheet)
sh = gc.open_by_key('1ucR3o1pwXMAuGT57XybkwzFxsq2x3QbKV4Oj_MYsjaQ')
# Velge et spesifikt ark fra regnearket (wsh - worksheet)
wsh = sh.worksheet("KOSandel120000")

# Laste inn data fra wsh i en pandas DataFrame
df = pd.DataFrame(wsh.get_all_records(head=4))

df.columns = ['Region', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Konverter kolonnene fra 2015 til 2023 til numeriske verdier
df[['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']] = df[['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']].apply(pd.to_numeric, errors='coerce')

# Fjern rader med NaN-verdier i kolonnen for 2023
df_2023 = df.dropna(subset=['2023'])

# Høyeste prosentandel i 2023
hoyeste_verdi_2023 = df_2023['2023'].max()
hoyeste_kommuner_2023 = df_2023[df_2023['2023'] == hoyeste_verdi_2023]['Region'].tolist()
print(f"Den høyeste prosentandelen i 2023 er {hoyeste_verdi_2023}%.")
print(f"Kommuner med høyeste prosentandel: {', '.join(hoyeste_kommuner_2023)}")

# Laveste prosentandel i 2023
laveste_verdi_2023 = df_2023['2023'].min()
laveste_kommuner_2023 = df_2023[df_2023['2023'] == laveste_verdi_2023]['Region'].tolist()
print(f"Den laveste prosentandelen i 2023 er {laveste_verdi_2023}%.")
print(f"Kommuner med laveste prosentandel: {', '.join(laveste_kommuner_2023)}")

# Høyeste gjennomsnitt fra 2015 til 2023
df['gjennomsnitt'] = df[['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']].mean(axis=1)
hoyeste_gjennomsnitt = df['gjennomsnitt'].max()
hoyeste_kommuner_gjennomsnitt = df[df['gjennomsnitt'] == hoyeste_gjennomsnitt]['Region'].tolist()
print(f"Den høyeste gjennomsnittlige prosentandelen fra 2015 til 2023 er {hoyeste_gjennomsnitt}%.")
print(f"Kommuner med høyeste gjennomsnittlig prosentandel: {', '.join(hoyeste_kommuner_gjennomsnitt)}")

# Laveste gjennomsnitt fra 2015 til 2023
laveste_gjennomsnitt = df['gjennomsnitt'].min()
laveste_kommuner_gjennomsnitt = df[df['gjennomsnitt'] == laveste_gjennomsnitt]['Region'].tolist()
print(f"Den laveste gjennomsnittlige prosentandelen fra 2015 til 2023 er {laveste_gjennomsnitt}%.")
print(f"Kommuner med laveste gjennomsnittlig prosentandel: {', '.join(laveste_kommuner_gjennomsnitt)}")

#Gjennomsnitt for alle kommuneri et spesifikt år
aar = '2023'

df[aar] = pd.to_numeric(df[aar], errors='coerce')

gjennomsnitt_for_aar = df[aar].mean()

print(f"Den gjennomsnittlige prosentandelen for alle kommuner i {aar} er {gjennomsnitt_for_aar:.2f}%.")


