openssl rand -base64 741 > ${PWD}/mongodb/keyfile
chmod 600 ${PWD}/mongodb/keyfile
chown 999:999 ${PWD}/mongodb/keyfile
