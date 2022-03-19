# Overview

This program stores records of board and card games that a user is interested in. A user can view information about different board and card games that are taken from the board game website, [Board Game Geeks](https://boardgamegeek.com). Users can view a table with all of the games, find games based on their category, or pull up the records for an individual game in the repository. 

Users can add new games to the repository. They can also follow links to websites dedicated to board games. Finally, there is a link to the Admin page that allows users to log in and view the user, group, and game data hosted in the website.

This software was developed as a means of learning more about the Django framework. Through developing this software, I was able to become more familiar with Django's syntax, structure, and capabilities. 

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

* Home - This is the default web page that users are directed to when they first access the program. Users can access other pages from this site through a menu, a sidebar, or through links to individual games in program's database. The individual games listed are created dynamically, and can be changed depending on what games the user adds to the database.
* Add Game - This web page is accessed through the 'Add Game' option on the top menu. This hosts a form that allows users to enter new games into the database.
* Links - This web page is accessed through the 'Links' option on the top menu. This hosts links to the external websites, 'Board Game Geek' and 'Boardgaming'.
* Game List - This web page is accessed through the 'Game List' option on the sidebar. This page displays the Game database table, and dynamically changes based on what games are entered into the table.
* Thematic Games List - This web page is accessed through the 'Thematic Games List' option on the sidebar. This page the data for lists all the games in the Game database table that are listed by BoardGameGeeks as a thematic game. This dynamically changes depending on what games are entered by the user.
* Strategic Games List - This web page is accessed through the 'Strategic Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as a strategic game. This dynamically changes depending on what games are entered by the user.
* War Games List - This web page is accessed through the 'War Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as a war game. This dynamically changes depending on what games are entered by the user.
* Family Games List - This web page is accessed through the 'Family Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as a family game. This dynamically changes depending on what games are entered by the user.
* CGS Games List - This web page is accessed through the 'CGS Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as a CGS game. This dynamically changes depending on what games are entered by the user.
* Abstract Games List - This web page is accessed through the 'Abstract Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as an abstract game. This dynamically changes depending on what games are entered by the user.
* Party Games List - This web page is accessed through the 'Party Games List' option on the sidebar. This page lists the data for all the games in the Game database table that are listed by BoardGameGeeks as a party game. This dynamically changes depending on what games are entered by the user.
* Children's Games List - This web page is accessed through the 'Children's Games List' option on the sidebar. This page lists the data for lists all the games in the Game database table that are listed by BoardGameGeeks as a game for children. This dynamically changes depending on what games are entered by the user.

# Development Environment

This program was developed in Pycharm 2021.3.2 Community Edition using the Django framework.

The following libraries were used to create this software:
* django 4.0.3
* pandas 1.4.1

# Useful Websites

* [Django Documentation and Tutorial](https://docs.djangoproject.com/en/3.0/contents/)
* [TutorialsPoint - Django Tutorial](https://www.tutorialspoint.com/django/index.htm)
* [GeeksforGeeks - Django Tutorial](https://www.geeksforgeeks.org/django-tutorial/)
* [florida web design](http://www.bryantsmith.com/)

# Future Work

* Ability to mass import game data via .csv files
* Graphs or charts displaying game statistics
* Update html and css styles