---------------
Buildfarm setup
---------------

.. highlight:: text

Buildfarm is a set of hosts where you can build Solaris packages. You can
connect Intel and SPARC and build a set of packages with one shell command.

If you prefer a video tutorial instead of a written document, there is
a `packaging video tutorial`_ available. It covers all the steps from a fresh
Solaris 10 install to a built package. It takes about 2-3h to complete.

Prerequisites
-------------

* `basic OpenCSW installation`_, as you would do on any Solaris host where
  you're using OpenCSW packages.
* You need a `local catalog mirror`_ which will allow you to quickly access
  all packages that are in any of OpenCSW catalogs for any Solaris version.
  A typical location is ``/export/mirror/opencsw``.


Base setup
----------

The base setup is enough to build packages but does not allow to automatically
check your packages for errors.

::

    sudo pkgutil -y -i vim gar_dev mgar gcc4core gcc4g++ sudo

Oracle Solaris Studio Compiler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need a compiler. Most of the packages built by OpenCSW use Oracle Solaris
Studio (historically called 'SOS'), which you can `download from Oracle`_. You
want to go with the packaged (non-tar) version. In case you have access to an
Oracle Solaris development tools support contract, please make sure to also
install `the latest Oracle Solaris Studio compiler patches`_. The compilers
should be installed at the following locations:

* Sun Studio 11: ``/opt/studio/SOS11``
* Sun Studio 12: ``/opt/studio/SOS12``
* Sun Studio 12u1: ``/opt/studio/sunstudio12.1``
* Solaris Studio 12u2: ``/opt/solstudio12.2``
* Solaris Studio 12u3: ``/opt/solarisstudio12.3``

You can install multiple versions of SOS on one system. If you have your
compiler installed at a different location you can set it in your ``~/.garrc``
with the following lines:

::

    SOS11_CC_HOME = /opt/SUNWspro
    SOS12_CC_HOME = /opt/studio12/SUNWspro


Installing Oracle Solaris Studio 12
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    cd ss12
    ./batch_installer -d /opt/studio/SOS12 --accept-sla

Installing Oracle Solaris Studio 12u3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    sudo ./solarisstudio.sh --non-interactive --tempdir /var/tmp

Patching the installed compilers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remember to patch the compilers, with PCA or manually (requires a software
service contract from Oracle).

Setup ``~/.garrc``
^^^^^^^^^^^^^^^^^^

Finally, you need to create your personal ``~/.garrc`` configuration file. It
contains your name and e-mail adress, both of which are included in the
metadata of built packages. Further, GAR needs to know where to store
downloaded sources and generated packages.

Here's an example:

::

    # Data for pkginfo
    SPKG_PACKAGER   = Dagobert Michelsen
    SPKG_EMAIL      = dam@example.com
    #
    # Where to store generated packages
    SPKG_EXPORT     = /home/dam/pkgs
    #
    # Where to store downloaded sources
    GARCHIVEDIR     = /home/dam/src
    #
    # Disable package sanity checks by checkpkg if you are building on your
    # own host (checkpkg depends on OpenCSW buildfarm infrastructure)
    ENABLE_CHECK    = 0

In case you are sitting behind a proxy, you would also want to configure this in ~/.garrc.

::

    http_proxy = http://proxy[:port]

You can customize several other things in ``~/.garrc`` which we'll see later.
Do not customize anything which makes the build dependent on your
``~/.garrc``-settings! This includes changing compilers flags, ``PATH``, etc.
This is equally true for ``gar.conf.mk`` - please don't modify it! If you feel
it needs change please subscribe to the `users mailing list`_ and discuss your
change there.

Basic git configuration
^^^^^^^^^^^^^^^^^^^^^^^

Git will be installed as one of dependencies. It is used by GAR to make source
patching easier. Provide basic configuration for git:

::

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

You also need to set up the EDITOR command, because git's expectations don't
match up with the behavior of ``/bin/vi``. Here's an example how to set it to
use vim:

::

    sudo pkgutil -y -i vim
    echo "export EDITOR=/opt/csw/bin/vim" >> ~/.bashrc

Of course, it can be your editor of choice.

Initialize the source tree
^^^^^^^^^^^^^^^^^^^^^^^^^^

As regular user (do not use ``root`` for safety reasons) to be used for
building init your local repository:

::

    mgar init [<path-for-build-recipes>] (defaults to ~/opencsw)

Please make yourself familiar with `mgar`_.

Fetch all the build recipes:

::

    mgar up --all

checkpkg database
-----------------

You can use any database engine supported by sqlobject.  MySQL and sqlite have
been tested.

When using MySQL, you need to create the database and a user which has access
to that database (not covered here).

max_allowed_packet problem in MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since checkpkg stores objects in JSON, it sometimes stores values way bigger
than the default allowed 1MB.  For this to work with MySQL, the following
needs to be present in ``/etc/opt/csw/my.cnf``::

  [mysqld]
     max_allowed_packet=64M

