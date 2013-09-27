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

* `local catalog mirror`_ which will allow you to quickly access
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

Multi-host setup
----------------

How to set up hosts allowing you to build for both Intel and SPARC
architectures.  At least three servers are needed:

* Solaris 9 Sparc to build 32 bit and 64 bit Sparc binaries
* Solaris 9 x86 to build 32 bit build x86 binaries
* Solaris 10 x86 to build 64 bit x86 binaries

Servers with Solaris 10 Sparc are optional for most of the packages.  However,
there may be packages which rely on private kernel data (like "top") which
needs to be build for each and every Solaris version to run on.

The user homes should be in ``/home/<user>`` and the home directory should be
shared between the build machines. This is important for building x86 packages
as the 32 bit part needs to be build on Solaris 9 and the 64 bit part on
Solaris 10.

Under ``/home/experimental/<project>/`` are project-specific directories with
permissions 0755 which are accessible via
``http://buildfarm.opencsw.org/experimental.html``. ``experimental/`` itself
is 01755 and users are free to create new projects as needed.

There is a `matrix of packages installed on the buildfarm`_.

.. _matrix of packages installed on the buildfarm:
   http://buildfarm.opencsw.org/versionmatrix.html

System-wide garrc
^^^^^^^^^^^^^^^^^

System-wide ``garrc`` is useful when you have multiple users, for example
colleagues at work who also build packages.  It can also contain information
about which hosts are used to build packages for which architectures. Create
the ``/etc/opt/csw/garrc`` file with appropriate content. For example::

  GARCHIVEDIR     = /home/src
  GARCHIVEPATH    = /home/src
  
  SPKG_EXPERIMENTAL = /home/experimental
  
  BUILDHOST_platform-solaris9-sparc-32 = unstable9s
  BUILDHOST_platform-solaris9-sparc-64 = unstable9s
  BUILDHOST_platform-solaris10-sparc-32 = unstable10s
  BUILDHOST_platform-solaris10-sparc-64 = unstable10s
  BUILDHOST_platform-solaris11-sparc-32 = unstable11s
  BUILDHOST_platform-solaris11-sparc-64 = unstable11s
  BUILDHOST_platform-solaris9-i386-32 = unstable9x
  BUILDHOST_platform-solaris9-i386-64 = unstable10x
  BUILDHOST_platform-solaris10-i386-32 = unstable10x
  BUILDHOST_platform-solaris10-i386-64 = unstable10x
  BUILDHOST_platform-solaris11-i386-32 = unstable11x
  BUILDHOST_platform-solaris11-i386-64 = unstable11x
  
  define modulation2host
  $(BUILDHOST_platform-$(GAR_PLATFORM)-$(MEMORYMODEL_$(ISA)))
  endef
  
  PACKAGING_HOST_solaris9-sparc = unstable9s
  PACKAGING_HOST_solaris9-i386 = unstable9x
  PACKAGING_HOST_solaris10-sparc = unstable10s
  PACKAGING_HOST_solaris10-i386 = unstable10x
  PACKAGING_HOST_solaris11-sparc = unstable11s
  PACKAGING_HOST_solaris11-i386 = unstable11x
  
  http_proxy = http://proxy:3128
  frp_proxy = http://proxy:3128
  GIT_USE_PROXY = 1
  
  SOS12_CC_HOME = /opt/SUNWspro


Installing Software
^^^^^^^^^^^^^^^^^^^

All software is archived and available from ``/home/farm`` on the buildfarm.
Make sure you deinstall ``SUNWgmake``. That version is outdated and misses
functions needed by GAR (e.g. abspath).

Install Java Package
++++++++++++++++++++

There are versions of JDK and JRE between Java 1.3 and Java 6 installed in ``/usr``.

