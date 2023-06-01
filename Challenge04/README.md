Titre: 

	Chat-llenge 04


Catégories:

	- Stéganographie
	- Brute force
	- Encodage


Introduction:

	Tu pourrais japper que je ne te donnerais pas le mot de passe.
	
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
	
	01 - Aller sur le site "https://github.com/RickdeJager/stegseek/releases" et télécharger le fichier "stegseek_0.6-1.deb".
		
	02 - Se rendre dans le dossier qui contient le fichier "stegseek_0.6-1.deb" et l'installer avec la commande:
		sudo apt install ./stegseek_0.6-1.deb
	
	03 - Entrer l'url "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt" et télécharger la liste de mot de passe "rockyou.txt".
	
	04 - Pour trouver le mot de passe, exécuter la commande:	
		stegseek roar.jpg rockyou.txt

	05 - Pour extraire le fichier de l'image, exécuter la commande:
		steghide info roar.jpg
		
	06 - Répondre "y".
	
	07 - Entrer la passphrase trouvée: "secret".
	
	08 - Extraire le fichier flag.txt avec la commande:
		steghide extract -sf roar.jpg
		
	09 - Entrer la passphrase: "secret".
	
	10 - Afficher le fichier flag.txt avec la commande:
		cat flag.txt

	11 - Aller sur le site "https://gchq.github.io/CyberChef/" et copié le contenu du flag.txt: "MDEyNTN7UTM0NTRGXzRKNDFIX0Y0MTUwQn0=" dans "Input".
		
	12 - Glisser l'option "from base64" dans recipe et cliquer sur "Bake".
	
	13 - Coller le résultat de "Output": "01253{Q3454F_4J41H_F4150B}" dans "Input" et remplacer "From base64" par "ROT13".
	
	14 - Remplacer la valeur "13" de "ROT13" par "12" et cliquer sur "Bake".

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

	01253{C3454R_4V41T_R4150N}
	
```	
	                   BRAVO!
		                /
         ,_         _,
         |\\.-"""-.//|
         \`         `/
        /    _   _    \
        |    a _ a    |
        '.=    Y    =.'
          >._  ^  _.<
         /   `````   \
         )           (
        ,(           ),
       / )   /   \   ( \
       ) (   )   (   ) (
       ( )   (   )   ( )
       )_(   )   (   )_(-.._
      (  )_  (._.)  _(  )_, `\
       ``(   )   (   )`` .' .'
          ```     ```   ( (`
                         '-'
 ```
