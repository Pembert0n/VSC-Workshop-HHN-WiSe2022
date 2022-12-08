# Bitte nicht gleich nach der Lösung surfen!
def bubblesort(elements):
    swapped = False
    # Tipp damit der die Liste sortiert wird, muss man durch die Liste iterieren
    # Tipp: Manchmal macht es Sinn eine Liste von hinten nach vorne zu iterieren
    # In der Funktion muss später swapped = True vorhanden sein, aber das ist nebensächlich
      
        
        
        if not swapped:
            # Wenn nichts getauscht wurde
            # dann ist die Liste schon sortiert
            return
 
elements = [39, 12, 18, 85, 72, 10, 2, 18]
 
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)