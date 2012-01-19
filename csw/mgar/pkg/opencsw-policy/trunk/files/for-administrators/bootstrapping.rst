-------------
Bootstrapping
-------------

On a Solaris 10 system, you can use the capacity of pkgadd to download
packages via http::

  pkgadd -d http://get.opencsw.org/now

On Solaris 8 and 9 (best effort support only), you need to download the
package using e.g. wget and install it with::

  wget http://mirror.opencsw.org/opencsw/pkgutil.pkg
  pkgadd -d pkgutil.pkg

