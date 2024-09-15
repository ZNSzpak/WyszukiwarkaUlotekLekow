import csv, sqlite3

con = sqlite3.connect("RP.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("DROP TABLE leki ;")
cur.execute("CREATE TABLE leki (NazwaProduktuLeczniczego, Ulotka);")# use your column names here

#cur.execute("ALTER TABLE leki DROP COLUMN (Identyfikator Produktu Leczniczego, Nazwa powszechnie stosowana, Rodzaj preparatu, Nazwa poprzednia produktu, Droga podania  Gatunek  Tkanka  Okres karencji, Moc, Postać farmaceutyczna, Typ procedury, Numer pozwolenia, Ważność pozwolenia, Kod ATC, Podmiot1 odpowiedzialny, Opakowanie, Substancja czynna, Nazwa wytwórcy, Kraj wytwórcy, Nazwa importera, Kraj importera, Nazwa wytwórcy importera, Kraj wytwórcy importera, Podmiot odpowiedzialny w kraju eksportu, Kraj eksportu, Charakterystyka, Ulotka importu równoległego, Oznakowanie opakowań importu równoległego);")# use your column names here


with open('Rejestr_Produktow_Leczniczych_calosciowy_stan_na_dzien_20240410.csv','r', encoding='cp437') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin, delimiter=";") # comma is default delimiter
    to_db = [(i['NazwaProduktuLeczniczego'], i['Ulotka']) for i in dr]
    #for row in dr:
     #   print(row['NazwaProduktuLeczniczego'], row['Ulotka'])

cur.executemany("INSERT INTO leki (NazwaProduktuLeczniczego, Ulotka) VALUES (?, ?);", to_db)
con.commit()
con.close()