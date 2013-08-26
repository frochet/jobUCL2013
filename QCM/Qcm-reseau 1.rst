.. raw:: html

  <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="js/jquery-shuffle.js"></script>
  <script type="text/javascript" src="js/rst-form.js"></script>
  <script type="text/javascript">$nmbr_prop = 4</script>


=========================
Mission X : The Network Layer, Principles
=========================

Ces questions ont pour objectif de vous permettre de tester vous-même votre compréhension de la matière couverte par cette mission de mise en route.

Ces questions supposent que vous avez lu le cinquième chapitre du syllabus contenant l'introduction à la Network Layer.


Question 1. Shortest Path Tree
------------------------------

Analyse the network given. What is the shortest path tree for the router A?

  .. figure:: ../png/qcm1-1.png
     :align: center
     :scale: 100

.. class:: positive

-
  .. figure:: ../png/Q1-solution1.png 
     :align: center
     :scale: 100
  
-
  .. figure:: ../png/Q1-solution2.png 
     :align: center
     :scale: 100

.. class:: negative

-
 .. figure:: ../png/Q1-mauvais1.png 
     :align: center
     :scale: 100
-
 .. figure:: ../png/Q1-mauvais2.png 
     :align: center
     :scale: 100
 
 .. class:: comment


Question 2. Commande `ls(1)`_
-----------------------------

La commande `ls(1)`_ permet de lister le contenu d'un répertoire. Elle supporte de nombreux paramètres. Parmi les groupes d'affirmation suivants, un seul est valide, lequel ?

.. class:: positive

-
  - Dans un répertoire, la commande ``ls -a`` sans argument permet d'afficher la liste de tous les fichiers et répertoires présents
  - La commande ``ls -d`` permet de lister les répertoires présents dans le répertoire courant
  - La commande ``ls -l`` permet d'obtenir la liste détaillée du contenu du répertoire courant avec toutes les informations relatives à chaque fichier et répertoire


-
  - Dans un répertoire, la commande ``ls -a`` sans argument permet d'afficher la liste de tous les fichiers et répertoires présents
  - La commande ``ls -R`` permet de lister de façon récursive le contenu du répertoire courant et de ses sous-répertoires
  - La commande ``ls -l`` permet d'obtenir la liste détaillée du contenu du répertoire courant avec toutes les informations relatives à chaque fichier et répertoire


.. class:: negative

-
  - Dans un répertoire, la commande ``ls *`` sans argument permet d'afficher la liste de tous les fichiers et répertoires présents
  - La commande ``ls -f`` permet de lister le contenu du répertoire courant sans trier les fichiers par nom
  - La commande ``ls -l`` permet d'obtenir la liste détaillée du contenu du répertoire courant avec toutes les informations relatives à chaque fichier et répertoire

  .. class:: comment

     Relisez la page de manuel de `ls(1)`_. Sous Unix, le shell va remplacer ``*`` par l'ensemble des fichiers présents dans le répertoire courant

-
  - Dans un répertoire, l'appel à `ls(1)`_ sans argument permet d'afficher la liste de tous les fichiers et répertoires présents
  - La commande ``ls -r`` permet de lister de façon récursive le contenu du répertoire courant et de ses sous-répertoires
  - La commande ``ls -l`` permet d'obtenir la liste détaillée du contenu du répertoire courant avec toutes les informations relatives à chaque fichier et répertoire

  .. class:: comment

     Relisez la page de manuel de `ls(1)`_. Sous Unix, l'appel à `ls(1)`_ sans argument dans le shell affichera l'ensemble des fichiers présents dans le répertoire courant



Question 3. Premier programme en langage C
------------------------------------------

Depuis la publication du livre de référence [KernighanRitchie1998]_, le premier programme écrit en langage C affiche à l'écran la chaîne de caractères "Hello, world". Parmi les codes source ci-dessous, un seul est entièrement correct. Lequel ?


.. class:: positive

-
 .. code:: c

    #include <stdio.h>
    int main(int argc, const char *argv[]) {
        printf("Hello, world\n");
    }

-
 .. code:: c

    #include <stdio.h>
    int main(int argc, const char *argv[]) {
        printf("Hello,");
	printf(" world\n");
    }

.. class:: negative

-
 .. code:: c

    #include <stdio.h>
    void main(int argc, const char *argv[]) {
        printf("Hello, world\n");
    }


 .. class:: comment

      En C, contrairement à Java, la fonction ``main`` retourne une valeur de type ``int``.

-
 .. code:: c

    int main(int argc, const char *argv[]) {
        printf("Hello, world\n");
    }


 .. class:: comment

       La fonction `printf(3)`_ utilisée par ce programme fait partie de la librairie standard de gestion des I/O. Pour l'utiliser, il faut inclure le header `stdio.h`_. Même si certains compilateurs pouvaient l'inclure par défaut, il est préférable de spécifier ce header explicitement.

-
 .. code:: c

    #include <stdlib.h>
    int main() {
        printf("Hello, world\n");
    }


 .. class:: comment

    En C, la signature de la fonction ``main`` est ``int main(int argc, const char *argv[])`` même si certains compilateurs peuvent être tolérants. `printf(3)`_ est défini via `stdio.h`_ et non `stdlib.h`_.

-
 .. code:: c

    #include <stdlib.h>
    void main()
        printf("Hello, world\n");
    }


 .. class:: comment

    En C, la signature de la fonction ``main`` est ``int main(int argc, const char *argv[])`` même si certains compilateurs peuvent être tolérants. `printf(3)`_ est défini via `stdio.h`_ et non `stdlib.h`_.


Question 4. Deuxième programme en langage C
-------------------------------------------

