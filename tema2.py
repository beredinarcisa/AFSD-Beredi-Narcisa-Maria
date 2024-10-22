articol = "Inconștiență dusă la extrem de un tânăr aflat la volanul unui autoturism într-o parcare din Baia Mare. La adăpostul întunericul șoferul având probabil adrenalină în sânge a început să facă drifturi, tulburând liniștea publică. Un cititor al site-ului nostru l-a filmat și a alertat totodată poliția rutieră. Agenții de poliție l-au identificat, l-au amendat și i-au reținut și permisul de conducere."
lungime = len(articol)
jumatate = lungime // 2
prima_parte = articol[:lungime]
a_doua_parte = articol[lungime:]
prima_parte = prima_parte.upper().strip()
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
a_doua_parte = ''.join(c for c in a_doua_parte if c.isalnum() or c.isspace())
rezultatul_final = prima_parte + ' ' + a_doua_parte
print(rezultatul_final)