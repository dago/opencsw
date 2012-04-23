---------------
Getting started
---------------

OpenCSW uses a tool named pkgutil_ on top of the Solaris packaging utilities to
automatically download, install and update packages. It needs to be installed
manually once, after that all maintenance is done via pkgutil.

.. _pkgutil: http://pkgutil.net

On a Solaris 10 system, you can use the capacity of pkgadd to download
and install it via http in one step::

  pkgadd -d http://get.opencsw.org/now

You may need to specify a proxy with ``-x <proxy>:<port>``, be aware that there are
known issues with Squid and possibly other proxies.

On Solaris 8 and 9 (or 10 if you have issues with the above ``pkgadd``) you
need to download the package manually (e.g. using wget) and then install it::

  wget http://mirror.opencsw.org/opencsw/pkgutil.pkg
  pkgadd -d pkgutil.pkg all

You can now start installing packages. For a list of available packages use::

  /opt/csw/bin/pkgutil -l

For easy access to OpenCSW programs, put ``/opt/csw/bin`` in front of
``PATH``, and ``/opt/csw/share/man`` in front of ``MANPATH``. On Solaris 10,
you can do that by editing the ``/etc/default/login`` file, and logging out
and back in.

As the list is quite long and you probably have an idea what you are looking for the
list can be fuzzy-matched with::

  root# pkgutil -a vim
  common               package              catalog                        size
  gvim                 CSWgvim              7.3.055,REV=2010.11.25       1.1 MB
  vim                  CSWvim               7.3.055,REV=2010.11.25    1002.2 KB
  vimrt                CSWvimrt             7.3.055,REV=2010.11.25       7.3 MB

Lets just go ahead and try one::

  root# pkgutil -y -i vim
  ...
  root# vim

Voila! You have installed your first package!


------------------
Selecting a mirror
------------------

Now that you are about to install lots of stuff it may be a good time to select
one of the mirrors from ``mirror.opencsw.org`` close to you. The official
mirrors are listed at::

  http://www.opencsw.org/get-it/mirrors/

Please uncomment the line with ``mirror`` so it looks similar to this with the
URL replaced by the mirror you picked::

  mirror=http://mirror.opencsw.org/opencsw/unstable

By default, pkgutil is configured to use the ``testing`` catalog. You might
change it to ``unstable`` if you want to use newer versions of packages.

You can verify the setting with ``pkgutil -V``::

  ...
  maxpkglist              10000 (default: 10000)
  mirror                  http://mirror.opencsw.org/opencsw/unstable
                          (default: http://mirror.opencsw.org/opencsw/unstable)
  noncsw                  false (default: false)
  ...

On the next catalog update with ``pkgutil -U`` the catalogs are pulled from the new mirror.


-------------------------------------
Setting up cryptographic verification
-------------------------------------

The catalog is signed with PGP and it is a good idea to set up your system to
verify the integrity of the catalog. As the catalog itself contains hashes for
all packages in the catalog this ensures you actually install the packages
which were officially released. First you need to install ``gnupg`` (of course
with pkgutil!)::

  pkgutil -y -i gnupg

Then you need to import the public key::

  root# wget -O - http://www.opencsw.org/security/  | gpg --import -

The current fingerprint looks like this::

  root# gpg --fingerprint board@opencsw.org
  pub   1024D/9306CC77 2011-08-31
        Key fingerprint = 4DCE 3C80 AAB2 CAB1 E60C  9A3C 05F4 2D66 9306 CC77
  uid                  OpenCSW catalog signing <board@opencsw.org>
  sub   2048g/971EDE93 2011-08-31

You may also trust the key once you verified the fingerprint::
  root# /opt/csw/bin/gpg --edit-key board@opencsw.org trust

Now everything is in place for enabling security in ``pkgutil``. Edit the ``/etc/opt/csw/pkgutil.conf``
and uncomment the two lines with ``use_gpg`` and ``use_md5`` so they look like this::

  use_gpg=true
  use_md5=true

You can verify that it worked with ``pkgutil -V``::

  root@login [login]:/etc/opt/csw > pkgutil -V
  ...
  show_current            true (default: true)
  stop_on_hook_soft_error not set (default: false)
  use_gpg                 true (default: false)
  use_md5                 true (default: false)
  wgetopts                not set (default: none)

On the next ``pkgutil -U`` you should see a catalog integrity verification wit ``gpg``::

  ...
  Checking integrity of /var/opt/csw/pkgutil/catalog.mirror_opencsw_current_sparc_5.10 with gpg.
  gpg: Signature made Sat Jan 21 18:34:45 2012 CET using DSA key ID 9306CC77
  gpg: Good signature from "OpenCSW catalog signing <board@opencsw.org>"
  gpg: WARNING: This key is not certified with a trusted signature!
  gpg:          There is no indication that the signature belongs to the owner.
  Primary key fingerprint: 4DCE 3C80 AAB2 CAB1 E60C  9A3C 05F4 2D66 9306 CC77
  ==> 3173 packages loaded from /var/opt/csw/pkgutil/catalog.mirror_opencsw_current_sparc_5.10
  ...


--------------------
Package dependencies
--------------------

The OpenCSW packages have been compiled to allow easy forward migration and
crossgrades/mixing between Sparc and x64 CPUs. That means the same version of the
package is available for Solaris 10 and 11 for both Sparc and i386. There are
some exceptions where the software is absolutely not available or has a version
mismatch (e.g. acroread). To allow this there are usually no dependencies to
SUNW packages. This sometimes leads to large dependency chains (and people
thinking of OpenCSW packages as "bloated") but that is the price to pay for
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
Internet access, you can use pkgutil to prepare a .pkg file with the whole
dependency chain. This wasy is much easier than copying dependencies one by
one::

  pkgutil \
    --stream \
    --target=sparc:5.10 \
    --output imagemagick-and-others.pkg \
    --yes \
    --download \
    imagemagick coreutils vim ggrep gsed

At the end of the run, pkgutil displays the correct order to install the
packages in.

The resulting package stream will be placed in the ``~/.pkgutil/packages``
directory.

This topic is also `discussed`_ on the community site.

.. _discussed:
   http://www.opencsw.org/community/
   questions/92/
   installing-without-a-direct-internet-access
