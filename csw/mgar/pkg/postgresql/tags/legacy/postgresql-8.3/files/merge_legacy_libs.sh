#!/opt/csw/bin/bash
# $Id$

set -u
set -e
set -x

declare -r ARCH=$1
declare -r SOURCE_DIR=$2
declare -r TARGET_DIR=$3

if [[ "${ARCH}" = "i386" ]]; then
  archs="i386 amd64"
elif [[ "${ARCH}" = "sparc" ]]; then
  archs="sparcv8 sparcv9"
else
  echo "Wrong arch: ${ARCH}"
  exit 1
fi

for arch in ${archs}; do
  files=${SOURCE_DIR}/lib*-${arch}-*
  for f in $files; do
    if [[ -r ${f} ]]; then
      bn=$(basename ${f})
      soname=$(echo $bn | cut -d- -f1)
      filename=$(echo $bn | cut -d- -f3)
      echo + ${bn}
      if [[ "${arch}" = "sparcv8" || "${arch}" = "i386" ]]; then
        gcp ${SOURCE_DIR}/${bn} ${TARGET_DIR}/${filename}
        gln -s ${filename} ${TARGET_DIR}/${soname}
      else
        mkdir -p ${TARGET_DIR}/${arch}
        gcp ${SOURCE_DIR}/${bn} ${TARGET_DIR}/${arch}/${filename}
        gln -s ${filename} ${TARGET_DIR}/${arch}/${soname}
      fi
    else
      echo - ${f}
    fi
  done
done
