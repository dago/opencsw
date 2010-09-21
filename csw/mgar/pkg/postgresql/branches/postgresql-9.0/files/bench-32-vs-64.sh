#!/opt/csw/bin/bash
# vim:set sw=2 ts=2 sts=2:
#
# $Id$
#
# Usage: run as user postgres
# $ ./bench-32-vs-64.sh sparcv8
# $ ./bench-32-vs-64.sh sparcv9

set -u
set -e

do_arch() {
	local arch="$1"
	local bindir=/opt/csw/bin/postgresql/8.4/${arch}
	local pgdatadir=/var/opt/csw/postgresql/8.4/pgdata-${arch}
	echo "architecture: ${arch}"
	echo "bindir: ${bindir}"
	echo "pgdatadir: ${pgdatadir}"
	read -p "Press ENTER to continue. > " JUNK
	echo "Stopping the database."
	${bindir}/pg_ctl -D ${pgdatadir} -l ${pgdatadir}/postgresql.log stop || true
	echo "Removing ${pgdatadir}"
	rm -rf "${pgdatadir}"
	mkdir -p "${pgdatadir}"
	echo "Initializing ${pgdatadir}"
	${bindir}/initdb -D ${pgdatadir} -E "utf-8" -U postgres
	echo "Starting the database"
	${bindir}/pg_ctl -D ${pgdatadir} -l ${pgdatadir}/postgresql.log start
	echo "Waiting for the database to start up."
	sleep 3
	echo "Creating the pgbench database"
	${bindir}/createdb -E utf-8 pgbench
	echo "Initializing pgbench"
	pgbench -i -s 10 pgbench

	echo "Running benchmarks"
	# http://www.robsell.com/howto/pgbench.html
	# local HOST=localhost
	local USER=postgres
	local DB=pgbench
	local totxacts=1000
	for c in 10
	do
		t=`expr $totxacts / $c`
		# psql -h $HOST -U $USER -c 'vacuum analyze' $DB
		# psql -h $HOST -U $USER -c 'checkpoint' $DB
		psql -U $USER -c 'vacuum analyze' $DB
		psql -U $USER -c 'checkpoint' $DB
		echo "===== sync ======" 1>&2
		sync;sync;sync;sleep 10
		echo $c concurrent users... 1>&2
		pgbench -n -U $USER -t $t -c $c $DB
	done
	${bindir}/pg_ctl -D ${pgdatadir} -l ${pgdatadir}/postgresql.log stop || true
}

all_architectures() {
	for arch in sparcv8 sparcv9
	do
		do_arch ${arch}
	done
}

main() {
	arg1="${1:-}"
	if [[ -n "$arg1" ]]; then
		do_arch $arg1
	else
		all_architectures
	fi
}

main "$@"
