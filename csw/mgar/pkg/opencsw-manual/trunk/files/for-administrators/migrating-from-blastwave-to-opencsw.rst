-----------------------------------
Migrating from Blastwave to OpenCSW
-----------------------------------

You cannot mix Blastwave packages with OpenCSW packages.

You need to migrate your packages, which means you need to uninstall all
Blastwave packages and install corresponding OpenCSW packages.

Instructions
------------

Install CSWpkgutil, it provides the admin file required later.

Create a list of currently installed CSW packages (Blastwave uses CSW package
namespace), except CSWwget::

  (cd /var/sadm/pkg; echo CSW*) | tr ' ' '\n' \
    | grep -v CSWwget | grep -v CSWpkgutil \
    > /var/tmp/before-migration.list

Configure pkgutil to use an OpenCSW mirror.  Do you have 2 copies of
pkgutil.conf, one in ``/opt/csw/etc`` and one in ``/etc/opt/csw``? Make sure
you only have one copy, use ``/etc/opt/csw`` as the location::

  opencsw_mirror="http://mirror.opencsw.org/opencsw/unstable/"
  cp /etc/opt/csw/pkgutil.conf /etc/opt/csw/pkgutil.conf.bak
  gsed -e '/^\s*mirror=/d' -i /etc/opt/csw/pkgutil.conf
  echo >> /etc/opt/csw/pkgutil.conf "mirror=${opencsw_mirror}"

Uninstall all the packages from the list.  In order to uninstall all the
packages in a batch mode, we need to use a so called admin file.  There's one
provided by CSWpkgutil, ``/var/opt/csw/pkgutil/admin``

::

  for pkg in `cat /var/tmp/before-migration.list`; do \
    pkgrm -n -a /var/opt/csw/pkgutil/admin $pkg; \
  done

Update pkgutil's catalog cache::

  pkgutil -U

Create a new list of packages to install.  Some packages have been renamed and
the package names aren't exactly the same in OpenCSW as in Blastwave. You can
compare the list of packages against a catalog file to figure out which exact
packages you need::

  cp /var/tmp/before-migration.list /var/tmp/after-migration.list

Use pkgutil to install the packages from the new list::

  for pkg in `cat /var/tmp/after-migration.list`; do \
    pkgutil -y -i $pkg; \
  done
