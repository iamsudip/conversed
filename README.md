=============================
http://conversed.iamsudip.xyz
=============================

Service Description
-------------------

Find details about people only using email address

api
---

Status check: http://conversed.iamsudip.xyz/status/

TODO
----

Right now the data shown are based on vibeapp.
But API data is very old that needs to be updated.

- [ ] If user has social profiles, scrap the page instantly and update and show the data

- [x] Right now, we are blindly dependent on API calls to vibeapp. We need to store the data to make things faster in our database so that once an email has been updated we won't use call API from the next time

- [ ] New UI for entire webapp

- [x] Right now, redhatcloud idles the hosting service when there is less user. Write a cronjob or ping service that will make sure that the service is running 24/7

References
----------

http://www.html5templatesdreamweaver.com/hover-effects.html

https://www.google.co.in/search?q=image+gallery&gws_rd=cr,ssl&ei=D9OmVIb5Eo3f8AWbi4HwBQ

Setup
-----

First fork & clone the repo.

Now *before creating and entering into virtualenv* make sure you install the following::

We are using *redis* as our database. So you need to install this, follow instructions below:

    $ wget https://github.com/antirez/redis/archive/2.8.19.tar.gz

    $ tar -xvzf 2.8.19.tar.gz

    $ cd 2.8.19

    $ sudo make install

    $ redis-server

    $ [ctrl] + d

I always recommend python-virtualenv for development.

After installing and activating the virtual environment do the following

Install the requirements file::

    $ pip install -r requirements.txt

cd to conversed/conversed locate main.py and run::

    $ python main.py

Happy hacking!

