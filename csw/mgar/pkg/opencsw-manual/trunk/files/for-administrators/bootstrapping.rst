-------------
Bootstrapping
-------------

OpenCSW uses a tool named pkgutil on top of the Solaris packaging utilities
to automatically download, install and update packages. This has to be installed
manually once, after that all maintenance is done via pkgutil.

On a Solaris 10 system, you can use the capacity of pkgadd to download
and install it via http in one step::

  pkgadd -d http://get.opencsw.org/now

On Solaris 8 and 9 you need to download the package manually e.g. using wget
and then install it::

  wget http://mirror.opencsw.org/opencsw/pkgutil.pkg
  pkgadd -d pkgutil.pkg

Now is a good time to modify your profile to honour the OpenCSW programs.
For a bourne shell add the following lines to your ``.profile``::

  PATH=$PATH:/opt/csw/bin
  MANPATH=$MANPATH:/opt/csw/share/man

Please source it or logout and login again to make sure the environment is adjusted.

You can now start installing packages. For a list of available packages use
::
  pkgutil -l

As the list is quite long and you probably have an idea what you are looking for the
list can be fuzzy-matched with
::
  root# pkgutil -a vim
  common               package              catalog                        size
  gvim                 CSWgvim              7.3.055,REV=2010.11.25       1.1 MB
  vim                  CSWvim               7.3.055,REV=2010.11.25    1002.2 KB
  vimrt                CSWvimrt             7.3.055,REV=2010.11.25       7.3 MB

Lets just go ahead and try one::

  root# pkgutil -i vim
  ...
  root# vim

Voila! You have installed your first package!


------------------
Selecting a mirror
------------------

Now that you are about to install lots of stuff it may be a good time to select
one of the mirrors from ``mirror.opencsw.org`` close to you. The official mirrors
are listed at
  http://www.opencsw.org/get-it/mirrors/


-------------------------------------
Setting up cryptographic verification
-------------------------------------

