LightningTalksLive
==================

Development for Lightning Talks Live, a site for giving lightning talks online. This is a Hack Day project by the folks at [Lincoln Loop](http://lincolnloop.com).

## Installation

### Project

Install project source::

    virtualenv LTL
    . LTL/bin/activate
    pip install -e git+git@github.com:lincolnloop/LightningTalksLive.git#egg=LightningTalksLive
    cd LTL/src/lightningtalkslive
    pip install -r requirements.txt
    cd LTL
    python manage.py migrate
    python manage.py runserver


[npm](https://www.npmjs.org/) to manage JavaScript dependencies.

### JS dependencies

   npm install -g gulp
   npm install

### Running locally

Use Gulp to build and serve the site locally, and watch for changes:

    $ gulp

### One time build

    $ gulp build
