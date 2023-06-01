Titre: 

	Chat-llenge 01


Catégories:

	- Sténographie


Introduction:

	Le chatton est caché dans une jambe de pantalons.
	Pourrez-vous trouver ce qu'il s'y cache d'autre?
	
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
		`
		sudo apt install steghide -y
		`

	02 - Se rendre dans le dossier qui contient l'image chatton.jpg
	
	03 - Pour voir s'il y a quelque chose de caché dans l'image, exécuter la commande:	
		`steghide info chatton.jpg`

	04 - Répondre "y".
	
	05 - Laisser la passphrase vide. Appuyer sur "Enter".
	
	06 - Extraire le fichier secret.txt avec la commande:
		`steghide extract -sf chatton.jpg`
		
	07 - Laisser la passphrase vide. Appuyer sur "Enter".
	
	08 - Afficher le fichier secret.txt avec la commande:
		`cat secret.txt`


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

	01253{74_B34UT3_C4CH33}
