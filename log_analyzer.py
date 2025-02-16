def llegir_fitxer(register.log):
  try:
        with open(register.log, 'r', encoding='utf-8') as fitxer:
            return fitxer.readlines()
    except FileNotFoundError:
        print(f"Error: No s'ha trobat el fitxer {register.log}.")
        return []
    except Exception as e:
        print(f"Error inesperat: {e}")
        return []
      
def comptar_registres(registre):
    return len(registre)

def comptar_per_tipus(registre):
  tipus = {"INFO": 0, "WARNING": 0, "ERROR": 0}
  for linia in registre:
      for clau in tipus.keys():
          if clau in linia:
              tipus[clau] += 1
  return tipus

def comptar_paraula_clau(registre, paraula_clau):
  return sum(linia.lower().count(paraula_clau.lower()) for linia in registre)

def generar_informe(register.log, paraula_clau):
  registre = llegir_fitxer(register.log)
  if not registre:
      return ""
    
  total_registres = comptar_registres(registre)
  tipus_registres = comptar_per_tipus(registre)
  paraula_comptatge = comptar_paraula_clau(registre, paraula_clau)
    
  informe = (f"Informe d'Anàlisi de Fitxer de Registre\n"
             f"---------------------------------------\n"
             f"Nombre total de registres: {total_registres}\n"
             f"Registres per tipus:\n"
             f"\tINFO: {tipus_registres['INFO']}\n"
             f"\tWARNING: {tipus_registres['WARNING']}\n"
             f"\tERROR: {tipus_registres['ERROR']}\n"
             f"Recurrence de la paraula clau '{paraula_clau}': {paraula_comptatge}\n"
             f"---------------------------------------")
    
  return informe
