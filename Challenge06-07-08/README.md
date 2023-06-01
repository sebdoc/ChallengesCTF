Titre: 

	Challenge web 06-07-08

Catégories:

	- Web
	- Encodage


Introduction:

	Il y a 3 flags cachés dans ces pages webs. Saurez vous garder le rythme?
	
	
Instructions:

	01 - Se rendre dans le répertoire du fichier "app.py".
		
	02 - Exécuter "app.py" avec la commande:
		python app.py
		
	03 - Ouvrir un navigateur web et se rendre à la page indiqué dans le terminal de commandes en prenant soin de bien d'indiquer le port.
		Ex: 127.0.0.1:8181
		
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

Writeup défi 06:

	01 - Sur la page "index.html" faire un clic droit et choisir "Afficher la page source" ou utiliser l'inspecteur.
	
	02 - Le flag est en commentaire.

Writeup défi 07:

	01 - Sur la page "flag2.html" faire un clic droit et choisir "Afficher la page source" ou utiliser l'inspecteur.

	02 - Le flag est dans le code HTML.

Writeup défi 08:
	
	01 - Sur la page "flag3.html" faire un clic droit et choisir "Afficher la page source" ou utiliser l'inspecteur.
	
	01 - Copier la séquence de clignotement entre les braquettes et l'enregistrer dans un fichier texte nommé :"output.txt".
		"off","off","on","on","off","off","off","off","off","off","on","on","off","off","off","on","off","off","on","on","off","off","on","off","off","off","on","on","off","on","off","on","off","off","on","on","off","off","on","on","off","on","on","on","on","off","on","on","off","on","off","on","off","on","off","off","off","on","off","on","off","on","off","on","off","on","off","on","on","on","on","on","off","off","on","on","off","on","off","off","off","off","on","on","off","on","off","on","off","on","off","on","on","on","on","on","off","on","off","off","on","on","off","off","off","off","on","on","off","off","on","on","off","on","off","on","on","on","on","on","off","on","off","on","off","on","off","off","off","on","off","on","off","off","on","off","off","off","on","on","off","off","off","off","off","off","on","on","off","off","off","on","off","off","on","on","off","on","off","on","off","off","on","on","off","off","off","on","off","off","on","on","off","off","on","on","off","on","off","off","on","on","off","on","off","off","on","on","off","off","on","on","off","on","off","on","on","on","on","on","off","on","off","off","off","on","on","off","off","on","off","off","on","on","off","off","off","off","on","on","off","on","off","off","off","on","off","off","off","on","on","on","off","on","on","on","on","on","off","on",
		
	02 - Créer un script python pour transformer les "on" et les "off" en "1" et en "0":
		touch 10.py
		
	03 - Avec votre éditeur de texte favori, copier cette séquence dans le script:
```
with open('output.txt', 'r') as file:
    content = file.read()

# Remplacement des occurrences de '"on",' par 1
content = content.replace('"on",', '1')
# Remplacement des occurrences de '"off",' par 0
content = content.replace('"off",', '0')

with open('binary_output.txt', 'w') as file:
    file.write(content)

print("La conversion est terminée. Le résultat est enregistré dans le fichier 'binary_output.txt'.")
```	
	04 - Ouvrir le fichier "binary_output.txt" et copier la séquence de "1" et de "0" qu'il contient dans la section "Input" du site "https://gchq.github.io/CyberChef/".
		"001100000011000100110010001101010011001101111011010101000101010101011111001101000011010101011111010011000011001101011111010101000101001000110000001100010011010100110001001100110100110100110011010111110100011001001100001101000100011101111101"

	05 - Glisser l'option "FromBinary" dans la "Recipe" et cliquer sur "Bake".

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

Flags:

	01253{8R4V0_V0U5_4V3Z_L3_PR3M13R_FL4G}
	
	01253{W0W_D3UX13M3_FL4G}
		
	01253{TU_45_L3_TR01513M3_FL4G}
