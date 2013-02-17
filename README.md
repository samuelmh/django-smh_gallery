django-smh_gallery
==================

A simple photo gallery app for the Django web framework.


What is this?
-------------
This project can be understood in two ways:
1.  It is a __Django app__ to show and manage images grouped in galleries.
2.  It is a __web application__ that let you do the previous.
Perfect option for people that just need a simple portfolio page and only want to focus in their work (artists, photographers, designers, painters). 


Features
--------
*   __Gallery view__. A grid of thumbnailed images.
*   __Image view__. Displays the image, title, date, description, and provides social sharing (FB, Twitter, Linkedin).
*   __Management__ of galleries and images through the Django admin.


Technologies used
-----------------
*   [Python][1]: programming language.
*   [Django][2]: web framework.
*   [Bootstrap][3]: front-end framework.
*   [Foundation][4]: for its clearing widget (full screen carousel).


As django app
-------------------------
Deploy the folder smh_gallery as if it were another Django app and include the app in your settings.py.
If you have any doubt, see the example provided in the myapp folder.


As a web application
-------------------------

### First steps, the hard part ###
Download the full project. You should install a Django environment in your computer so you can test the web app locally.
This application uses a database, by default sqlite engine is used, if you want to change it to mysql or other, edit the file myapp/settings.py and set your desired one.

Open a console and go to the root project  folder "django-smh_gallery".
Synchronize/create the database. Type:
`python manage.py syncdb`
It will create the database and will ask you for the admin credentials that will be used in the future.

Run the testing server. Type:
`python manage.py runserver`

You should have the testing web server running, so if you try to open the http://localhost:8000 web, the home page appears.
If you have more questions on how to deploy, install, etc, please take a look to the [Django documentation][2]. The tutorial is pretty nice!


### Configuring the base ###
*   __base.html__
The file myapp/templates/base.html defines de basic template that will be loaded for every page. If you edit the file, you can change manually thing like:
* The title of the page
* The navigation bar sections
* The footer so you can put your copyright message.
* The Bootstrap theme (mainly the colors). See [Boottheme][5] and [Style Bootstrap][6].

*   __Sections__
The first issue you have to face is to define the sections your web will have. In the provided example there are four links: the homepage, my blog (external), a gallery and the about page. With some knowledge of html and the [Bootstrap documentation][3] (see the examples section), you will be able to redefine all.

*   __Defining a internal link__
A internal link is a link to somewhere in your web. I recommend you to follow the examples when defining an internal link:
    1.  Link to the home (exception)
    `<a href="{% url home %}">Home</a>`
    2.  Link to a satic page (not the homepage).
    `<a href="{% url static_section "about_me" %}">About me</a>`
    3.  Link to a gallery.
    `<a href="{% url smh_gallery_gallery "slug of the gallery" %}">My Gallery</a>`
    4.  Link to an image.
    `<a href="{% url smh_gallery_image "slug of the gallery" "slug of the image" %}">My Gallery</a>`
NOTE: the slug is the name the system gives to your gallery, it's based on the name you gave.


### Adding a static page ###
You can define static pages in the folder myapp/templates/ . Just copy one, change the name and edit it. Remember to focus only in the content you want to show, as other things as the navigation bar and the footer are defined in the base.html template.

If you want to link your static page (i.e static.html) somewhere in your app, follow the next example.
`<a href="{% url static_section "static" %}">link to my static page</a>`


### Adding a gallery ###
If you run the provided code out of the box, youll notice that the "My Gallery" link doesn't work. It's done on purpose for this example.

Once your basic layout is set, you can manage your images/galleries via web.
1.  Open the webpage http://localhost:8000/admin/ and sign in with the credentials you set when your synchronized the database. You should see the Django administration page.
2.  Press "Add" on the Galleries row on the Smh_Gallery section.
3.  As name, write "my gallery", the description is up to you. Press Save.
4.  If you look carefully the web, you see a table with the added gallery. the secon column is called slug, thats the name your gallery will be identified with.
5.  If you try your web page, the "My Gallery" link now takes you to an empty gallery. Congratulations.
6.  Open myapp/templates/base.html and see that I had previously linked the gallery for you :P. This is what the slug is used for.


### Adding an image  ###
If you have followed the tutorial, this procedure is similar to the previous one. I trust you'll success on doing it :)

Now you're the master of your portfolio, good luck.


LICENSE
-------
Foundation, Bootstrap and django-thumbs are property of their owners, the resting code is released under the following license.

Copyright (C) 2013  Samuel M.H.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Although the previous is utopic, I want to say tow things.

If you find this software useful, please take into considerating:
*   To give some money to the Wikipedia or an open source project.
*   To pay me a beer if you ever see me or if you don't, to pay a homeless a meal.
*   To donate (time, money, whatever) to charity.
*   To give me your soul (if you are a member tight fisted brotherhood or an idler).


The only restrictions I put on this software are:
*   It MUST NOT be used by any security (militar, police, pacification, liberation, whatever to do with men and weapons) organization.
*   It MUST NOT be used to promote antihuman behaviours (hate, proselitism, racism, xenophobia, etc).


[1]: http://www.python.org/ "Python"
[2]: https://www.djangoproject.com/ "Django"
[3]: http://twitter.github.com/bootstrap/ "Twitter's Bootstrap"
[4]: http://foundation.zurb.com/ "Foundation"
[5]: http://www.boottheme.com/#generatetheme "Boottheme - Bootstrap theme generator"
[6]: http://stylebootstrap.info/ "Stylebootstrap - Bootstrap theme generator"
