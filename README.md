# TFE21-232# EPL21-232

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#about-the-project">A propos</a>
      <ul>
        <li><a href="#built-with">Développé avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Guide de démarrage</a>
      <ul>
        <li><a href="#prerequisites">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## A propos

### Développé avec

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prérequis

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)

Développement d'une application Web pour la gestion des donnéess pluviométriques.
Le site web sera développé autour du Framework Django, et utilisera PostGres pour la base de données.

Nous allons créer des instances de Docker Compose afin de faciliter le déploiement de l'application:  
https://docs.docker.com/compose/django/

Docker Engine
Docker Compose

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

https://www.tinygraphs.com/ pour des images de profil générées aléatoirement

Utilisation de django jet afin de rendre la page d'administration du site web plus jolie : https://pypi.org/project/django-3-jet/
  => fix django-import-export compatibility with https://github.com/django-import-export/django-import-export/issues/618

- To lauch the DB Shell :
  sudo docker-compose exec postgres psql -U postgres

- To completely clear the database :
docker volume ls : list all the docker volumes or databases
docker volume rm "name of the database" : removes the specified DB ( in our case, tfe21-232_db-data ) 

- To realise test:
  make compose-manage-py cmd="test EPL21232.apps.data.tests"
