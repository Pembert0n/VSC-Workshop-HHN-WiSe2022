# Bitte nicht gleich nach der Lösung surfen!
def sorting(liste):
    size_count = len(liste)
    #Tipp: Es ist sinnvoll durch die Liste zu iterieren
    #Tipp: Die Funktin swap() sollte abgefragt werden, wenn ihr die Zahlen tauschen wollt
    

#Funktion um die Zahlen zu tauschen    
def swap(liste, start, end):
  tmp = liste[end]
  liste[end] = liste[start]
  liste[start] = tmp
sorting_list = [5, 1, 4, 9, 0, 8, 6]
sorting(sorting_list)
print(sorting_list)