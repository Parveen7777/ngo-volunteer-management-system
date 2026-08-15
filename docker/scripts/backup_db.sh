#!/bin/sh

BACKUP_DIR=database/backups
DB_FILE=database/ngo.db

mkdir -p $BACKUP_DIR

cp $DB_FILE $BACKUP_DIR/ngo_backup_$(date +%Y%m%d_%H%M%S).db

echo "Database backup completed."
