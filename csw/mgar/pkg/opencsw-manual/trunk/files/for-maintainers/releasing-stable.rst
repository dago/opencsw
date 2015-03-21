Releasing stable
================

Gotchas
-------

1. "stable" does not exist in the database as a separate catalog, but
   "unstable" does exist. "stable" and "testing" are symlinks which point at
   named releases.
2. There are two super confusing directories on the buildfarm:

   * ``/home/mirror/opencsw-official`` we make changes here
   * ``/home/mirror/opencsw/official`` copy of the official mirror, we do not
     make any manual changes to it

Prerequisites
-------------

* Access to ``web@web``
* Access to ``root@mysql``
* Access to ``catalogsign@cswsign``
* Access to the gar and opencsw subversion repositories (these are 2 separate repositories)
* Catalog signing password (the gpg private key password)
* Access to wordpress on www.opencsw.org
* Access to the twitter account

The procedure
-------------

In this example:

* old stable: **kiel**
* new stable: **bratislava**
* new testing: **munich** (does not exist when you start working)

Creating a new named catalog and populating it:

RECOMMENDED: as ``web@web``, run ``crontab -e`` and disable
``opencsw-future-update`` because it will get in your way later on.

ACTION NEEDED: Make a backup of the `checkpkg` database::

  ssh root@mysql
  # We'll be messing with the database. Let's back it up.
  mysqldump --max_allowed_packet=128M -u root checkpkg | pv \
    | gzip > checkpkg-$(date +%Y-%m-%d).sql.gz
  mysql -u root checkpkg

ACTION NEEDED: Create the new catalog in the database.

In the SQL prompt, we're creating a row which represents the new catalog::

  INSERT INTO catalog_release (name) VALUES('munich');

The new catalog exists in the database, but is empty. We need to make
a snapshot of unstable and populate the new catalog from it. We will also need
to create a directory on disk for the new catalog. The scripts generating
catalogs don't create catalog subdirectories automatically.

We wrap the copying in a transaction in case we mess something up, so we can
roll back instead of having to restore a backup::

  START TRANSACTION;
  INSERT INTO srv4_file_in_catalog (arch_id, osrel_id, catrel_id, srv4file_id,
                                    created_on, created_by)
  SELECT
    arch_id, osrel_id,
    (SELECT id FROM catalog_release WHERE name = 'munich'),
    srv4file_id, created_on, created_by
  FROM
    srv4_file_in_catalog
  WHERE
    catrel_id = (SELECT id FROM catalog_release WHERE name = 'bratislava');
  COMMIT;

The database part is done. Next up is the code. We have a number of places in
the code where catalogs are listed by name. You can grep for the new stable
name, e.g. "bratislava". Ideally this code would be refactored and store this
in one place only. Feel free to do it!

Note: The Go code will turn up in the grep results, but it doesn't need
modifications: catalog names can be passed as command line flags.

ACTION NEEDED: Add "bratislava" to catalog lists in the code. See the example patch: http://sourceforge.net/p/gar/code/24148/

ACTION NEEDED: Replace "kiel" with "bratislava" in all scripts in
``~web/bin``. At the time of writing the following scripts were updated:

* generate-unstable
* find-obsolete-pkgs
* promote_to_testing.sh
* dist-hardlinkify

There could be other, new scripts that need updating. Examine the crontab of
the "web" user and see if there are any other files that need updating. Or
just grep for "kiel" (the old stable) in ``~web/bin`` on the web host.

ACTION NEEDED: Submit your modifications. Run ``svn commit ...`` to make sure
y our modifications are pushed back to the repository.

Making a directory for the new catalog::

  mkdir -p /home/mirror/opencsw-official/munich/{i386,sparc}/5.{8,9,10,11}

Note: The catalog generation program could be modified to create these
directories, but it doesn't do that as of September 2014.

ACTION NEEDED: Add "munich" to the list of catalogs eligible for signing::

  ssh catalogsign@cswsign
  vim /opt/catalog_signatures/bin/http_gpg_daemon

Force the daemon to pick up the changes. This will require the signing
password::

  /opt/catalog_signatures/bin/reset_passphrase

Keep pressing CTRL+c until screen terminates::

  /opt/catalog_signatures//tmp/signing_daemon.pid
  /opt/catalog_signatures/bin/signing_daemon

Press CTRL+A, then D to exit screen.

Submit the changes. Note: I don't know how to do that. You need permissions to
a separate git repository hosted on SourceForce. I don't have access to it.
Ben does.

ACTION NEEDED: Modify symlinks in the source directory, as ``web@web``::

  cd /home/mirror/opencsw-official
  # You should see "stable -> kiel".
  ls -l stable testing

  rm testing
  ln -s munich testing
  rm stable
  ln -s bratislava stable

  # Just to confirm. You should see "stable -> bratislava".
  ls -l stable testing

ACTION NEEDED: Edit the top-level README file::

  vim /home/mirror/opencsw-official/README

ACTION NEEDED: Create new symlinks in the ``releases/`` subdirectory::

  cd /home/mirror/opencsw-official
  tree releases/
  ln -s ../../bratislava releases/stable/$(date +%Y-%m)-bratislava
  ln -s ../../munich releases/testing/$(date +%Y-%m)-munich
  # Look if the symlinks look correct.
  tree releases/

Manually run the catalog generation (as web@web)::

  /home/web/bin/opencsw-future-update

If prompt returns immediately, it means one copy of the script is already
running - it's started automatically every 10 minutes. Wait a minute for it to
finish and run the command again. The runs that run every 10 minutes only
generate the unstable catalog. In this case we need a full run, which is done
by running ``opencsw-future-update`` without arguments.

When the run is finished, visit
http://buildfarm.opencsw.org/catalog-generation.log and see if it succeded. Go
to https://mirror.opencsw.org/opencsw/munich/i386/5.10/catalog and see if the
catalog file is signed. If not, read the log file and fix any problems you
encounter. Ask buildfarm@ or maintainers@ for help if necessary.

Note: To see if there are any errors, you need to look for a line like this::

  ++ rm -f /var/tmp/catalog-generation.lock/pid

near the end of the line, and look at lines immediately above this line. This
is where potential error messages might be. For example, signing could fail.
If it runs fine, you will see::

./opencsw-future-update completed successfully

near the end of the file.

When everything works, continue.

ACTION NEEDED: If you disabled ``opencsw-future-update`` earlier, enable it again.

ACTION NEEDED: Communicate. Send out information about the new stable to
users@, with BCC to announce@, example:
http://lists.opencsw.org/pipermail/users/2014-March/009745.html.  Make sure to
send a plaintext email. Then reply to this email, but enter maintainers@ as
the ``To:`` address. Publish a post on the website (wordpress) and send a tweet
with a link to that post.

You're done!

If this document is missing anything, please update it.
