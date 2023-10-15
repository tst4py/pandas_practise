
from datensaetze_importieren import umsatz_1, pd

# 2 Varianten, um einzelne Spalten auszuwählen (ist dann kein dataframe mehr, sondern eine series)
column_city = umsatz_1.Stadt
column_city_2 = umsatz_1["Stadt"]

# Mit shape oder len() die gesamten Einträge in einer Spalte zählen
total_per_column = umsatz_1["Stadt"].shape
total_per_column_2 = len(umsatz_1["Stadt"])

# Nur eindeutige Daten pro Spalte ausgeben mit unique()
unique_per_column = umsatz_1["Stadt"].unique()

# Anzahl der eindeutigen Daten pro Spalte mit nunique() oder len()
total_unique_per_column = umsatz_1["Stadt"].nunique()
total_unique_per_column_2 = len(umsatz_1["Stadt"].unique())

# Die größten Daten für eine bestimmte Spalte ausgeben mit nlargest(Anzahl Datensätze, "Spalte")
highest_sales = umsatz_1.nlargest(4, "Umsatz")

# Mehrere Spalten auswählen
two_columns = umsatz_1[["Stadt", "Land"]]

list_of_columns = ["Stadt", "Land", "Umsatz"]
list_of_columns_output = umsatz_1[list_of_columns]


