=================
django-brainstorm
=================

Django app for creating a site with multiple areas to brainstorm ideas.

This app powers http://sunlightlabs.com/ideas/ and other similar sites.

django-brainstorm is a project of Sunlight Labs (c) 2009.
Written by James Turk <jturk@sunlightfoundation.com>.

All code is under a BSD-style license, see LICENSE for details.

Source: http://github.com/sunlightlabs/django-brainstorm/


Requirements
============

python >= 2.4
django >= 1.0

Usage
=====

1. Add 'brainstorm' to your ``INSTALLED_APPS`` setting.
2. Add a reference to ``brainstorm.urls`` somewhere in your urls.py::

   (r'^', include('brainstorm.urls')),  # something that looks like this

3. Login to the django admin and create a subsite.

A subsite has a slug, name, description, theme, and a number of other options.  The important two are theme and slug, slug dictates where the subsite will live and theme specifies the name of a theme template (see `Creating Themes`_ for details)

Creating Themes
===============

A theme is represented by a single django template, currently kept at templates/themes/themename.html

Required Elements
-----------------

The theme must include a content block that will be filled by the page, the theme should also include "idea_form.html" if you wish to use the generic idea submission form.

Example dynamic content block::

    <!-- content -->
    <div>
        <h2 id="secondLogo"><a href="http://mysite.com/subsite/">{{subsite.name}}</a></h2>
        <div id="featureBox">
            <p>project description</p>
        </div>

        <div id="ltColumn">
        {% block content %}
        {% endblock %}
        </div>

        <div id="rtColumn">
        <h3>Submit New Idea</h3>
            {% include "idea_form.html" %}
        </div>
        <div class="clear"></div>
    </div>


Styling the Theme
-----------------

Obviously the styling/design of the static portions of the theme is entirely within the hands of the designer.
There are however a few dynamic sections which typically will need some form of styling.

index
.....

The 'content' block of the index contains two divs: 'div#ideas' and 'div#pagination'.

'div#ideas' contains an list where each li is a pair of div.btnVote and div.voteContent. When a div.btnVote has been voted up it will have the additional class 'voted' to allow for additional styling.

'div.btnVote' contains the link 'a.vote_link' for voting and 'div.votes_counted' for displaying the current vote total.

'div.voteContent' contains an <h3> with the idea title, a div.commentMeta with the idea's submitter/date, and a <p> with the description.


idea
....

The content block of the idea page contains one div: 'div#idea'.

'div#idea' contains a single pair of 'div.btnVote' and 'div.voteContent' (see `index`_ for description of these elements)


(TODO: comments support)
