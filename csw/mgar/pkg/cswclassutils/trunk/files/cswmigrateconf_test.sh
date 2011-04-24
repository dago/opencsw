#!/opt/csw/bin/bash

set -x
set -u
set -e

readonly CAS_DIR="files"
readonly CAS_UNDER_TEST="CSWcswclassutils.i.cswmigrateconf"
# readonly WORK_DIR="$(gmktemp -d /tmp/castest.XXXXXXXXXX)"
readonly WORK_DIR="$(gmktemp -d castest.XXXXXXXXXX)"
readonly SRC_DIR="${WORK_DIR}/src"
PKG_INSTALL_ROOT="${WORK_DIR}/root"
readonly OLD_CONFDIR_ABS="${PKG_INSTALL_ROOT}/opt/csw/etc"
readonly NEW_CONFDIR_ABS="${PKG_INSTALL_ROOT}/etc/opt/csw"

cleanup() {
tree "${WORK_DIR}"
echo "To clean up:"
echo "rm -rf \"${WORK_DIR}\""
read -p "Clean? [y/n] > " ANSWER
if [[ "${ANSWER}" == y ]]
then
  rm -rf "${WORK_DIR}"
else
  echo "Not removing."
fi
}

trap cleanup EXIT

echo "Working in '${WORK_DIR}'"
mkdir -p "${PKG_INSTALL_ROOT}"
mkdir -p "${SRC_DIR}"

# Place files
echo "MIGRATE_FILES=\"foo.conf bar.d\"" > "${SRC_DIR}/foo"
mkdir -p "${OLD_CONFDIR_ABS}"
echo "foo: bar" > "${OLD_CONFDIR_ABS}/foo.conf"

mkdir -p "${OLD_CONFDIR_ABS}/bar.d"
echo "I am the bar daemon." > "${OLD_CONFDIR_ABS}/bar.d/bar.conf"
echo "I have two configuration files." > "${OLD_CONFDIR_ABS}/bar.d/baz.conf"

# And a directory

# Running the script

echo "${SRC_DIR}/foo bar" | PKG_INSTALL_ROOT=${PKG_INSTALL_ROOT} /bin/sh -x "${CAS_DIR}/${CAS_UNDER_TEST}"

if [[ $? -ne 0 ]]; then
  echo "Test failed."
fi

# Verification
# What?

