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
