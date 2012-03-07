-------------
Bootstrapping
-------------

OpenCSW uses a tool named pkgutil on top of the Solaris packaging utilities to
automatically download, install and update packages. It needs to be installed
manually once, after that all maintenance is done via pkgutil.

On a Solaris 10 system, you can use the capacity of pkgadd to download
and install it via http in one step::

  pkgadd -d http://get.opencsw.org/now

On Solaris 8 and 9 you need to download the package manually, e.g. using wget
and then install it::

  wget http://mirror.opencsw.org/opencsw/pkgutil.pkg
  pkgadd -d pkgutil.pkg all

For easy access to OpenCSW programs, put ``/opt/csw/bin`` in front of PATH,
and ``/opt/csw/share/man`` in front of MANPATH.

You can now start installing packages. For a list of available packages use::

  pkgutil -l

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
one of the mirrors from ``mirror.opencsw.org`` close to you. The official mirrors
are listed at::

  http://www.opencsw.org/get-it/mirrors/

It is important to note that ``pkgutil`` can use **two** configuration files:

- ``/etc/opt/csw/pkgutil.conf``
- ``/opt/csw/etc/pkgutil.conf``

This may seem confusing, the reason why there are two is that it is possible to run
OpenCSW in a `sparse root environment`_ where ``/opt`` is not writable. In this scenario
you use configurations in ``/opt/csw/etc`` for global settings and ``/etc/opt/csw``
for zone-specific setting. Both ``pkgutil.conf`` are identical on installation with all
configuration options commented out, so you can just pick one for now. As a rule of thumb it is
recommended to prefer the more prominent ``/etc/opt/csw``. Please uncomment the line
with ``mirror`` so it looks similar to this with the URL replaced by the mirror you picked::

  mirror=http://mirror.opencsw.org/opencsw/unstable

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

The catalog is signed with PGP and it is a good idea to set up your system to verify
the integrity of the catalog. As the catalog itself contains hashes for all packages
in the catalog this ensures you actually install the packages which were officially
released. First you need to install ``pgp`` (of course with pkgutil!)::

  pkgutil -y -i gpg

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

Package dependencies are modeled in the OpenCSW `catalogs`_ to allow automatic
dependency resolution via pkgutil. To view the current dependencies for a
package you can use::

  pkgutil --deptree <pkg>


---------------------------
Setting up a private mirror
---------------------------

Sometimes it is sufficient to just go on with a mirror on the internet. However, there are situations
where a local mirror can be useful. When you have a lot of servers accessing the repository, want to control
the package updates exactly or when your production servers just can't access the internet at all
a local mirror is necessary.

To set up the mirror you should use rsync as it can update your local copy quickly and with low
bandwidth use and also preserves hardlinks. Not all mirrors provide access via the rsync protocol,
a list can be found at http://www.opencsw.org/get-it/mirrors/ .
To make a full copy of the OpenCSW repository use this::

  pkgutil -y -i rsync
  rsync -aH --delete rsync://rsync.opencsw.org/opencsw /my/server/repo

The directory ``repo`` can either be shared via HTTP or via NFS to the pkgutil clients.
Use http://myserver/url-to-repo/ for HTTP and file:///myserver/dir-to-repo for NFS as
mirror option in pkgutil.


Mirroring only a subset
=======================

You can also mirror only a subset of the repository, e.g. the 'unstable' catalog or even
just a few packages.

pkgutil --stream


Layout of the mirror
====================
