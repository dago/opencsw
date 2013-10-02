--------------------------
Building a package catalog
--------------------------

When to build your own catalog
------------------------------

In short, any time you have a set of packages you want to install with
pkgutil, but there isn't an existing catalog that provides you with the right
mix. The typical cases include:

#. You've built a set of packages and you want to test them.
#. You want to pick a subset of packages from an existing catalog on the
   mirror.
#. You want to install older versions of some packages, for instance pick a few
   packages from the old package stash (``allpkgs``) and some other, newer
   packages.
#. You have a set of packages internal to your company that you want to
   distribute across your servers.

How to build your own catalog
-----------------------------

Make sure you've installed the ``pkgutilplus`` package. It contains the
``bldcat`` utility. You can use it to create a local catalog containing
your package::

  catalog_root=${HOME}/opencsw-catalog
  catalog_path=${catalog_root}/$(uname -p)/$(uname -r)
  cp /path/to/your_package.pkg ${catalog_path}
  bldcat ${catalog_path}

Once this is done, you can instruct ``pkgutil`` to install packages from
it. You can either serve the root catalog directory over HTTP, or you
can refer to a local filesystem path::

  sudo pkgutil -t file://${catalog_path} -y -i your_package

If you create a persistent local catalog, you can add the path or URL to
``/etc/opt/csw/pkgutil.conf``.

More details on catalog building
--------------------------------

``bldcat`` is relatively a simple perl script which parses your packages in
a directory and builds a catalog for them. The one argument is the directory
to parse for ``*.pkg.gz`` files and the ``catalog`` file is put in the same
directory together with the ``descriptions`` of all packages::

  $ bldcat .
  Inspecting ./xv-3.10a,REV=2008.10.17-SunOS5.8-sparc-CSW.pkg.gz
  $ ls -l
  -rw-r--r--   1 dam      csw          172 May 21 14:22 catalog
  -rw-r--r--   1 dam      csw           53 May 21 14:22 descriptions
  -rw-r--r--   1 dam      csw      1878846 May 21 14:17 xv-3.10a,REV=2008.10.17-SunOS5.8-sparc-CSW.pkg.gz
  $ more catalog
  xv 3.10a,REV=2008.10.17 CSWxv xv-3.10a,REV=2008.10.17-SunOS5.8-sparc-CSW.pkg.gz 83f5619d7daa6678812cc870810042f2 1878846 CSWcommon|CSWtiff|CSWpng|CSWjpeg|CSWzlib none none
  $ more descriptions
  xv - Interactive image display and manipulation tool

The script is a part of the pkgutilplus (CSWpkgutilplus) package.

Checking the catalog
--------------------

There's also a simple check that the catalog is correct. It checks that
every line is eight fields and that the dependency and category fields
begin and end with chars. It also warns if packages are not compressed
(normal for gzip and pkgutil). It also checks for duplicates.

Test run on a manipulated catalog::

  # chkcat /var/opt/csw/pkgutil/catalog
  Skipping signature.
  Skipping comment.
  Skipping comment.
  Skipping comment.

  ERROR! 7 fields instead of normal 8.
  2.2.4,REV=2008.10.01 CSWlibtoolrt libtool_rt-2.2.4,REV=2008.10.01-SunOS5.8-sparc-CSW.pkg.gz 72ae2f64521df6e18b7d665bbf11e984 82427 CSWisaexec|CSWcommon none

  ERROR! 7 fields instead of normal 8.
  rubydoc 1.8.7,REV=2008.09.19_p72 CSWrubydoc rubydoc-1.8.7,REV=2008.09.19_p72-SunOS5.8-i386-CSW.pkg.gz d47700240d7c675e5f843b03a937c28e 3032323 none
  WARNING! Package CSWrubytk is not compressed.
  rubytk 1.8.7,REV=2008.09.19_p72 CSWrubytk rubytk-1.8.7,REV=2008.09.19_p72-SunOS5.8-i386-CSW.pkg 2215ac92175922c593245ef577e92fc9 317259 CSWruby|CSWtcl|CSWtk|CSWcommon none


  WARNING! Package CSWrubytk is not compressed.
  rubytk 1.8.7,REV=2008.09.19_p72 CSWrubytk rubytk-1.8.7,REV=2008.09.19_p72-SunOS5.8-i386-CSW.pkg 2215ac92175922c593245ef577e92fc9 317259 CSWruby|CSWtcl|CSWtk|CSWcommon none

  ERROR! The category field of package CSWspamassassin begins with a non-char.
  spamassassin 3.2.5,REV=2008.10.21 CSWspamassassin
  spamassassin-3.2.5,REV=2008.10.21-SunOS5.8-i386-CSW.pkg.gz
  e5bd858be4a67023b02ee1e5e760295b 896877
  CSWosslrt|CSWperl|CSWpmarchivetar|CSWpmdbi|CSWpmdigestsha1|CSWpmiosocketinet6|CSWpmiosocketssl|CSWpmiozlib|CSWpmipcountry|CSWpmldap|CSWpmlibwww|CSWpmmaildkim|CSWpmmailspf|CSWpmmailtools|CSWpmmimebase64|CSWpmnetdns|CSWpmuri|CSWpmhtmlparser|CSWzlib|CSWcommon
  +none

  ERROR! The dependency field of package CSWxv ends with a pipe char.
  xv 3.10a,REV=2008.10.17 CSWxv xv-3.10a,REV=2008.10.17-SunOS5.8-i386-CSW.pkg.gz 9de3c40048fc8c9f79616ee388fc98f1 1731846 CSWcommon|CSWtiff|CSWpng|CSWjpeg|CSWzlib| none

  Skipping signature. Exiting.

The script is a part of the pkgutilplus (CSWpkgutilplus) package.
