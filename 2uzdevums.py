  """
    Funkcija koks akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to summas kvadrātu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar diviem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
"""

def koks(a,b,c):
  summa=a+b+c # jāiegūst visu skaitļu summa
  return summa*summa #3 summas kvadrāts

# piemēri --> visi varianti
rezultāts1=koks(1,2,3) # tiek apskatīti veselie skaitļi
rezultāts2=koks(2.5, 3.5, 4.0) # visi sk ar float
rezultāts3=koks(-1, 5,2)

# Datu izvads
print(f"rezultāts 1:{rezultāts1:2f}")
print(f"rezultāts 1:{rezultāts2:2f}")
print(f"rezultāts 1:{rezultāts3:2f}")
