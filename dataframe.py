
import pandas as pd

# dataframe erzeugen
dataframe_1 = pd.DataFrame([100, 200, 300, 400])

# Index setzen
dataframe_2 = pd.DataFrame([100, 200, 300, 400], index=["index1", "index2", "index3", "index4"])

# Spalten benennen
dataframe_3 = pd.DataFrame({"Zahlenwerte_1": [100, 200, 300, 400], "Zahlenwerte_2": [90, 521, 70, 900]},
                           index=["index1", "index2", "index3", "index4"])

# dataframe aus series erzeugen
series_1 = pd.Series([59, 5.2, 101, 134267], index=["Umsatz", "Ergebnis", "Börsenwert", "Mitarbeiter"],
                     name="Airbus")
series_2 = pd.Series([66, -3.5, 114, 156000], index=["Umsatz", "Ergebnis", "Börsenwert", "Mitarbeiter"],
                     name="Boing")

dataframe_4 = pd.DataFrame([series_1, series_2])

# Zeilen und Spalten Tauschen mit transpose()
dataframe_5 = pd.DataFrame([series_1, series_2]).transpose()
