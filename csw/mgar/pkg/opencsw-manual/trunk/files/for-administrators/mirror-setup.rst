---------------------------
Setting up a private mirror
---------------------------

Sometimes it is sufficient to simply use a mirror on the Internet.
However, there are situations where a local mirror can be useful. When you have
a lot of servers accessing the repository, want to control the package updates
exactly or when your production servers just can't access the internet at all,
a local mirror is necessary.

To set up the mirror you should use ``rsync`` as it can update your local copy
quickly and with low bandwidth use and also preserves hardlinks. Not all
mirrors provide access via the ``rsync`` protocol, a list can be found at
http://www.opencsw.org/get-it/mirrors/ .  To make a full copy of the OpenCSW
repository use this::

  pkgutil -y -i rsync
  rsync -aH --delete rsync://rsync.opencsw.org/opencsw /my/server/repo

The directory ``repo`` can either be shared via HTTP or via NFS to the
``pkgutil`` clients.  Use http://myserver/url-to-repo/ for HTTP and
file:///myserver/dir-to-repo for NFS as mirror option in ``pkgutil``.
