[[toc]]

+ Usage

The csw-upload-pkg utility is used to upload packages to OpenCSW catalogs. By default, it uploads your packages to the unstable catalog. The utility must be run on the login host.

[[code]]
maciej@login [login]:~ > csw-upload-pkg 
Usage: csw-upload-pkg [ options ] <file1.pkg.gz> [ <file2.pkg.gz> [ ... ] ]

Uploads a set of packages to the unstable catalog in opencsw-future.

- When an architecture-independent package is uploaded, it gets added to both
  sparc and i386 catalogs

- When a SunOS5.x package is sent, it's added to catalogs SunOS5.x,
  SunOS5.(x+1), up to SunOS5.11, but only if there are no packages specific to
  5.10 (and/or 5.11).

- If a package update is sent, the tool uses both the catalogname and the
  pkgname to identify the package it's updating. For example, you might upload
  foo_stub/CSWfoo and mean to replace foo/CSWfoo with it.

The --os-release flag makes csw-upload-pkg only insert the package to catalog with the
given OS release.

The --catalog-release flag allows to insert a package into a specific catalog,
instead of the default 'unstable'.

= General considerations =

This tool operates on a database of packages and a package file store. It
modifies a number of package catalogs, e.g.:

  {{dublin,unstable,kiel,bratislava}}x{{sparc,i386}}x{{5.8,5.9.5.10,5.11}}

For more information, see:
http://wiki.opencsw.org/automated-release-process#toc0
[[/code]]

