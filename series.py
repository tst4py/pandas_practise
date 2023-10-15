
import pandas as pd

# Eine Series in pandas ist ein eindimensionales beschriftetes Array, das Daten jeden Typs aufnehmen kann
# (z.B. Integer, String, Floating Point, Python-Objekte, etc.). Die Achsenbeschriftungen werden zusammenfassend
# als Index bezeichnet.

# Das np.nan-Element ist ein spezieller Wert, der "Not a Number" repräsentiert und oft für fehlende Daten
# in pandas verwendet wird.

# Series with different datatypes
series_1 = pd.Series([0.1, 2, 5, 12.8])
series_2 = pd.Series(["gelb", "rot", "schwarz"])
series_3 = pd.Series(["gelb", 2, 28.98, True])

# Series from dictionaries
dict_1 = {"Hamburg": "SPD", "Bayern": "CSU", "Hessen": "CDU"}
series_4 = pd.Series(data=dict_1)

# arrange order with index as argument
series_5 = pd.Series(data=dict_1, index=["Bayern", "Hessen", "Hamburg"])

# index at Series
series_6 = pd.Series(["blau", "violett", "lila", "rot"], index=[100, 200, 300, 400])
