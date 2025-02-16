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
