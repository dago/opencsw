============================
Installing packages en masse
============================

---------------------------------------------------
Installing on a host without an Internet connection
---------------------------------------------------

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

This topic is also `discussed on the community site`_.

.. _discussed on the community site: http://www.opencsw.org/community/questions/92/installing-without-a-direct-internet-access

-----------------
Large deployments
-----------------

To manage package across multiple hosts, you can use a configuration management
system like puppet, see `Andy Botting's blog post`_ for an example.

.. _Andy Botting's blog post:
   http://www.andybotting.com/using-pkgutil-on-solaris-with-puppet-for-easy-package-management 
