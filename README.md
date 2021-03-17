# TFE21-232# EPL21-232
Développement d'une application Web pour la gestion des donnéess pluviométriques.
Le site web sera développé autour du Framework Django, et utilisera PostGres pour la base de données.

Nous allons créer des instances de Docker Compose afin de faciliter le déploiement de l'application:  
https://docs.docker.com/compose/django/

Pour démarrer le site web : 

- make build ( la première fois )
- make compose-start
- make compose-stop ( quand vous voulez terminer les containers docker qui tournent en fond )
- make compose-manage-py cmd="createsuperuser" pour créer un super-utilisateur
- make compose-manage-py cmd="makemigrations" pour créer les migrations
- make compose-manage-py cmd="migrate" pour appliquer les migrations

FrontEnd : bootstrap with https://startbootstrap.com/previews/freelancer

Utilisation de Chart.js pour les graphes en utilisant un CDN 

Utilisation de MapBox et OpenStreetView pour la varte interactive au travers d'un CDN

Utilisation de DataTables, un plug-in pour la bibliothèque jQuery Javascript. Ajoute toutes sortes de fonctionnalités avancées à n'importe quel tableau HTML.
https://datatables.net/manual/api

Utilisation de django-import-export afin de facilement importer des données pluviométriques aux formats csv, xsl, ... ( https://django-import-export.readthedocs.io/en/latest/installation.html#settings )

Utilisation de django jet afin de rendre la page d'administration du site web plus jolie : https://pypi.org/project/django-3-jet/

- To lauch the DB Shell :
  sudo docker-compose exec postgres psql -U postgres

- To completely clear the database :
docker volume ls : list all the docker volumes or databases
docker volume rm "name of the database" : removes the specified DB ( in our case, tfe21-232_db-data ) 
