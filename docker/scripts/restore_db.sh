#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: ./restore_db.sh backup_file.db"
    exit 1
fi

cp $1 database/ngo.db

echo "Database restored successfully."
