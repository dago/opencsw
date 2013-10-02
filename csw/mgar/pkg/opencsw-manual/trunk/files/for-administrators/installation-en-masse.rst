============================
Installing packages en masse
============================

--------------------
Package dependencies
--------------------

The OpenCSW packages have been compiled to allow easy forward migration and
crossgrades/mixing between SPARC and x86_64 CPUs. That means the same version of the
package is available for Solaris 10 and 11 for both SPARC and x86. There are
some exceptions where the software is absolutely not available or has a version
mismatch (e.g. acroread). To allow this, there are usually no dependencies on
SUNW packages. This sometimes leads to large dependency chains (and people
thinking of OpenCSW packages as bloated) but that is the price to pay for
the interoperability and we feel that in times of ever growing disks the
flexibility is worth more than the saved bytes.

Package dependencies are modeled in the OpenCSW catalogs to allow automatic
dependency resolution via pkgutil. To view the current dependencies for a
package you can use::

  pkgutil --deptree <pkg>


--------------------------------------------------------------
Creating a .pkg file for a host without an Internet connection
--------------------------------------------------------------

If you need to install a package with multiple dependencies on a host with no
Internet access, you can use ``pkgutil`` to prepare a ``.pkg`` file with the
whole dependency chain. This is much easier than copying dependencies one by
one::

  pkgutil \
    --stream \
    --target=sparc:5.10 \
    --output imagemagick-and-others.pkg \
    --yes \
    --download \
    imagemagick coreutils vim ggrep gsed

At the end of the run, ``pkgutil`` displays the correct order to install the
packages in.

The resulting package stream will be placed in the ``~/.pkgutil/packages``
directory.

This topic is also `discussed`_ on the community site.

.. _discussed: http://www.opencsw.org/community/questions/92/installing-without-a-direct-internet-access
