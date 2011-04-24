#!/opt/csw/bin/bash

set -x
set -u
set -e

readonly CAS_DIR="files"
readonly CAS_UNDER_TEST="CSWcswclassutils.i.cswmigrateconf"
readonly TMP_DIR="$(gmktemp -d castest.XXXXXXXXXX)"
readonly SRC_DIR="${TMP_DIR}/src"
PKG_INSTALL_ROOT="${TMP_DIR}/root"
readonly OLD_CONFDIR_ABS="${PKG_INSTALL_ROOT}/opt/csw/etc"
readonly NEW_CONFDIR_ABS="${PKG_INSTALL_ROOT}/etc/opt/csw"

cleanup() {
tree "${TMP_DIR}"
echo "To clean up:"
echo "rm -rf \"${TMP_DIR}\""
read -p "Clean? [y/n] > " ANSWER
if [[ "${ANSWER}" == y ]]
then
  rm -rf "${TMP_DIR}"
else
  echo "Not removing."
fi
}

trap cleanup EXIT

echo "Working in '${TMP_DIR}'"
mkdir -p "${PKG_INSTALL_ROOT}"
mkdir -p "${SRC_DIR}"

# Place files
echo "MIGRATE_FILES=\"foo.conf bar.d\"" > "${SRC_DIR}/foo"
echo "MIGRATE_FILES=\"bar.d\"" > "${SRC_DIR}/foo"
mkdir -p "${OLD_CONFDIR_ABS}"
echo "foo: bar" > "${OLD_CONFDIR_ABS}/foo.conf"

mkdir -p "${OLD_CONFDIR_ABS}/bar.d"
echo "I am the bar daemon." > "${OLD_CONFDIR_ABS}/bar.d/bar.conf"

# And a directory

# Running the script

echo "${SRC_DIR}/foo bar" | PKG_INSTALL_ROOT=${PKG_INSTALL_ROOT} /bin/sh -x "${CAS_DIR}/${CAS_UNDER_TEST}"

if [[ $? -ne 0 ]]; then
  echo "Test failed."
fi

# Verification
# What?

