backup-fuzzer
=============

File Backup Fuzzer is a small script to generate a fuzz list of potential backup files that may be inadvertently present on web folders, available for download thanks to sloppy admins.

Examples: 

* wp-config.php~
* .wp-config.php.swp
* wp-config.php.tgz
* wp-config.php.bak
* wp-config.php_20141705
* wp-config.txt
* ...

```
Examples of usage showing the number of variations generated:

$ python backup_fuzzer.py  "wp-config.php" | wc -l
1270200
$ python backup_fuzzer.py -bd  "wp-config.php" | wc -l
302520
$ python backup_fuzzer.py  "wp-config.php" | wc -l
1270200
$ python backup_fuzzer.py --basic-dates "wp-config.php" | wc -l
302520
$ python backup_fuzzer.py --no-dates "wp-config.php" | wc -l
120
$ python backup_fuzzer.py --case-sensitive "wp-config.php" | wc -l
3810600
$ python backup_fuzzer.py --years 0 "wp-config.php" | wc -l
661080
$ python backup_fuzzer.py --years 0 --basic-dates --case-sensitive "wp-config.php" | wc -l
389160
```


