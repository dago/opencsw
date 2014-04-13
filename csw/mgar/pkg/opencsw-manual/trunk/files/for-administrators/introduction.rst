---------------------------
Introduction to the project
---------------------------

The world of open source is big. Solaris releases do contain the software
companion disc which contains a number of precompiled packages with open source
software, but you will almost always need a piece of software that is missing
from the companion disc, or isn't up to date enough.

OpenCSW fills this gap by providing binary packages and the corresponding build
recipes. Installing our packages is easy: you can install a package with all
dependencies with a single command.

If you want to build your own packages, build recipes for our package are
available in the `source code repository`_.

The OpenCSW packages have been compiled to allow easy forward migration and
crossgrades/mixing between SPARC and x86_64 CPUs. That means the same version
of each package is available for Solaris 10 and 11, for both SPARC and Intel
architectures. There are some exceptions, where the software is not available
for one of the architectures, or has a version mismatch (e.g. acroread).

For more information, you can watch our `project overview video`_ (1h) and
take a look at the `slide deck`_.


Support for different Solaris versions
======================================

As of April 2014:

* Solaris 11 – can use OpenCSW packages thanks to the backward binary compatibility
* Solaris 10 – is the main focus
* Solaris 9 – best effort, occasional updates
* Solaris 8 – no package updates at all

Mailing lists
=============

We suggest subscribing to our low traffic `announce list`_.

.. _announce list:
   https://lists.opencsw.org/mailman/listinfo/announce

.. _source code repository:
   https://sourceforge.net/p/gar/code/HEAD/tree/

.. _project overview video:
   http://youtu.be/Qmv5tvHEf4Q

.. _slide deck:
   http://de.slideshare.net/dmichelsen/opencsw-what-is-the-project-about
