---------------
Catalog staging
---------------

For releases and staging overview, see the releases and staging wiki
page[#releases-and-staging-wiki]_, written in 2009. You can also see the README
file on the `OpenCSW master mirror`_.

* unstable is a working catalog where package maintainers can make changes at
  will. It is regenerated every few hours.
* testing is a symlink to a named release. It gets periodically updated from the
  unstable catalog. As of March 2014, it is done infrequently, by a human.
* stable is a symlink to a named release. Once a stable release is made, it is
  not updated unless there are important security updates to be pushed.

Footnotes
---------
.. [#releases-and-staging-wiki]
   `Releases and staging wiki page`_
.. _Releases and staging wiki page:
   http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/
   lib/python/sharedlib_utils_test.py#L13
.. _OpenCSW master mirror:
   http://mirror.opencsw.org/opencsw/
