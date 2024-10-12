import gspread as gs
import pandas as pd

# Få tilgang til Google Cloud (gc)
gc = gs.api_key("AIzaSyBKrUqkbU3gsEujXEh8N3uQTN7fM0Dpg3I")
# Laste inn hele regnearket fra Google Drive i variabelen sh (spreadsheet)
sh = gc.open_by_key('1ucR3o1pwXMAuGT57XybkwzFxsq2x3QbKV4Oj_MYsjaQ')
# Velge et spesifikt ark fra regnearket (wsh - worksheet)
wsh = sh.worksheet("KOSandel120000")

# Laste inn data fra wsh i en pandas DataFrame
df = pd.DataFrame(wsh.get_all_records(head=4))

####################################################################################################3

# Funksjon for å finne høyeste prosentandel for 2023
def finn_hoyeste_prosent(data: pd.DataFrame, aar: int) -> dict:
    # Konverter kolonnen for året til numerisk, håndter eventuelle feil
    data[str(aar)] = pd.to_numeric(data[str(aar)], errors='coerce').round(1)
    #høyeste prosentandel
    hoyeste_verdi = data[str(aar)].max()
    #kommunene som har denne høyeste prosentandelen
    hoyeste_kommuner = data[data[str(aar)] == hoyeste_verdi]['Region'].tolist()
    return {'hoyeste_verdi': hoyeste_verdi, 'kommuner': hoyeste_kommuner}

# Tilpass DataFrame med riktige kolonnenavn (antatt fra 2015 til 2023)
df.columns = ['Region', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
# Finn den høyeste prosentandelen for 2023
resultat = finn_hoyeste_prosent(df, 2023)

# Skriv ut resultatet
print(f"Den høyeste prosentandelen i 2023 er {resultat['hoyeste_verdi']}%.")
print(f"Kommuner med høyeste prosentandel: {', '.join(resultat['kommuner'])}")

#################################################################################################

# Funksjon for å finne laveste prosentandel for et spesifikt år
def finn_laveste_prosent(data: pd.DataFrame, aar: int) -> dict:
    """Returner laveste prosentandel og tilsvarende kommuner for et gitt år."""
    # Konverter kolonnen for året til numerisk, håndter eventuelle feil
    data[str(aar)] = pd.to_numeric(data[str(aar)], errors='coerce').round(1)
    
    # Finn laveste prosentandel
    laveste_verdi = data[str(aar)].min()
    
    # Finn kommunene som har denne laveste prosentandelen
    laveste_kommuner = data[data[str(aar)] == laveste_verdi]['Region'].tolist()
    
    return {'laveste_verdi': laveste_verdi, 'kommuner': laveste_kommuner}

# Test for laveste prosentandel i 2023
resultat_laveste = finn_laveste_prosent(df, 2023)

# Skriv ut resultatet
print(f"Den laveste prosentandelen i 2023 er {resultat_laveste['laveste_verdi']}%.")
print(f"Kommuner med laveste prosentandel: {', '.join(resultat_laveste['kommuner'])}")

#########################################################################################################
def hoyeste_gjennomsnitt(data: pd.DataFrame, start_aar: int, slutt_aar: int) -> dict:
    '''Returnerer høyeste gjennomsnitt prosentandel og kommunen for perioden 2015- 2023'''
    #Velg kolonner ig konverter dem til numeriske verdier
    kolonner = [str(aar) for aar in range(start_aar, slutt_aar + 1)]
    data[kolonner] = data[kolonner].apply(pd.to_numeric, errors='coerce')
    data['gjennomsnitt'] = data[kolonner].mean(axis=1)
   
    hoyeste_gjennomsnitt = data['gjennomsnitt'].max()
    hoyeste_kommuner = data[data['gjennomsnitt'] == hoyeste_gjennomsnitt]['Region'].tolist()
    return {'hoyeste_gjennomsnitt': hoyeste_gjennomsnitt, 'kommuner': hoyeste_kommuner}

# test høyeste gjennomsnitt fra 2015 til 2023

resultat_hoyeste = hoyeste_gjennomsnitt(df, 2015, 2023)

# skriv ut resultatet
print(f"Den kommunen med det høyeste gjennomsnittlige andelen fra 2015 til 2023 er' {resultat_hoyeste['hoyeste_gjennomsnitt']}%.")
print(f"Kommuner med høyeste gjennomsnittlig prosentandel: {', '.join(resultat_hoyeste['kommuner'])}")


#########################################################################################################
# Funksjon for å finne kommunen med lavest gjennomsnittlig prosentandel fra 2015 til 2023
def finn_laveste_gjennomsnitt(data: pd.DataFrame, start_aar: int, slutt_aar: int) -> dict:
    """Returner laveste gjennomsnittlige prosentandel og kommunen for perioden."""
    # Velg kolonner for perioden og konverter dem til numeriske verdier
    kolonner = [str(aar) for aar in range(start_aar, slutt_aar + 1)]
    data[kolonner] = data[kolonner].apply(pd.to_numeric, errors='coerce')
    
    # Beregn gjennomsnittet for hver kommune
    data['gjennomsnitt'] = data[kolonner].mean(axis=1)
    
    # Finn laveste gjennomsnitt
    laveste_gjennomsnitt = data['gjennomsnitt'].min()
    
    # Finn kommunen som har dette laveste gjennomsnittet
    laveste_kommuner = data[data['gjennomsnitt'] == laveste_gjennomsnitt]['Region'].tolist()
    
    return {'laveste_gjennomsnitt': laveste_gjennomsnitt, 'kommuner': laveste_kommuner}

# Test for laveste gjennomsnittlige prosentandel fra 2015 til 2023
resultat_gjennomsnitt = finn_laveste_gjennomsnitt(df, 2015, 2023)

# Skriv ut resultatet
print(f"Den laveste gjennomsnittlige prosentandelen fra 2015 til 2023 er {resultat_gjennomsnitt['laveste_gjennomsnitt']}%.")
print(f"Kommuner med lavest gjennomsnittlig prosentandel: {', '.join(resultat_gjennomsnitt['kommuner'])}")
