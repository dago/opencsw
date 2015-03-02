.. _no-internet-access:
.. _installing-on-a-host-without-an-internet-connection:

----------------------------------
Installing without Internet access
----------------------------------

One way is to :ref:`create a mirror of the OpenCSW catalog
<setting-up-local-mirror>`, transfer it to the internal network, and serve it
over HTTP (e.g. with Apache or lighttpd). You can then configure pkgutil on
the restricted machines to use your internal package mirror.

The second option is to build a single package stream file containing the
package(s) you want to install, with all the dependencies. You do need one
machine with Internet access, and a way to transfer files from it to the
machines with restricted access.

Let's assume you have a working Solaris host that has Internet access - this
is not your target machine, it's an intermediate host. You bootstrap OpenCSW
on it::

  pkgadd -d http://get.opencsw.org/now
  PATH=/opt/csw/bin:$PATH
  export PATH
  pkgutil -U -u pkgutil

Now that you have a functional pkgutil, you can use it to build your package
stream with dependencies. You can then use the following command (split into
multiple lines for readability), as a regular user::

  pkgutil \
    --stream \
    --target=sparc:5.10 \
    --output imagemagick-and-others.pkg \
    --yes \
    --download \
    imagemagick coreutils vim ggrep gsed

You'll see how pkgutil downloads many different packages and repacks them into
a single package stream. You can then transfer it to your target machines and
install packages from it. You need to install the packages in the right order;
pkgutil will print that order out when it finishes creating the package
stream.

The resulting package stream will be placed in the ``~/.pkgutil/packages``
directory.

This topic is also `discussed on the community site`_.

.. _discussed on the community site: http://www.opencsw.org/community/questions/92/installing-without-a-direct-internet-access
