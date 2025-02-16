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
