
from datensaetze_importieren import umsatz_1, umsatz_2


# Mit head() die obersten 5 Einträge (default) und mit tail() die untersten 5 Einträge (default) ausgeben
print(umsatz_1.head())
print(umsatz_1.tail())

# Mit head() und mit tail() weitere Einträge ausgeben
print(umsatz_1.head(10))
print(umsatz_1.tail(10))

# Weitere Informationen (class, dtype, RangeIndex, Data columns, memory usage) zu einem dataframe mit info()
print(umsatz_2.info())

# Mit describe() nähere Info zu der Datenstruktur erhalten (Anzahl Datensätze, Durchschnittswerte, Standardabweichung,
# min, 25%, Median, 75%, max)
print(umsatz_1.describe())

# Mit transpose() transponieren...
print(umsatz_2.describe().transpose())

# Mit columns die Spalten abfragen
print(umsatz_2.columns)

# Mit values die Werte in array abfragen
print(umsatz_2.values)

# Mit dtypes die Datentypen abfragen
print(umsatz_2.dtypes)

# Anzahl Zeilen, Spalten mit len() oder shape()
print(len(umsatz_1))
print(len(umsatz_1.columns))
print(umsatz_1.shape)

# Bestimmte Anzahl an Zeilen zufällig ausgeben mit sample(). Mit frag als Parameter prozentuale Anzahl ausgeben.
print(umsatz_2.sample(10))
print(umsatz_2.sample(frac=0.004))
