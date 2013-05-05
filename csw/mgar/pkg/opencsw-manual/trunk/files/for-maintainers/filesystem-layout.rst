-------------------------
OpenCSW filesystem layout
-------------------------

.. highlight:: text

Introduction
------------

OpenCSW installs into an already installed Solaris system, and follows the
general rule of not conflicting with existing Solaris files.

The outermost installation directories are:

* ``/opt/csw`` (base of the hierarchy)
* ``/etc/opt/csw`` (configuration files)
* ``/var/opt/csw`` (data files)

The ``/opt/csw`` directory and everything below is considered read-only. It's
a common practice to set up non-global sparse zones with shared ``/opt/csw``.
In this setup, non-global zones see ``/opt/csw`` as mounted read-only. Any
local state needs to be kept under ``/var/opt/csw``.

Inside the ``/opt/csw`` prefix, the typical hierarchy rules apply. You can
consult the Debian `filesystem hierarchy standard`_ for an overview. A short version is:

* Executables go to ``/opt/csw/bin`` ``/opt/csw/sbin`` ``/opt/csw/libexec``
* Shared libraries go to ``/opt/csw/lib``
* Architecture-independent files go to ``/opt/csw/share``
* Documentation goes to ``/opt/csw/shared/doc``
* Manual pages go to ``/opt/csw/share/man``

What's special about the Solaris directory hierachy, including OpenCSW is the
possibility to include binaries for multiple architectures in a single package.
The standard is to create a subdirectory under ``bin`` named after the processor
architecture name, as returned by the ``isalist`` utility. For example, 32-bit
binaries might be in ``/opt/csw/bin`` and 64-bit Intel binaries would be in
``/opt/csw/bin/amd64``.

.. [#shared-opt-csw]
   `Shared /opt/csw configuration files`_

.. _Shared /opt/csw configuration files:
   http://wiki.opencsw.org/shared-opt-csw-setup

.. _filesystem hierarchy standard:
   http://wiki.debian.org/FilesystemHierarchyStandard
