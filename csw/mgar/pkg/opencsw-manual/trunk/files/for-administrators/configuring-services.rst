====================
Configuring services
====================

/etc/opt/csw vs. /opt/csw/etc
-----------------------------

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
+++++++

``pkgutil`` can use **two** configuration files:

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
------------

Configuration files are usually shipped as template with a `.CSW` suffix which
is copied during installation to the native name without the suffix. This file
is meant to be user-adjustable. On package deinstallation or update the
template is deinstalled whereas the configuration file without suffix is kept
unless it hasn't been modified.
