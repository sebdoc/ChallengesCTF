Titre: 

	Challenge difficile raid 05


Catégories:

	- forensic


Introduction:

	J'ai inscris mon flag dans un fichier PDF que j'ai mis dans un raid 5 à 3 disques mais je crois qu'il y en a un de brisé.
	
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
	
	01 - Se rendre dans le dossier qui contient les 3 disques.
	
	02 - On voit qu'un des disques n'est pas de la même taille que les autres. Il faut recréer le 3e disque et le raid 5 pour retrouver le flag caché.
		Supprimer "disk3.img".
		
	03 - Créer un script python nommé "exploit.py" avec la commande:
		touch exploit.py
		
	04 - Éditer le fichier "exploit.py" avec vim parce que c'est le meilleur éditeur de texte/IDE. Entrez la commande:
		vim exploit.py
		
	05 - Appuyer sur "i" et copier le script qui suit à l'intérieur.
```	
from pwn import *

#read the 2 working disks
disk1 = read('disk1.img')
disk2 = read('disk2.img')

#xor to recover disk3 form the RAID 5 array
disk3 = xor(disk1, disk2)

#save the recovered disk
write('disk3.img', disk3)
```
	06 - Enregistrer le script en faisant "Esc", ":qw" et "Enter".
	
	07 -  installer python avec la commande:
		sudo apt install python -y
		
	08 - Installez le module "pip" avec la commande:
		pip install pwntools
		
	09 - Exécuter le script avec la commande:
		python exploit.py 

	10 - Créer les loops pour chaques disques avec les commandes:
		sudo losetup /dev/loop1 disk1.img
		sudo losetup /dev/loop2 disk2.img
		sudo losetup /dev/loop3 disk3.img
		
	11 - Refaire fonctionner le raid 5 avec la commande:
		sudo mdadm --create --level=5 --raid-device=3 /dev/md0 /dev/loop1 /dev/loop2 /dev/loop3

	12 - Créer le dossier qui acceuillera le raid avec la commande:
		sudo mkdir /mnt/raid

	13 - Monter le raid dans le dossier avec la commande:
		sudo mount /dev/md0 /mnt/raid/

	14 - Retrouver le fichier PDF perdu dans le dossier "/mnt/raid".
	
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

	01253{UN_VR41_D15QU3_F4NT0M3}
	
