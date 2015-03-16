.. $Id$

-------------------------
Automated release process
-------------------------

The ``csw-upload-pkg`` utility is used to upload packages to OpenCSW catalogs.
By default, it uploads your packages to the unstable catalog. The utility must
be run on the login host.

::

  maciej@login [login]:~ > csw-upload-pkg
  Usage: csw-upload-pkg [ options ] <file1.pkg.gz> [ <file2.pkg.gz> [ ... ] ]

  (..help message...)

Make sure you upload both Intel and SPARC packages in a single call to
``csw-upload-pkg``.

Once your packages are sent, you can verify the state of the checkpkg database
by visiting the web frontend of the checkpkg database [#catalog-list]_ and
inspecting the catalogs you expect your package to be.

The opencsw-future tree [#opencsw-future]_ on the mirror host is updated
a couple times per day. Your uploaded packages will appear there eventually.

In case of problems with the tool, please re-run the tool in debug mode
(``--debug``) and send full output to maintainers@.

Infrastructure
--------------

* Buildfarm - a collection of Solaris zones and hardware hosting them
* Buildfarm database is a MySQL database on the buildfarm, on the mysql
  zone (mysql.bo.opencsw.org)
* Web interface for the buildfarm database http://buildfarm.opencsw.org/pkgdb/
* External REST interface at http://buildfarm.opencsw.org/pkgdb/rest/
* Internal REST interface at http://buildfarm.opencsw.org/releases/
* Master mirror at http://mirror.opencsw.org
* unstable catalog at http://mirror.opencsw.org/opencsw/unstable/
* Source code at https://sourceforge.net/p/gar/code/HEAD/tree/csw/mgar/gar/v2/lib/python/

Uploading a package
-------------------

What happens when you upload a package using csw-upload-pkg, these things
happen:

#. csw-upload-pkg examines the given file name set for correctness

  * It alerts in certain conditions, e.g. a present i386 file but missing sparc file, or an UNCOMMITTED tag

#. csw-upload-pkg runs 'pkgdb importpkg' to make sure that your package's metadata are imported to the buildfarm database
#. csw-upload-pkg queries the external rest interface for package metadata; it verifies that metadata have been uploaded successfully
#. csw-upload-pkg queries the internal rest interface to know whether package data (as opposed to metadata) are uploaded to the master mirror

  * if not yet there, csw-upload-pkg sends a POST request with package data

#. csw-upload-pkg queries the external rest interface for contents of catalogs
#. csw-upload-pkg calculates which packages to insert to which catalogs

  * Depending on the given file set and catalog contents, 5.9 packages may or may not be inserted into 5.10 and 5.11 catalogs

#. csw-upload-pkg sends a sequence of DELETE and PUT queries to the internal rest interface to modify catalogs

Catalog generation
------------------

web zone runs a cron job which wakes up every 3h and performs a set of tasks.
It generates a new unstable catalog from the database, and pushes it to the
master mirror.

* pkgdb is invoked, and it generates a catalog at the given location

  * pkgdb uses a direct MySQL connection

* catalog notifier is run, and sends e-mails to the maintainers of modified packages
* A cron job on unstable9x generates atom feeds for each catalog every hour.

Promoting / copying packages between releases
---------------------------------------------

http://lists.opencsw.org/pipermail/maintainers/2013-July/018220.html mailing list discussion

Automated, runs once a day. Reports are at
http://buildfarm.opencsw.org/package-promotions/promote-packages.html

.. [#catalog-list] `Catalog list in the checkpkg database.
   <http://buildfarm.opencsw.org/pkgdb/catalogs/>`_
.. [#opencsw-future] `opencsw-future catalog tree
   <http://mirror.opencsw.org/opencsw-future/>`_