Votre deuxième programme en langage C doit afficher à l'écran la chaîne de caractères `SINF1252`. Lequel parmi les programmes ci-dessous affiche-t-il correctement cette chaîne de caractères ?

.. class:: positive

-
 .. code:: c

    #include <stdlio.h>
    int main(int argc, const char *argv[]) {
        int a = 1252;
        printf("SINF%d\n", a);
    }

 .. class:: comment

    En C, la fonction `printf(3)`_ prend un nombre variable d'arguments. Le premier est toujours une spécification de formatage qui indique la chaîne de caractères à afficher. Les autres arguments sont des identifiants de variables dont les valeurs seront utilisées pour construire la chaîne de caractères à afficher. Le deuxième argument remplace le premier format `%d`, le troisième argument le deuxième format, etc. La page de manuel de `printf(3)`_ fournit de nombreux détails sur le fonctionnement de cette fonction qui accepte de nombreux paramètres.

-
 .. code:: c

    #include <stdlio.h>
    int main(int argc, const char *argv[]) {
        int a = 1252;
        printf("SINF");
	printf("%d\n", a);
    }

 .. class:: comment

    En C, la fonction `printf(3)`_ prend un nombre variable d'arguments. Le premier est toujours une spécification de formatage qui indique la chaîne de caractères à afficher. Les autres arguments sont des identifiants de variables dont les valeurs seront utilisées pour construire la chaîne de caractères à afficher. Le deuxième argument remplace le premier format `%d`, le troisième argument le deuxième format, etc. La page de manuel de `printf(3)`_ fournit de nombreux détails sur le fonctionnement de cette fonction qui accepte de nombreux paramètres.

.. class:: negative

-
 .. code:: c

    #include <stdlio.h>
    int main(int argc, const char *argv[]) {
        int a = 1252;
        printf("SINF%a\n", a);
    }

 .. class:: comment

    Dans la fonction `printf(3)`_, ``%a`` est utilisé lorsque l'on veut placer dans une chaîne de caractères un nombre réel en notation hexadécimale. Dans ce cas, ``a`` étant un entier, il aurait fallu utiliser ``%d``.

-
 .. code:: c

    #include <stdlio.h>
    int main(int argc, const char *argv[]) {
        int a = 1252;
        printf(SINF);
	printf(%d\n, a);
    }

 .. class:: comment

    En C, une chaîne de caractères (ou un descripteur de format pour `printf(3)`_ qui est aussi une chaîne de caractères) commence et se termine par le caractère ``"``.

-
 .. code:: c

    #include <stdlio.h>
    int main(int argc, const char *argv[]) {
        int a = 1252;
        printf("SINF$a\n", a);
    }

 .. class:: comment

    Dans la fonction `printf(3)`_ en C, et contrairement à d'autres langages, le caractère ``$`` ne joue pas de rôle particulier. Le programme ci-dessus affichera donc simplement ``SINF$a`` à l'écran.


Question 5. Arguments passés à un programme C
---------------------------------------------

Considérons le programme C ci-dessous qui permet de manipuler les arguments passés en ligne de commande.

        .. code-block:: c

                #include <stdlio.h>
                #include <stdlib.h>
                int main(int argc, const char *argv[])
                {
                        int a = atoi(argv[1]);
                        printf("%d\n", a);
                }

Parmi les groupes d'affirmations ci-dessous, un seul ne contient que des affirmations qui sont toutes vraies. Lequel ?


.. class:: positive

-

  - Lors de l'exécution de la fonction ``main``, ``argc`` est initialisé au nombre d'arguments passés au programme (y compris le nom de l'exécutable lui-même).
  - Lors de l'exécution de la fonction ``main``, le tableau ``argv[]`` contient dans ```argv[0]`` le nom du programme, dans ``argv[1]`` le premier argument, etc.
  - La fonction ``atoi`` permet de convertir une chaîne de caractères en l'entier équivalent.


.. class:: negative

-
  - Lors de l'exécution de la fonction ``main``, ``argc`` est initialisé à zéro.
  - Lors de l'exécution de la fonction ``main``, le tableau ``argv[]`` contient dans ``argv[0]`` le premier argument, dans ``argv[1]`` le second argument, etc.
  - La fonction ``atoi`` calcule la taille de son argument.

  .. class:: comment

     Les trois affirmations sont fausses. ``argc`` sera toujours initialisé à un vu que le nom du programme est toujours passé en argument. Le premier élément du tableau ``argv[]``, ``argv[0]``, est le nom du programme qui est exécuté. Enfin, la fonction ``atoi`` permet de convertir une chaîne de caractères en l'entier équivalent.

-
  - Lors de l'exécution de la fonction ``main``, ``argc`` est le nombre maximum d'arguments que l'on peut lui passer.
  - Lors de l'exécution de la fonction ``main``, le tableau ``argv[]`` contient dans ``argv[0]`` le premier argument, dans ``argv[1]`` le second argument, etc.
  - La fonction ``atoi`` doit prendre comme argument une chaîne de caractères qui ne contient que des chiffres.

  .. class:: comment

     Les deux premières affirmations sont fausses. ``argc`` contient le nombre d'arguments passés effectivement au programme. Le premier élément du tableau ``argv[]``, ``argv[0]``, est le nom du programme qui est exécuté.

-
  - Lors de l'exécution de la fonction ``main``, le tableau ``argv[]`` contient dans ```argv[0]`` le premier argument, dans ``argv[1]`` le second argument, etc.
  - La fonction ``atoi`` permet de convertir une chaîne de caractères en l'entier équivalent.

  .. class:: comment

     Le premier élément du tableau ``argv[]``, ``argv[0]``, est le nom du programme qui est exécuté.

.. include:: ../../../links.rst
.. include:: ../../../man_links.rst
.. include:: ../../../incl_links.rst
