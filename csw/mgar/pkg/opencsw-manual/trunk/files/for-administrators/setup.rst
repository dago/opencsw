.. _installation-full-setup:

----------
Full setup
----------

Optional: A few basic packages
==============================

Optional but recommended:

* gzip
* coreutils
* wget


PATH
====

For easy access to OpenCSW programs, put ``/opt/csw/bin`` in front of ``PATH``,
and ``/opt/csw/share/man`` in front of ``MANPATH``. On Solaris 10, you can do
that by editing the ``/etc/default/login`` file, uncomment the ``PATH`` and
``SUPATH`` variables definition, adjust the values as required and log out and
back in.


Symlinks in /opt/csw/gnu
========================

OpenCSW tries to avoid providing binaries which clash with those in
``/usr/bin``. Coreutils get a prefix for all the binary names, e.g. ``cp``
becomes ``gcp``. Some packages provide symlinks with original file names, from
the ``/opt/csw/gnu`` directory, for example ``/opt/csw/gnu/cp`` is a symlink to
``/opt/csw/bin/gcp``. You can put ``/opt/csw/gnu`` in front of your ``PATH``.


Do not set LD_LIBRARY_PATH
==========================

LD_LIBRARY_PATH is an environment variable which can be used to make the
dynamic linker look for shared libraries in specific places. It is not
necessary to set it for OpenCSW binaries. All of them are built with the ``-R``
flag, so each binary itself knows where to look for the shared objects.

You do not need to set LD_LIBRARY_PATH system-wide; and if you do, you will
likely break your system, even to the point of locking yourself out. Some of
the library names clash between ``/usr/lib`` and ``/opt/csw/lib``, and if you
run the Solaris openssh daemon with LD_LIBRARY_PATH set to
``/opt/csw/lib``, ``/usr/lib/ssh/sshd`` will try to load libcrypto from
``/opt/csw/lib`` and fail to start.


Upgrading packages
==================

You need to take care to keep your packages up to date. It doesn't happen
automatically out of the box. To upgrade packages, run::

  pkgutil -U -u -y

To automate this process across multiple hosts, you can use a configuration
management system like puppet.


/etc/opt/csw vs. /opt/csw/etc
=============================

There are two locations where configuration files are stored. This may look
confusing at first, the reason is that we try to support both sparse zones and
full zones as good as possible.  Remember that in a sparse root environment
``/opt`` is shared from the global zone. As a rule of thumb configuration files
which are specific to a zone are kept in ``/etc/opt/csw`` which is also
generally preferred (these are in fact most of the configuration files),
whereas ``/opt/csw/etc`` is used for configuration files which are globally
set. Some packages honour both locations, where the global ``/opt/csw/etc`` is
read first and can be customized by ``/etc/opt/csw``, but this is specific to
the package as not all upstream software allows this easily.

There are some exceptions like Apache, where the configuration files are
historically in ``/opt/csw/apache2/etc``, but these are likely to go away some
time.


pkgutil
=======

pkgutil can use two configuration files:

- ``/etc/opt/csw/pkgutil.conf``
- ``/opt/csw/etc/pkgutil.conf``

This may seem confusing, the reason why there are two is that it is possible to
run OpenCSW in a sparse root environment where ``/opt`` is not writable. In
this scenario you use configurations in ``/opt/csw/etc`` for global settings
and ``/etc/opt/csw`` for zone-specific setting. Both ``pkgutil.conf`` are
identical on installation with all configuration options commented out, so you
can just pick one for now. As a rule of thumb it is recommended to prefer the
more prominent ``/etc/opt/csw``. 


preserveconf
============

Configuration files are usually shipped as template with a ``.CSW`` suffix
which is copied during installation to the native name without the suffix. This
file is meant to be user-adjustable. On package deinstallation or update the
template is deinstalled whereas the configuration file without suffix is kept
unless it hasn't been modified.

