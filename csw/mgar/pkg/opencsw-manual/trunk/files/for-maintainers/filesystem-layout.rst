-------------------------
OpenCSW filesystem layout
-------------------------

.. highlight:: text

Introduction
------------

OpenCSW installs over an already installed Solaris system, and follows the
general rule of not conflicting with existing Solaris files.

The outermost installation directories are:

* /opt/csw (base of the hierarchy)
* /etc/opt/csw (configuration files)
* /var/opt/csw (data files)

The /opt/csw directory and everything below is considered read-only. It's
a common practice to set up non-global sparse zones with shared /opt/csw. In
this setup, non-global zones see /opt/csw as mounted read-only. Any local
state needs to be kept under /var/opt/csw.

.. [#shared-opt-csw]
   `Shared /opt/csw configuration files`_
.. Shared /opt/csw configuration files:
   http://wiki.opencsw.org/shared-opt-csw-setup
