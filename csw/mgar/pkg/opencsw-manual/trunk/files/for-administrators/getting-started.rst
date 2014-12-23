.. _getting-started:

---------------
Getting started
---------------

Solaris 10 and Solaris 11:

::

  pkgadd -d http://get.opencsw.org/now
  /opt/csw/bin/pkgutil -U
  /opt/csw/bin/pkgutil -a vim
  /opt/csw/bin/pkgutil -y -i vim
  /opt/csw/bin/vim

Done!

Additional, exceptional and/or optional steps:

- :ref:`selecting a local mirror <selecting-mirror>`
- :ref:`setting up cryptographic verification <setting-up-cryptograhic-verification>`
- :ref:`selecting the catalog release <selecting-catalog-release>`
- :ref:`older Solaris versions <old-solaris>`
- :ref:`behind a HTTP proxy <setup-behind-proxy>`

Continue to :ref:`Full setup <installation-full-setup>`.
