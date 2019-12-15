#! /bin/bash

backup_dir=/media/jin/5C0ED9670ED93B2A/MINT14_Backup/home/jin/
time=$(date +%Y%m%d)
week=$(date +%a)

# If not Full Backup Exists:
if [ ! -f $backup_dir/home_bak_full_*.tgz ]; then
	cat $backup_dir/backup_include.list | xargs tar zcvfp $backup_dir/home_bak_full_$time.tgz -g $backup_dir/backup.info

# Daily Incremental Backup
else
	cat $backup_dir/backup_include.list | xargs tar zcvfp $backup_dir/home_bak_incr_$time.tgz -g $backup_dir/$backup.info
fi
