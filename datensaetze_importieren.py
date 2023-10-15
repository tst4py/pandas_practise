
import pandas as pd
# import openpyxl

# csv Datei importieren
umsatz_1 = pd.read_csv("data/datengrundlage.csv")

# xlsx Datei importieren, nicht vergessen openpyxl in die Umgebung zu importieren
umsatz_2 = pd.read_excel("data/datengrundlage.xlsx")

if "__name__" == "__main__":
    # Die ersten 5 Zeilen ausgeben
    print(umsatz_1.head())
    print(umsatz_2.head())
