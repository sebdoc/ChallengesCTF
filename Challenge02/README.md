Titre: 

	Chat-llenge 02


Catégories:

	- Sténographie
	- Observation


Introduction:

	Regardez-le bien, ce petit chatton est vraiment joooli. 
	
```	
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
```  

Writeup:
	
	01 - Installer l'appliation Steghide avec la commande:
		sudo apt install steghide -y

	02 - Se rendre dans le dossier qui contient l'image petit.jpg
	
	03 - Ouvrir l'image petit.jpg et observer qu'il y est inscrit le mot "CUUUTE". 
	
	04 - Pour voir s'il se cache quelque chose dans l'image, exécuter la commande:	
		steghide info petit.jpg

	05 - Répondre "y".
	
	06 - Entrer la passphrase: "CUUUTE".
	
	07 - Extraire le fichier flag.txt avec la commande:
		steghide extract -sf petit.jpg
		
	08 - Entrer la passphrase: "CUUUTE".
	
	09 - Afficher le fichier flag.txt avec la commande:
		cat flag.txt

```	
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  
```

Flag:

	01253{D35_F015_17_F4UT_0B53RV3R}
	
