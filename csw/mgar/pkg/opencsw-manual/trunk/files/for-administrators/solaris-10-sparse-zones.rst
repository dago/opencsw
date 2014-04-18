--------------------------------
Solaris 10 :index:`sparse zones`
--------------------------------

1. set inherit-pkg-dir on ``/opt/csw``
2. install OpenCSW packages in the global zone

When inherited by non-global zones, ``/opt/csw`` is read-only.  Two directories
that might need local (per-zone) modifications are ``etc`` and ``var``.
Instead of using ``/opt/csw/etc`` and ``/opt/csw/var`` (which are read-only),
we use ``/var/opt/csw`` and ``/etc/opt/csw`` instead.

Most packages built after July 2010 support local ``var``.

**Keep all your zones running** when installing packages. Otherwise class
action scripts won't have a chance to run and you'll end up with a broken
installation, e.g. missing configuration files.

**Create users in advance.** Some packages create users on installation, if
these users don't exist already.  Users are created by name, without
controlling what UIDs they get.  If you want to keep UIDs of these users
consistent across all zones, create your users in advance.


Sparse zone with shared ``/usr``
================================

You need to install cswclassutils scripts (CSWcas-*) in the global zone.

Otherwise your setup won't work with OpenCSW packages, because the CSWcas-*
package family installs `class action scripts`_ into /usr. See the
`cswclassutils wants to write in /usr`_ thread for more information. 

.. _class action scripts:
   http://wiki.opencsw.org/cswclassutils-package
.. _cswclassutils wants to write in /usr:
   http://lists.opencsw.org/pipermail/maintainers/2009-December/010638.html


Local mount hack (unsupported)
==============================

If you're using a package which wasn't configured to use ``/etc/opt/csw``
and/or ``/var/opt/csw`` but you still need to have per-zone changes, you can
mount your own, writable ``/opt/csw/etc`` on top of the read only ``/opt/csw``::

  # /etc/vfstab entries
  /path/to/your/local/etc - /opt/csw/etc lofs - yes -
  /path/to/your/local/var - /opt/csw/var lofs - yes -

This is only a hack that might help you with a legacy package, it's not a
supported way of using OpenCSW packages.
