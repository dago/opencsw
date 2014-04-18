.. _catalog-releases:

---------------
Catalog staging
---------------

For releases and staging overview, see the releases and staging wiki page
Releases and Staging [#releases-and-staging-wiki]_, written in 2009. You can
also see the README file on the OpenCSW master mirror
[#opencsw-master-mirror]_.

* **:index:`unstable`** is a working catalog where package maintainers make changes at
  will. Updates to unstable are pushed every 10 minutes (April 2014).
* **testing** is a symlink to a named release. It gets periodically updated
  from the unstable catalog. As of March 2014, it is done infrequently, by a
  human.
* **:index:`stable`** is a symlink to a named release. Once a stable release is made, it
  is not updated unless there are important security updates to be pushed.

References
----------

.. [#releases-and-staging-wiki] `Releases and staging wiki page`_
.. _Releases and staging wiki page:
   http://wiki.opencsw.org/releases-and-staging
.. [#opencsw-master-mirror] `OpenCSW master mirror`_
.. _OpenCSW master mirror:
   http://mirror.opencsw.org/opencsw/