* Solaris 9 Sparc: ``cd /usr; for F in java/*sparc*; do sh $F; done``
* Solaris 9 x86: ``cd /usr; for F in java/*i586*; do sh $F; done``
* Solaris 10 Sparc: ``cd /usr; for F in java/*sparc*; do sh $F; done``
* Solaris 10 x86: ``cd /usr; for F in java/*i586* java/*amd64* java/*x64*; do sh $F; done``

Install Sun Studio Compiler
+++++++++++++++++++++++++++

On Solaris 8 the Sun Studio 11 Compiler is installed, on Solaris 9 and 10 both
Sun Studio 11 and 12 is installed. Solaris 10 has also Sun Studio 12u1
installed.

Sun Studio 11
+++++++++++++

::

  cd ss11
  cd /CD1 # Sparc only
  PATH=/usr/j2re1.4.2_17/bin:$PATH ./batch_installer -d /opt/studio/SOS11

Uninstall::

  cd /var/sadm/prod/com.sun.studio_11
  ./batch_uninstall_all

Please note: If you have also Sun Studio 12 installed the installer will
erranously remove some packages from Sun Studio 12 so you may need to
reinstall it after SOS 11 removal.

Sun Studio 12
+++++++++++++

::

  cd ss12
  ./batch_installer -d /opt --accept-sla

Uninstall::

  export PATH=/usr/jre1.6.0_20/bin:$PATH
  cd /opt
  java -cp . uninstall_Sun_Studio_12 -nodisplay -noconsole

Please note: If you have also Sun Studio 11 installed the installer will
erranously remove some packages from Sun Studio 11 so you may need to
reinstall it after SOS 12 removal.

Sun Studio 12u1
+++++++++++++++

Headless installation is a bit more complicated, see
http://docs.sun.com/app/docs/doc/820-7601/gemyt?a=view for details.

Sun Studio Compilers for OpenSolaris
++++++++++++++++++++++++++++++++++++

* Sun Studio 12u1
* Sun Studio Express 11/08
* Sun Studio Express 3/09

See http://developers.sun.com/sunstudio/downloads/opensolaris/index.jsp for details.

Don't forget to patch the compilers, with `PCA`_ or `manually`_.

.. _PCA:
   http://www.opencsw.org/packages/pca

.. _manually:
   http://www.oracle.com/technetwork/server-storage/solarisstudio/downloads/index-jsp-136213.html

Sun Studio for Solaris 11
+++++++++++++++++++++++++

TODO

Adding Users 
^^^^^^^^^^^^

From here on in (Jan 2009), we are trying to keep userids in sync across all
machines. www.opencsw.org is considered the "master".  If a user exists on
www, then an account created from them on other machines, should be made to
match up userids.

There are some older, legacy, non-matched-up accounts. To make it easier to
identify between newer and older accounts, cleanly created accounts are
created in the range 17100-18000.  Older accounts may be migrated/synced into
the range 17000-17099 if desired.

thus, if there is an account created on non-www machines, that is desired to
be non-synced, it should be outside the range of 17000-18000

The normal process for creating accounts across all machines, is that Ben
runs a script on www, which in turn calls scripts maintained by Ihsan and
Dagobert, to create accounts on www and buildfarm machines, respectively.

SSH Agent for each user
^^^^^^^^^^^^^^^^^^^^^^^

It is advised to use a passphrase for the SSH key. This can easily be done by
using the following steps:

Set passphrase on the key::

  ssh-keygen -p -f .ssh/id_dsa

Add this to your .zshrc (or the respective file for your favorite shell)::

  # executed for interactive shells
  if [ "x$HOSTNAME" = "xlogin" ]; then
    if [ -f ~/.ssh-agent ]; then
      source ~/.ssh-agent
    fi
  
    if [ -z "$SSH_AUTH_SOCK" -o ! -w "$SSH_AUTH_SOCK" ]; then
      if read -q '?Start ssh-agent? (y/n) '; then
          ssh-agent -s >~/.ssh-agent              && \
              source ~/.ssh-agent                 && \
              ssh-add
      fi
    fi
  fi

Make sure the ssh agent information is forwarded to trusted machines::

  (echo "Host current*"; echo "\tForwardAgent yes") >> ~/.ssh/config

There are similar methods with keychain available:

* `GPG, agent, pinentry and keychain`_

.. _GPG, agent, pinentry and keychain:
   http://lists.opencsw.org/pipermail/maintainers/2009-December/010732.html

Installing DB2 client
^^^^^^^^^^^^^^^^^^^^^

::

  useradd -u 1007 -g csw -c "DB2 Instance User" -d /export/db2inst1 -s /bin/sh db2inst1
  mkdir /export/db2inst1
  chown db2inst1:csw /export/db2inst1
  cd /opt/IBM/db2/V8.1/instance
  ./db2icrt -s client db2inst1

Installing IBM Informix Client SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  cd clientsdk.4.10.FC1DE.SOL
  ./installclientsdk
    (accept default everywhere)
    Default Install Folder: /opt/IBM/informix

It seems the 32 bit and 64 bit clients can not be installed in the same directory.

Buildfarm web app
-----------------

pkgdb-web is a web app on which you can browse your package database and
inspect package metadata without having to unpack and examine packages in the
terminal. Information such as list of files, pkginfo content and information
about binaries are available on that page.

The checkpkg database also holds information about catalogs.

* Live app on the OpenCSW buildfarm http://buildfarm.opencsw.org/pkgdb/
* Source code:
  * Browse http://gar.svn.sourceforge.net/viewvc/gar/csw/mgar/gar/v2/lib/web
  * Checkout:
    http://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/web

There are specifically two web apps: One is read-only (``pkgdb_web.py``) and
one is read-write (``releases_web.py``).

Catalog generation
------------------

Once you have the buildfarm database, you can generate your own package
catalogs. The main entry point which you can add to cron is the
``opencsw-future-update`` script.

* Source code:
  https://sourceforge.net/p/opencsw/code/HEAD/tree/buildfarm/bin/

Catalog signing daemon
----------------------

Catalog signing daemon is useful if you wish to automatically sign your built
catalogs with a GPG key.

* `Catalog signing daemon source code`_

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
