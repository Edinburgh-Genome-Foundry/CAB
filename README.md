<p align="center">
<img alt="CAB Logo" title="CAB Logo" src="https://github.com/Edinburgh-Genome-Foundry/CAB/blob/master/docs/imgs/CAB-title-small.png" width="400">
</p>
<h2 align="center">CAB - The friendly Computational Application Boilerplate</h2>

[![Build Status](https://travis-ci.org/Edinburgh-Genome-Foundry/CAB.svg?branch=master)](https://travis-ci.org/Edinburgh-Genome-Foundry/CAB)

CAB is a boiler plate to easily create websites with multiple computational apps.
A computational app consists in a page with a form (which can be interactive), and
some computational algorithm runnning in the backend.

CAB is aimed at scientists and programmers who want to quickly put an algorithm
online behind a user interface. It provides a complete integrated system with a
HTTP proxy, jobs queues, presets for development and production, etc., while only
requiring from the programmer to be familiar with Python and Vue.JS.

Below are a few screenshots of CAB out of the box. For an example of website built
with CAB, see [cuba.genomefoundry.org](http://cuba.genomefoundry.org/).

![docker-organization](https://github.com/Edinburgh-Genome-Foundry/CAB/blob/master/docs/imgs/screenshots.png)

## What's inside ?

CAB only uses techologies that are versatile and fun to work with:

- Python and Django in the backend, to run scientific/computational routines.
- Vue.js in the frontend, one of the easiest frameworks to learn and maintain.
- Docker-compose for deploying your app anywhere in just a few lines.

![docker-organization](https://github.com/Edinburgh-Genome-Foundry/CAB/blob/master/docs/imgs/plan.png)

This comes with the following advantages:

- Creating a new app is super simple: just add one file in the front end (for
  the input form) and one file in the back-end (the code for computations).
- Full live-reload ! The changes you make to your backend or frontend code
  take effect immediately. No need to refresh a page or restart a server by hand.
- Plenty of easy-to-use library of components to build your user interface without
  headache, using [Element](http://element.eleme.io/#/en-US).
- Works on any nachine: one-line install, one-line deploy. No
  clash with the rest of your system since everything runs inside containers.


## User Guide

Developing with CAB app requires a good familiarity with Python, Vue, and
base knowlege of Docker and Git.

### Getting started

The next steps will download, install, and launch CAB on your computer.

1. Install ``docker`` and ``docker-compose`` on your machine. This step depends
   on your machine (Windows, Linux, MacOS) so you'll need to google it.

2. Download CAB from Github:

```
git clone git+github.com/Edinburgh-Genome-Foundry/CAB.git
```

3. Go to the root ``CAB/`` directory (the one containing this README and the
   ``docker-compose.yml``) and launch your application in development mode. The
   first time you try this, Docker will download and build a lot of things,
   which may take several minutes. It will only take a few seconds the next
   times you run this command.

```
docker-compose up
```

4. Go to your browser and type ``localhost`` or ``127.0.0.1`` in the address bar.
   You should see the website appear. the console in which you launched
   ``docker-compose`` will keep printing logs of the different components
   (django, vue) so you can keep track and debug.

### Creating a new app

The next steps will add a new app to the CAB project.

1. Go to ``frontend/src/components/scenarios`` and create a new scenario view
   with a form, for instance by duplicating the file
   [ExampleScenario.vue](https://github.com/Edinburgh-Genome-Foundry/CAB/blob/master/frontend/src/components/scenarios/ExampleScenario.vue).

2. Register your scenario in file ``scenarios.js`` (in the same folder)
   by adding ``require('./ExampleScenario')`` under the category you want.
   You should now see your new scenario in the home page and the menu of the
   website.

3. Next we will add some backend computations to process the form and return a
   result. First go to ``backend/app/views`` and create a new folder
   on the model of [``/example_scenario``](https://github.com/Edinburgh-Genome-Foundry/CAB/tree/master/backend/app/views/example_scenario).

4. Register the scenario in ``backend/app/views/__init__.py`` by adding

```
from .example_scenario import ExampleScenarioView
```

5. Register the URL by adding the following line at the end of
   ``backend/website/urls.py``:

```
url(r'^api/start/example_scenario$',
      views.ExampleScenarioView.as_view()),
```

6. That's it. You now have a new app with frontend and backend !

### Deploying the website on the web

The next steps will put your website on the web. Note that many other deployment
workflows are possible.

1. Get a hosting server (for instance from Amazon Web Services or Digital Ocean).
   Get the IP address of this server (we'll assume it is ``123.12.123.123``).

2. Log in this server (``ssh root@123.12.123.123``) and install Docker and
   Docker-Compose (some Digital Ocean servers come with these already installed).

3. From your computer, in the CAB root directory, run the following command to
   create a code repository on the distant server, and register that distant
   repository under the name ``prodserver``

```
./init_remote_git.sh root@123.12.123.123 CAB prodserver
```

4. On the remote server, in the folder ``CAB.git``, start the website in
   production mode:

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

5. Wait some time and go in your browser at the address ``123.12.123.123``,
   your website should be live !

Every time you want to update the website, from your computer in the CAB root
directory run ``git push prodserver master``. You will need to rebuild the
containers on the server if you have modified the frontend or added dependencies
to the backend (we may simplify this later).

Developer's guide
------------------

This section (to be expanded) will provide insights on CAB, for developers willing
to hack or extend the boilerplate. Right now we can give this nice map of the
``docker-compose`` integration:

![docker-organization](https://github.com/Edinburgh-Genome-Foundry/CAB/blob/master/docs/imgs/composition.png)


Licence
-------

CAB is an open source software originally written at the [Edinburgh Genome Foundry](http://genomefoundry.org/) by [Zulko](https://github.com/Zulko)
and released on [Github](https://github.com/Edinburgh-Genome-Foundry/CAB) under
the MIT licence (¢ Edinburgh Genome Foundry). Everyone is welcome to contribute !

If you publish an app made with CAB, you can licence your own code under any
other licence and copyright, e.g. by placing the terms of the licence on top of
each new file you create (this will typically be one file in the frontend and one
file in the backend).
