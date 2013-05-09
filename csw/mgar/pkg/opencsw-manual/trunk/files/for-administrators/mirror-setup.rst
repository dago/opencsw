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
mirrors provide access via the ``rsync`` protocol, please consult
`our list of mirrors`_.

To make a full copy of the OpenCSW repository, first make sure you have rsync
on your system::

  sudo pkgutil -y -i rsync

Then copy the files::

  sudo mkdir -p /export/mirror/opencsw
  sudo chown $LOGNAME /export/mirror/opencsw
  rsync -aH --delete rsync://rsync.opencsw.org/opencsw/ /export/mirror/opencsw

The directory ``opencsw-mirror`` can either be shared via HTTP or via NFS to the
``pkgutil`` clients.  Use ``http://myserver/opencsw-mirror/`` for HTTP and
``file:///myserver/opencsw-mirror`` for NFS as mirror option in ``pkgutil``.

.. _our list of mirrors:
  http://www.opencsw.org/get-it/mirrors/
