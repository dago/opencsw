#!/bin/bash

# Prints privileges grants for the shared database
# Using MySQL syntax

set -u
set -e

CONFIG_FILE="site_config.sh"

if [[ -r "${CONFIG_FILE}" ]]
then
  source "${CONFIG_FILE}"
else
  echo "Please create '$(pwd)/${CONFIG_FILE}'"
  echo "See $0 for details."
  exit 1
fi

# Example site_config.sh:
#
# DATABASE="..."
# DEFAULT_HOST="192.168.0.%"
# DBA_USER=dba_user
# RELMGR_USER=relmgr_user
# MAINTAINER_USER=maintainer_user

TABLES_ADMIN=(
  architecture
  catalog_release
  catalog_release_type
  csw_config
  data_source
  host
  os_release
)
TABLES_REL_MGR=(
  srv4_file_in_catalog
  csw_file
  maintainer
)
TABLES_REGULAR=(
  pkginst
  checkpkg_error_tag
  checkpkg_override
  srv4_depends_on
  srv4_file_stats
  srv4_file_stats_blob
)

function print_table_grant {
  local table=$1
  local dbname=$2
  local user=$3
  local host=$4
  local operations=${5:-}
  if [[ -z "${operations}" ]]
  then
    operations="SELECT, INSERT, UPDATE, DELETE"
  fi
  echo -n "GRANT ${operations}"
  echo " ON ${dbname}.${table} TO '${user}'@'${host}';"
}

function print_grants {
  local dbname="${DATABASE}"
  local admin_user="${DBA_USER}"
  local relmgr_user="${RELMGR_USER}"
  local maintainer_user="${MAINTAINER_USER}"
  local host="${DEFAULT_HOST}"
  echo "GRANT ALL PRIVILEGES ON ${dbname}.* TO '${admin_user}'@'localhost';"
  echo "GRANT SELECT ON ${dbname}.* TO '${relmgr_user}'@'${host}';"
  echo "GRANT SELECT ON ${dbname}.* TO '${maintainer_user}'@'${host}';"
  # Release manager's tables
  for tbl in "${TABLES_REL_MGR[@]}" \
             "${TABLES_REGULAR[@]}"
  do
    print_table_grant "${tbl}" "${dbname}" "${relmgr_user}" "${host}"
  done
  # Package maintainer's tables
  for tbl in "${TABLES_REGULAR[@]}"
  do
    print_table_grant "${tbl}" "${dbname}" "${maintainer_user}" "${host}"
  done
  print_table_grant maintainer "${dbname}" "${maintainer_user}" "${host}" "SELECT, INSERT"
  echo "CREATE USER '${admin_user}'@'localhost' IDENTIFIED BY '<fill-me-in>';"
  echo "CREATE USER '${admin_user}'@'${host}' IDENTIFIED BY '<fill-me-in>';"
  echo "CREATE USER '${relmgr_user}'@'${host}' IDENTIFIED BY '<fill-me-in>';"
  echo "CREATE USER '${maintainer_user}'@'${host}' IDENTIFIED BY '<fill-me-in>';"
  echo "-- or"
  echo "SET PASSWORD FOR '${admin_user}'@'localhost' = PASSWORD('<fill-me-in>');"
  echo "SET PASSWORD FOR '${admin_user}'@'${host}' = PASSWORD('<fill-me-in>');"
  echo "SET PASSWORD FOR '${relmgr_user}'@'${host}' = PASSWORD('<fill-me-in>');"
  echo "SET PASSWORD FOR '${maintainer_user}'@'${host}' = PASSWORD('<fill-me-in>');"
  echo
  echo "FLUSH PRIVILEGES;"
}

function main {
  print_grants
}

main "$@"
