#!/bin/bash
#
# update-t4-patch - retrieve the last t4 engine patch from
#                   hg.openindiana.org repository 
#           

T4_ENGINE_FILES="eng_t4_aes_asm.h eng_t4_bignum.h eng_t4_des_asm.h eng_t4_err.h eng_t4_sha2_asm.h \
                 eng_t4.c eng_t4_des.c eng_t4_err.c eng_t4_md5.c eng_t4_montmul.c eng_t4_sha1.c eng_t4_sha256.c eng_t4_sha512.c \
                 t4_aes.S t4_des.S t4_md5.S t4_sha1.S t4_sha2.S"
MERCURIAL_URL="https://hg.openindiana.org/upstream/oracle/userland-gate/raw-file/tip/components/openssl/openssl-1.0.1/"
WGET_OPTIONS="--quiet"


if [[ -z "$1" ]]; then
	echo "Usage: update-t4-patch.sh OPENSSL_VERSION"
	exit 1
fi

VERSION="$1"
PATCH_FILE="openssl-${VERSION}-t4-engine.sparc-patch"
PATCH_DATE=$(date +"%Y-%m-%d %H:%M:%S.%N %z")

echo "Updating t4 engine patch from ${MERCURIAL_URL}..."
(
	# ar in in /usr/ccs/bin under Solaris 9 and 10 so we change the path
	wget $WGET_OPTIONS --output-document=- ${MERCURIAL_URL}/patches/openssl-${VERSION}-t4-engine.sparc-patch | \
		sed -e 's/\/usr\/bin\/ar/\/usr\/ccs\/bin\/ar/g'

	# in the repository, the new files are not part of the patch, but we merge them
	# in a single patch
	for FILE in $T4_ENGINE_FILES; do \
		if [[ "${FILE##*.}" != "S" ]]; then
			DIR="engine"
		else
			DIR="${FILE:3:3}/asm"
		fi

		wget $WGET_OPTIONS --output-document="${PATCH_FILE}.tmp" "${MERCURIAL_URL}/engines/t4/$FILE"
		NB_LINES=$(wc -l "${PATCH_FILE}.tmp" | awk '{ print $1 }')

		echo "Index: crypto/$DIR/$FILE"
		echo "==================================================================="
		echo "diff -uNr openssl-${VERSION}/$DIR/$FILE openssl-${VERSION}/$DIR/$FILE"
		echo "--- openssl-${VERSION}/crypto/$DIR/$FILE 1970-01-01 01:00:00.000000000 +0100"
		echo "+++ openssl-${VERSION}/crypto/$DIR/$FILE ${PATCH_DATE}"
		echo "@@ -0,0 +1,${NB_LINES} @@"
		sed -e 's/^/+/' "${PATCH_FILE}.tmp"
	done
) > "${PATCH_FILE}"

rm -f "${PATCH_FILE}.tmp"
echo "Updated patch in ${PATCH_FILE}"