There are packages which require data structures larger than 32MB, hence the
64MB value.

case-insensitive string comparison in MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _C.5.5.1. Case Sensitivity in String Searches:
   http://dev.mysql.com/doc/refman/5.0/en/case-sensitivity.html

MySQL documentation in section `C.5.5.1. Case Sensitivity in String Searches`_
says:

  For nonbinary strings (CHAR, VARCHAR, TEXT), string searches use the
  collation of the comparison operands. For binary strings (BINARY, VARBINARY,
  BLOB), comparisons use the numeric values of the bytes in the operands; this
  means that for alphabetic characters, comparisons will be case sensitive.

In SQLObject, the UnicodeCol column type is translated into VARCHAR, which
results in case-insensitive comparisons.  This makes checkpkg throw file
collision errors between files such as "Zcat.1" and "zcat.1".  In order to
work around this, a case-sensitive collation needs to be used; for example,
latin1_bin.  Collation setting can be altered for certain columns, as
follows::

  ALTER TABLE csw_file MODIFY COLUMN path VARCHAR(900) NOT NULL COLLATE latin1_bin;
  ALTER TABLE csw_file MODIFY COLUMN basename VARCHAR(255) NOT NULL COLLATE latin1_bin;

Before applying these changes, make sure that you're using the same column
settings as the ones in the database.

Configuration
^^^^^^^^^^^^^

The database access configuration is held in ``~/.checkpkg/checkpkg.ini`` or,
in the shared config scenario, in ``/etc/opt/csw/checkpkg.ini``.  The format
is as follows::

  [database]
  
  type = mysql
  name = checkpkg
  host = mysql
  user = checkpkg
  password = yourpassword


Initializing tables and indexes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The next step is creating the tables in the database.

::

  bin/pkgdb initdb

System files indexing
^^^^^^^^^^^^^^^^^^^^^

The following commands will index and import files on the filesystem.  Please
note that you might need to change 'SunOS5.10' and 'sparc' to match your file.

::

  bin/pkgdb system-files-to-file
  bin/pkgdb import-system-file install-contents-SunOS5.10-sparc.marshal

You can notice that there are separate steps: collecting the data and saving
as a file, and importing the data. Why are they separate? You need to collect
data on the host that contains them, but you might import the data on
a different host.

OpenCSW catalog indexing
^^^^^^^^^^^^^^^^^^^^^^^^

Next step, import your OpenCSW catalog mirror::

  bin/pkgdb sync-catalogs-from-tree unstable /home/mirror/opencsw/unstable

Importing the whole catalog takes time, and depending on the speed of your
machine, it can take anything from a few hours to a few days.  The good news
is that you only need to import each package once, and once catalog updates
come in, pkgdb only imports the new packages.

You will need to perform this operation each time the OpenCSW catalog is
updated.  Otherwise your packages will be checked against an old state of the
catalog.

Your database is now ready.

Advanced setup
--------------

The following components are not required, but are quite useful.

* pkgdb-web (with Apache) is a web app on which you can browse your package
  database and inspect package metadata without having to unpack and examine
  packages in the terminal. Information such as list of files, pkginfo content
  and /usr/ccs/bin/dump output are available on that page.
* system garrc is useful when you have multiple users, for example colleagues
  at work who also want to build packages.
* `Additional setup documented on the wiki`_

  * Java setup
  * Solaris Studio setup if you want to build software with that compiler.
    Many of existing build recipes at OpenCSW use this compiler, not GCC.
  * ssh agent setup for paswordless logins

* catalog signing daemon is useful if you wish to build package catalogs
  locally and sign them with a GPG key.

  * `Catalog signing daemon source code`_

.. _GAR setup:
  http://sourceforge.net/apps/trac/gar/wiki/GarSetup

.. _Additional setup documented on the wiki:
  http://wiki.opencsw.org/buildfarm

.. _local catalog mirror:
  ../for-administrators/mirror-setup.html

.. _basic OpenCSW installation:
  ../for-administrators/getting-started.html

.. _packaging video tutorial:
  http://youtu.be/JWKCbPJSaxw

.. _Catalog signing daemon source code:
  http://sourceforge.net/p/opencsw/code/HEAD/tree/catalog_signatures/

.. _download from Oracle:
.. _Oracle Solaris Studio:
  http://www.oracle.com/technetwork/server-storage/solarisstudio/downloads/index.html

.. _the latest Oracle Solaris Studio compiler patches:
   http://www.oracle.com/technetwork/server-storage/solarisstudio/downloads/index-jsp-136213.html

.. _users mailing list:
   https://lists.opencsw.org/mailman/listinfo/users

.. _mgar:
   http://wiki.opencsw.org/gar-wrapper
