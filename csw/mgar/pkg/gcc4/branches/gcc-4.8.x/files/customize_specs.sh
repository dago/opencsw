#!/opt/csw/bin/bash

# This script generates and modifies a GCC specs file which after placing on
# the filesystem will automatically add -R/opt/csw/lib to all gcc/g++
# invocations.

set -x
set -e

DESTDIR=$1
PROGRAM_SUFFIX=$2
VERSION=$3

# Creating a modified specs file
# In the global modulation, the gcc binary is not there.
gcc_bin="${DESTDIR}/opt/csw/bin/gcc${PROGRAM_SUFFIX}"
if [[ -x "${gcc_bin}" ]]; then
  "${gcc_bin}" -dumpspecs > specs
  gsed -i \
    -e \
    '/\*lib:/,+1 s+%.*+& %{m64:-R /opt/csw/lib/64 } %{!m64:-R /opt/csw/lib}+' \
    specs
  # Since the inclusion of the Go language, there are 3 directories named
  # $(VERSION). Two of them are related to the language, and can be filtered
  # out by matching "/go/".
  target="$(gfind ${DESTDIR}/opt/csw/lib -name ${VERSION} -type d -print \
	    | ggrep -v /go/)"
  gmv -v specs "${target}"
fi
