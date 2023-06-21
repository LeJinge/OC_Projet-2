
# OpenClassrooms - Project 2

Ce projet permet de scraper des données importantes de livres sur le site http://books.toscrape.com et de les classer dans un csv par catégorie. Il vous permet également de télécharger les images de chaque livre et de les classer par catégorie.


## Installation et lancement du script

Prérequis : 
- Python
- Git

Une fois les prérequis installés, placez vous dans un répertoire souhaité puis clonez le repository :
```
git clone https://github.com/LeJinge/OC_Projet-2.gitcd
```

Placez vous dans le dossier Projet_2_Books_To_Scrap puis créez un nouvel environnement virtuel :
```
python -m venv .env
```

Ensuite activez cet environnement virtuel :

Windows :
```
.env\scripts\activate.bat
```

Linux et Mac OS :
```
source .env/scripts/activate
```

Pour finir installer les packages nécessaires :
```
pip install -r requirements.txt
```

Vous pouvez enfin lancer le script:
```
python main.py
```