Once your packages are sent, you can verify the state of the checkpkg database by visiting the web frontend of the checkpkg database[[footnote]][http://buildfarm.opencsw.org/pkgdb/catalogs/ Catalog list in the checkpkg database frontend][[/footnote]] and inspecting the catalogs you expect your package to be.

The opencsw-future tree[[footnote]][http://mirror.opencsw.org/opencsw-future/ opencsw-future catalog tree][[/footnote]] on the mirror host is updated a couple times per day.  Your uploaded packages will appear there eventually.

In case of any problems with the tool, please re-run the tool in debug mode (--debug) and send full output to Maciej.

+ Infrastructure

* **Buildfarm** - a collection of Solaris zones and hardware hosting them
* **Buildfarm database** is a MySQL database on the buildfarm, on the mysql zone (mysql.bo.opencsw.org)
* **Web interface for the buildfarm database** http://buildfarm.opencsw.org/pkgdb/
* **External REST interface** at http://buildfarm.opencsw.org/pkgdb/rest/
* **Internal REST interface** at http://buildfarm.opencsw.org/releases/
* **Master mirror** at http://mirror.opencsw.org
* **unstable catalog** at http://mirror.opencsw.org/opencsw-future/unstable/
* **[http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/lib/python Source code]** of those applications is available from SourceForge.

++ Uploading a package

Here's a rough description of what happens when you upload a package using csw-upload-pkg.

# csw-upload-pkg examines the given file name set for correctness
 * It alerts in certain conditions, e.g. a present i386 file but missing sparc file, or an UNCOMMITTED tag
# csw-upload-pkg runs 'pkgdb importpkg' to make sure that your package's metadata are imported to the buildfarm database
# csw-upload-pkg queries the external rest interface for package metadata; it verifies that metadata have been uploaded successfully
# csw-upload-pkg queries the internal rest interface to know whether package data (as opposed to metadata) are uploaded to the master mirror
 * if not yet there, csw-upload-pkg sends a POST request with package data
# csw-upload-pkg queries the external rest interface for contents of catalogs
# csw-upload-pkg calculates which packages to insert to which catalogs
 * Depending on the given file set and catalog contents, 5.9 packages may or may not be inserted into 5.10 and 5.11 catalogs
# csw-upload-pkg sends a sequence of DELETE and PUT queries to the internal rest interface to modify catalogs

++ Catalog generation

web zone runs a cron job which wakes up every 3h and performs a set of tasks.  It generates a new unstable catalog from the database, and pushes it to the master mirror.

* pkgdb is invoked, and it generates a catalog at the given location
 * pkgdb uses a direct MySQL connection
* catalog notifier is run, and sends e-mails to the maintainers of modified packages
* A cron job on unstable9x generates atom feeds for each catalog every hour.   For the time being, they can be found in  [http://buildfarm.opencsw.org/~bwalton Ben's directory].

++ Promoting / copying packages between releases

//([http://lists.opencsw.org/pipermail/maintainers/2013-July/018220.html mailing list discussion])//

The integrate_catalogs.py script is used. For example:

[[code]]
lib/python/integrate_catalogs.py \
  --from-catalog=unstable \
  --to-catalog=kiel \
  -o to_kiel_17.sh

vim to_kiel_17.sh

# Looks good?
bash to_kiel_17.sh
[[/code]]

The number 17 is just there for tracking; I'm keeping the previous generated integration scripts to keep track of what I've done in the past.

The task requires manual/mental tracking of the state of unstable, e.g. you need to know if unstable is in a good enough shape to be integrated/copied to testing.

The integrate_catalogs.py script itself does not perform any operations. It queries the database and generates a shell script. You then review the shell script, make modifications as needed, and execute it. The operations in the shell script are low level: removing and creating associations between catalogs and svr4 package files, identified by md5 sums. For example it's "add <md5> to 5.9/unstable/i386". In practice, you mostly edit the shell script to delete some lines in order to prevent some packages from being promoted, e.g. if you know that certain package is currently buggy in unstable.

The script defines the basic operations, using curl and the REST interface:

[[code]]
function _add_to_cat {
  ${CURL} -X PUT ${REST_URL}catalogs/$1/$2/$3/$4/ ; echo
}

function _del_from_cat {
  ${CURL} -X DELETE ${REST_URL}catalogs/$1/$2/$3/$4/ ; echo
}
[[/code]]

Then it defines a function to push a specific package:

[[code]]
function upgrade_apache2 {
  # apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel sparc SunOS5.10 697eb40b67ffcb1da7bd36d4dcf28102
  _add_to_cat kiel sparc SunOS5.10 2ed8346d32734206398497e1ff1798e3
  # apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel sparc SunOS5.11 697eb40b67ffcb1da7bd36d4dcf28102
  _add_to_cat kiel sparc SunOS5.11 2ed8346d32734206398497e1ff1798e3
  # apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel i386 SunOS5.10 4faee5142d978e27bee8372275327ed6
  _add_to_cat kiel i386 SunOS5.10 145bd67387314ad5028178f6df27b96d
  # apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel i386 SunOS5.11 4faee5142d978e27bee8372275327ed6
  _add_to_cat kiel i386 SunOS5.11 145bd67387314ad5028178f6df27b96d
}
[[/code]]

Additionally, there are the undo functions in the shell script. After
executing the script you save it, and if anything needs to be rolled
back, there are functions in the shell script to reverse the
operation.

[[code]]
function undo_upgrade_apache2 {
  # UNDO of apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel sparc SunOS5.10 2ed8346d32734206398497e1ff1798e3
  _add_to_cat kiel sparc SunOS5.10 697eb40b67ffcb1da7bd36d4dcf28102
  # UNDO of apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel sparc SunOS5.11 2ed8346d32734206398497e1ff1798e3
  _add_to_cat kiel sparc SunOS5.11 697eb40b67ffcb1da7bd36d4dcf28102
  # UNDO of apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel i386 SunOS5.10 145bd67387314ad5028178f6df27b96d
  _add_to_cat kiel i386 SunOS5.10 4faee5142d978e27bee8372275327ed6
  # UNDO of apache2 upgrade from 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17
  _del_from_cat kiel i386 SunOS5.11 145bd67387314ad5028178f6df27b96d
  _add_to_cat kiel i386 SunOS5.11 4faee5142d978e27bee8372275327ed6
}
[[/code]]

In the final section of the script, the upgrade functions are called:

[[code]]
upgrade_apache2 # version 2.2.22,REV=2012.06.01 to 2.2.24,REV=2013.06.17 # bundles:httpd
[[/code]]

All these operations need to be performed on the login host.

++ Connections

This image is generated from a [http://sourceforge.net/apps/trac/gar/browser/csw/mgar/gar/v2/doc/connections.dot graphviz file] available from gar source code repository.  It describes connections made by various infrastructure components.

[[=image connections.png size="medium"]]

+ Discussion

Pains with the current process:
* --Released packages are sometimes still in testing/ (fixed by Dago)--
* --The whole process includes too many manual steps, which could be automated--
* --Mixed usage of testing/ for developer testing and user testing--

Comparison of new catalog layout with Debian:

||~ Debian ||~ OpenCSW ||~ Who puts stuff there ||~ an example command ||
|| Experimental || {{experimental/}} || by the maintainer || {{cp <pkg> /home/experimental/<name>}} ||
|| Unstable || {{unstable/}} || by the maintainer || {{csw-upload-pkg}} ||
|| Testing / Named release || {{testing/}} | {{kiel/}} || by an automated job || //not implemented// ||
|| Stable / Named release || {{stable/}} | {{dublin/}} || by release manager || {{rm stable; ln -s dublin stable}} ||

For each catalog there is a set of machines equipped with the packages from the catalog. The catalog is always an overlay over the more stable version. That means the catalog for testing contains all packages from current, where the packages from testing supersede the ones from current.

||~ {{experimental/}} ||~ {{unstable/}} ||~ {{testing/}} ||~ {{stable/}} ||
|| e8s / e8x || u8s / u8x || t8s / t8x || s8s / s8x ||
|| e9s / e9x || u9s / u9x || t9s / t9x || s9s / s9x ||
|| e10s / e10x || u10s / u10x || t10s / t10x || s10s / s10x ||
|| eosols / eosolx || uosols / uosolx || tosols / tosolx || sosols / sosolx ||

Experimental has the notion of "projects", which allows a grouping of packages for release (like for XML Toolchain, X11, Gnome, etc.)
Package releases are directly made out of GAR:
[[code]]
gmake submitpkg[-<project>]
[[/code]]
This checks if everything has been committed (like now when CSW is put in instead of UNCOMMITTED) and makes a server-side copy  in SVN to tags as tags/[<project>_]<pkg>-<version>,REV=... (implemented in gar/v2-pbuild).

TBD: This triggers the automated buildbot which puts the packages automatically in experimental after building.

The same procedure is triggered by the upstream watch:
# Check out <pkg>
# Copy trunk to {{tags/<pkg>-<version>_REV=...}} with the new version
# Update Revision
# gmake makesum
# gmake garchive
# Commit changes
# (Trigger automatic buildbot build)
# Mail maintainer after build has finished

In Oslo we talked about additional commands like csw-build and csw-release initiated by Trygve, maybe he can write something about the usage?

++ See also

* [[[Releases and staging]]]
* [[[Release process]]]
