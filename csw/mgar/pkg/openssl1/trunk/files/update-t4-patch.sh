#!/bin/bash
#
# update-t4-patch - retrieve the last t4 engine patch from
#                   hg.openindiana.org repository 
#           

T4_ENGINE_FILES="sparc_arch.h md5-sparcv9.pl aest4-sparcv9.pl dest4-sparcv9.pl sparcv9_modes.pl vis3-mont.pl sparcv9-gf2m.pl sparct4-mont.pl"
MAIN_T4_PATCH_FILE="103-openssl_t4_inline.patch"
#SOURCE_URL="http://buildfarm.opencsw.org/source/raw/solaris-userland/components/openssl/openssl-1.0.1/"
SOURCE_URL="https://hg.openindiana.org/upstream/oracle/userland-gate/raw-file/default/components/openssl/openssl-1.0.1/"
WGET_OPTIONS="--quiet"


if [[ -z "$1" ]]; then
	echo "Usage: update-t4-patch.sh OPENSSL_VERSION"
	exit 1
fi

VERSION="$1"
PATCH_FILE="openssl-${VERSION}-t4-engine.sparc.5.11.patch"
PATCH_DATE=$(date +"%Y-%m-%d %H:%M:%S.%N %z")

echo "Updating t4 engine patch from ${SOURCE_URL}..."
(
	# ar in in /usr/ccs/bin under Solaris 9 and 10 so we change the path
	wget $WGET_OPTIONS --output-document=- ${SOURCE_URL}/patches/${MAIN_T4_PATCH_FILE} | \
		sed -e 's/\/usr\/bin\/ar/\/usr\/ccs\/bin\/ar/g'

	# in the repository, the new files are not part of the patch, but we merge them
	# in a single patch
	for FILE in $T4_ENGINE_FILES; do \
		if [[ "${FILE##*.}" = "h" ]]; then
			DIR="crypto"
		elif echo "$FILE" | grep -- '-sparcv9.pl' >/dev/null; then
			DIR="crypto/${FILE:0:3}/asm"
		elif [[ "$FILE" = "sparcv9_modes.pl" ]]; then
			DIR="crypto/perlasm"
		else
			DIR="crypto/bn/asm"
		fi

		wget $WGET_OPTIONS --output-document="${PATCH_FILE}.tmp" "${SOURCE_URL}/inline-t4/$FILE"
		NB_LINES=$(wc -l "${PATCH_FILE}.tmp" | awk '{ print $1 }')

		echo "Index: $DIR/$FILE"
		echo "==================================================================="
		echo "diff -uNr openssl-${VERSION}/$DIR/$FILE openssl-${VERSION}/$DIR/$FILE"
		echo "--- openssl-${VERSION}/$DIR/$FILE 1970-01-01 01:00:00.000000000 +0100"
		echo "+++ openssl-${VERSION}/$DIR/$FILE ${PATCH_DATE}"
		echo "@@ -0,0 +1,${NB_LINES} @@"
		sed -e 's/^/+/' "${PATCH_FILE}.tmp"
	done
) > "${PATCH_FILE}"

rm -f "${PATCH_FILE}.tmp"
echo "Updated patch in ${PATCH_FILE}"



