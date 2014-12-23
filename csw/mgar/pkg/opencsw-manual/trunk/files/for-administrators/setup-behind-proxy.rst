.. _setup-behind-proxy:

Behind a proxy
==============

You may need to specify a proxy with ``-x <proxy>:<port>``, be aware that there
are known issues with Squid and possibly other proxies::

  pkgadd -x myproxy:3128 -d http://get.opencsw.org/now

Proxy with a password
=====================

You will need to configure ``/etc/opt/csw/wgetrc``::

  proxy_user=<user>
  proxy_password=<password>

Continue to :ref:`Full setup <installation-full-setup>`.
