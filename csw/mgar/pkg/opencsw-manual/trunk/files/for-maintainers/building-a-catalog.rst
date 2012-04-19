--------------------------
Building a package catalog
--------------------------

If you have built a package (or a set of them), you might want to test them.
You could just gunzip the packages and run pkgadd, but if you wanted to test
your package on a couple of systems, it's better to build a catalog.

Make sure you've installed the ``pkgutilplus`` package. It contains the
``bldcat`` utility. You can use it to create a local catalog with your
package::

  catalog_root=${HOME}/opencsw-catalog
  catalog_path=${catalog_root}/$(uname -p)/$(uname -r)
  cp /path/to/your_package.pkg ${catalog_path}
  bldcat ${catalog_path}

Once this is done, you can instruct pkgutil to install packages from it. You
can either serve the root catalog directory over HTTP, or you can refer to
a local filesystem path::

  sudo pkgutil -t file://${catalog_path} -y -i your_package

If you create a persistent local catalog, you can add the path or URL to
``/opt/csw/etc/pkgutil.conf``.
