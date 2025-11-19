#  Agent de Débogage Autonome

Ce projet implémente un agent logiciel capable d'automatiser un cycle complet de débogage : détecter une erreur d'exécution dans un script Python, analyser la trace d'erreur à l'aide d'un Grand Modèle de Langage (LLM), appliquer le correctif au fichier source, et valider la réussite.

##  Architecture du Projet

Le système repose sur une boucle d'exécution gérée par trois fichiers principaux :

### 1. `lanceur_executor.py` (L'Exécuteur)
Gère le flux de contrôle : il exécute le script cible, capture les erreurs, appelle l'Agent IA pour l'analyse, réécrit le fichier source avec la correction, et ré-exécute le script pour valider le succès.

### 2. `ai_analyst.py` (L'Agent IA)
Responsable de l'analyse. Il est configuré pour communiquer (en mode simulation pour la démo) avec le LLM afin d'obtenir le correctif sous un format **JSON structuré**.

### 3. `script_bugge.py` (Le Code Cible )
Le script contenant le bug initial (`IndentationError`) destiné à être corrigé. Son contenu est écrasé et mis à jour par le `lanceur_executor.py` lors du processus de correction.

##  Démarrage et Exécution de la Démo

L'objectif de cette démonstration est de voir le système s'auto-corriger en une seule exécution du lanceur.


### 1. Configuration de l'Environnement

On crée et on active un environnement virtuel

### 2. Lancement de l'Agent Débogueur

On exécute le script principal (`lanceur_executor.py`) :

```bash
.venv/bin/python lanceur_executor.py

### 3. Résultat Attendu 

1.  **Échec initial :** Le lanceur détecte une erreur (ex: `IndentationError`) dans le script cible.
2.  **Analyse :** L'Agent IA (en simulation) génère un JSON contenant le code corrigé.
3.  **Correction :** Le fichier `script_bugge.py` est automatiquement écrasé par la version corrigée.
4.  **Validation :** Le lanceur ré-exécute le script mis à jour.
5.  **Succès :** Le programme affiche le message **`🎉 CORRECTION RÉUSSIE !`** et le code final fonctionne (affichage du DataFrame Pandas).

---
###  Note 

* ** Le dossier `__pycache__` n'est pas inclus dans le dépôt. Il contient le bytecode compilé de Python, qui est spécifique à l'environnement local et automatiquement régénéré. Le fichier `.
