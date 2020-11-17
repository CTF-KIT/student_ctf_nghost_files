# [Night mode task](https://student.ctf.su/nightmode)

### Solution:
 * Scan website with DirBuster
 * Use git-dumper for download .git files
 * Use "cat-git-object.py" for decompress object files
 * upload.php:32 have header inject
 ```php
 header("Content-Disposition: attachment; filename=\"".$file['filename']."\"");
 ```
 * Put CR (0x0d) byte to filename will break header line
 * Use two step exploit upload (poc.js + payload.html)
 * Report link file and receive base64(secret) on server