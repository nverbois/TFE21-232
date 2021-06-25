# TFE21-232# EPL21-232

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#a-propos">A propos</a>
      <ul>
        <li><a href="#développé-avec">Développé avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#guide-de-démarrage">Guide de démarrage</a>
      <ul>
        <li><a href="#prérequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#licence">Licence</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#remerciements">Remerciements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## A propos

Cette application a été concue par deux étudiants ingénieurs belges dans le cadre de leur mémoire. Ce travail a été le fruit d'un partenariat entre l'Université de Louvain-La-Neuve et l'Université d'état d'Haïti. Ce projet a pour mission d'aider la population haïtienne à accéder aux données pluviométriques à l'aide d'une carte interactive du pays affichant les différentes stations pluviométriques. 

Vous trouverez premièrement une carte interactive d'Haïti sur laquelle vous distinguerez les différentes stations répertoriées. Vous aurez aussi l'opportunité de comparer les différentes données présentes sur notre site web et de réaliser des statistiques au travers de tableaux comparatifs et de graphiques qui seront à votre disposition.

### Développé avec

* [Django](https://www.djangoproject.com)
* [Bootstrap](https://getbootstrap.com)
* [PostGreSQL](https://www.postgresql.org)


<!-- GETTING STARTED -->
## Guide démarrage

Les prérequis pour cette application sont légers et se limitent à avoir Make et Docker ( Engine + Compose ) installés au préalable. 

### Prérequis

#### Make

* make ( sous MacOS ou Linux)
  ```sh
  brew install make
  ```
* make ( sous Windows)
  ```sh
  scoop install make
  ```
  
#### Docker Engine
Rendez-vous sur le site officiel de Docker Engine, à l'adresse: https://docs.docker.com/engine/install/. Pour Windows/MacOS, vous pourrez simplement installer l'application Docker desktop, tandis que pour Linux, différents fichiers d'installation (.deb ou .rpm) sont disponibles à l'adresse précédente. 

#### Docker Compose

Enfin, il vous suffira de finir par installer Docker Compose, dont les détails selon les systèmes d'exploitation sont disponibles à l'adresse: https://docs.docker.com/compose/install/. Il s’agit de l’adresse officielle du guide d’installation de Docker Compose.
Un autre lien utile de Compose propre au framework que nous utilisons, Django, est: https://docs.docker.com/compose/django/

### Installation

1. Obtenez une clef d'API gratuite aurpès de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/api-keys/)
2. Clonez le répertoire
   ```sh
   git clone https://github.com/nverbois/TFE21-232.git
   ```
3. Construisez l'application
   ```sh
   Make build
   ```
4. Entrez votre clef d'API dans `EPL21232/settings.py`
   ```py
   SENDGRID_API_KEY = 'ENTREZ VOTRE CLEF API';
   ```

<!-- USAGE EXAMPLES -->
## Utilisation

* Construire l'application (la première fois)
  ```sh
  make build
  ```
  
* Lancer l'application 
  ```sh
  make compose-start
  ```
  
* Arrêter l'application 
  ```sh
  make compose-stop
  ```
  
* Créer un super-utilisateur 
  ```sh
  make compose-manage-py cmd="createsuperuser"
  ```

* Créer les migrations de la base de données 
  ```sh
  make compose-manage-py cmd="makemigrations"
  ```
  
* Appliquer les migrations
  ```sh
  make compose-manage-py cmd="migrate"
  ```
  
* Ouvrir le Shell de PostGreSQL
  ```sh
  docker-compose exec postgres psql -U postgres
  ```
* Lister les volumes de Docker
  ```sh
  docker volume ls
  ```
* Remettre à zéro la base de données
  ```sh
  docker volume rm tfe21-232_db-data
  ```
* Lancer les tests unitaires
  ```sh
  make compose-manage-py cmd="test EPL21232.apps.data.tests"
  ```
  
  

<!-- LICENSE -->
## Licence

Ce projet est distribué sous licence MIT. Consultez la section `LICENSE` pour plus d'informations.



<!-- CONTACT -->
## Contact

Nicolas Verbois - nicolasverbois@student.uclouvain.be

Florian Duprez - florianduprez@student.uclouvain.be

Project Link: [https://github.com/nverbois/TFE21-232](https://github.com/nverbois/TFE21-232)



<!-- ACKNOWLEDGEMENTS -->
## Remerciements
* [Start BootStrap](https://startbootstrap.com/previews/freelancer)
* [Chart.JS](https://www.chartjs.org)
* [OpenLayers](https://openlayers.org)
* [DataTables](https://datatables.net/manual/api)
* [Django Import/Export](https://django-import-export.readthedocs.io/en/latest/)
* [Django Jet](http://jet.geex-arts.com)
* [TinyGraphs](https://www.tinygraphs.com/)
* [Split Date and Time in Excel](https://www.excel-exercise.com/split-date-and-time/)
* [How to quickly convert time to text in Excel](https://www.extendoffice.com/documents/excel/5399-excel-convert-time-to-text-or-number-of-hours-minutes-seconds.html)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)





