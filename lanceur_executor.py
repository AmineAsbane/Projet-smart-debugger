import subprocess
import json
import os
from ai_analyst import analyze_and_fix

BUGGY_SCRIPT = 'script_bugge.py'

def execute_script(filename):

    try:
        result = subprocess.run(
            ['python', filename],
            capture_output=True,
            text=True,
            check=True, 
            encoding='utf-8'
        )
        return result.returncode, result.stdout, None
    except subprocess.CalledProcessError as e:
        return e.returncode, None, e.stderr
    except FileNotFoundError:
        return -1, None, "Erreur: Interpréteur 'python' introuvable. Assurez-vous qu'il est dans votre PATH."

def run_bug_fix_agent(code_source, captured_error):
 
    print(" Analyse du problème par l'Agent Groq...")
    
    correction_data = analyze_and_fix(code_source, captured_error)
    
    if not correction_data or 'correction' not in correction_data:
        print(" L'Agent Groq n'a pas réussi à fournir une correction valide.")
        return False

    try:
        correction = correction_data['correction']
        new_code = correction['code']
        description = correction['description']
        
        print(f" Correction proposée (Format JSON):")
        print(json.dumps(correction_data, indent=2, ensure_ascii=False))

        print("\n️ Application du correctif au script...")
        with open(BUGGY_SCRIPT, 'w', encoding='utf-8') as f:
            f.write(new_code)
        
        print(f"️ Fichier {BUGGY_SCRIPT} mis à jour.")
        print(f"Explication de l'IA: {description}")
        return True

    except Exception as e:
        print(f"Erreur critique lors du traitement du JSON ou de l'écriture du fichier: {e}")
        return False


def main():

    print(" Démarrage de l'Agent de Débogage...")
    
    return_code, stdout, stderr = execute_script(BUGGY_SCRIPT)
    
    if return_code == 0:
        print(f" Exécution réussie (Code: 0). Sortie:\n{stdout}")
        return

    
    try:
        with open(BUGGY_SCRIPT, 'r', encoding='utf-8') as f:
            code_source = f.read()
    except FileNotFoundError:
        print(f"Erreur: Le fichier {BUGGY_SCRIPT} est introuvable.")
        return

    print(f" Exécution échouée (Code: {return_code}). Erreur capturée pour l'Agent Groq.")
    print(f"\n--- ERREUR CAPTURÉE (Pour Debug) ---\n{stderr}")
    
    if run_bug_fix_agent(code_source, stderr):
        
        print("\n Tentative de ré-exécution du script corrigé...")
        
        return_code_fixed, stdout_fixed, stderr_fixed = execute_script(BUGGY_SCRIPT)
        
        if return_code_fixed == 0:
            print(f" CORRECTION RÉUSSIE !")
            print(f"Le script s'est exécuté correctement après la correction de l'IA.")
            print(f"Sortie du script:\n{stdout_fixed}")
        else:
            print(f"️ CORRECTION ÉCHOUÉE.")
            print(f"Le script corrigé a encore échoué (Code: {return_code_fixed}).")
            print(f"Nouvelle erreur: {stderr_fixed}")


if __name__ == '__main__':
    main()
