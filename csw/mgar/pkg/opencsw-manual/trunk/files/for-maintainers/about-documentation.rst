------------------------------
About Documentation at OpenCSW
------------------------------

.. highlight:: text

Introduction
------------

There are 5 places for documentation at OpenCSW:

* `OpenCSW wiki`_

  * Optimized for frequent changes.
  * Used for ongoing issues, such as projects in progress.
  * Powered by Wikidot, has own user name space, separate sign-up and login.
 
* `OpenCSW manual`_ (this document is part of it)
 
  * Less frequently changing, but more reviewed and polished documentation.
  * Part of the source code repository.
 
* `GAR documentation`_
 
  * Used for GAR / build system specific documentation.
  * Lives in the GAR project SourceForge area.
  * Uses SourceForge credentials.
 
* `Main OpenCSW website`_
 
  * Used for general project information
  * Lives in the project Wordpress site
  * Own user name space, separate sign-up and login
 
* `Community Q&A`_
 
  * Used for questions from users.
  * Own user name space, separate sign-up and login, but accepts
    Google accounts, Facebook and Twitter.
  * Receives spam, and needs to be cleaned up manually.


Editing documentation
---------------------

Many documentation locations have own user name spaces, and require separate
account applications and approvals. If you're a maintainer and you don't have
permissions to edit the wiki, set up an account on wikidot.com and write to
maintainers@ or ask on the IRC channel to get your user added to the project.

If you're a maintainer and you notice something wrong or missing in any of the
above places, don't leave it broken!  If you're not sure what's supposed to be
in the given piece of documentation, ask on the maintainers@ mailing list or on
IRC.


No documentation is better than wrong documentation
---------------------------------------------------

If you notice a piece of documentation that you know is incorrect or obsolete,
DELETE IT.  Yes, really! Even if you don't know what's supposed to be there, and
deleting is the only thing you can do.

Don't be concerned about losing content ‒ wikis and wordpress are versioned,
and so is the source code repository. We can always recover content if we need
to. Once you've deleted the offending piece of text, ask on maintainers@ or IRC
about given topic and if it's worth documenting, write it down in an
appropriate place (may not be the place where you originally found it).

Moving documentation
--------------------

If a piece of documentation is in a wrong place, move it to the right place.
For example, if you notice the catalog format documentation on the wiki, you
can immediately see that it's in a wrong place. The catalog format is
practically unchanging and therefore should go into the less frequently
changing, more polished section: the manual. Use common sense, if in doubt, ask
on maintainers@.

When you're moving a piece of documentation, create a link from the old place
to the new place, so that web spiders and humans can still find their piece of
documentation, starting at the old location.


What should not be documented?
------------------------------

Some things are just not worth documenting. For example, it doesn't make sense
to create a document with a list of our RESTful URLs. We can link directly to
the list in the source code, which is just as easy to read, and is less likely
to be incorrect.


.. _OpenCSW wiki: http://wiki.opencsw.org/buildfarm
.. _OpenCSW manual: http://www.opencsw.org/manual/
.. _GAR documentation: http://gar.opencsw.org/
.. _Main OpenCSW website: http://www.opencsw.org/use-it/
.. _Community Q&A: http://www.opencsw.org/community/
