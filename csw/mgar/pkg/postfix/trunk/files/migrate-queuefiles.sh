#!/bin/bash
#
# migrate-queuefiles.sh:
#  helper script to move possible queue files from the CSWpostfix 2.4.x
#  spool location to the CSWpostfix >= 2.6.x spool location.
#
# $Id$

SPOOL_OLD=/opt/csw/var/spool/postfix
SPOOL_NEW=/var/opt/csw/spool/postfix
QDIRS="incoming active deferred corrupt hold bounce defer trace"

if [ "$1" != "-y" ]; then
  echo "This helper script will move leftover postfix email queue files from "
  echo 
  echo "  $SPOOL_OLD   to   $SPOOL_NEW"
  echo
  echo "Please make sure to understand what it does, backup your queue files"
  echo "in advance, and re-run this script with -y to start the process."
  exit 1
fi

[ -x /usr/bin/zonename ] && ZONEOPT="-z `/usr/bin/zonename`"
if pgrep $ZONEOPT -lf /opt/csw/libexec/postfix/master; then
   echo "Make sure postfix is not running! Exiting."
   exit 1
fi

for qdir in $QDIRS; do
    [ -d ${SPOOL_OLD}/$qdir ] || continue
	echo "Moving files from ${SPOOL_OLD}/$qdir to ${SPOOL_NEW}/$qdir"
	cd ${SPOOLDIR_NEW}/$qdir && \
		find ${SPOOLDIR_OLD}/$qdir -type f -exec mv '{}' . +
done

echo "No errors so far? Then please run postsuper now."
