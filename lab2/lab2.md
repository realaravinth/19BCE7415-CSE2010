# Lab2

- Name: Aravinth TM
- Registration Number: 19BCE7415

## Install software in windows with CMD
```powershell
PS C:\Users\Aravinth\Downloads> msiexec.exe \i 'C:\Users\Aravinth\Downloads\7z1900-x64.msi' \qn \norestart \log C:\Users\Aravinth\Downloads\i.log
```

## Users in system

```bash
userdbctl user
```

### Output

```bash
NAME               DISPOSITION   UID   GID REALNAME            HOME              SHELL
root               intrinsic       0     0 -                   /root             /bin/bash
nobody             intrinsic   65534 65534 Nobody              /                 /usr/bin/nologin
bin                system          1     1 -                   /                 /usr/bin/nologin
daemon             system          2     2 -                   /                 /usr/bin/nologin
mail               system          8    12 -                   /var/spool/mail   /usr/bin/nologin
ftp                system         14    11 -                   /srv/ftp          /usr/bin/nologin
http               system         33    33 -                   /srv/http         /usr/bin/nologin
named              system         40    40 BIND DNS Server     /                 /usr/bin/nologin
uuidd              system         68    68 -                   /                 /usr/bin/nologin
dbus               system         81    81 System Message Bus  /                 /usr/bin/nologin
polkitd            system        102   102 PolicyKit daemon    /                 /usr/bin/nologin
rtkit              system        133   133 RealtimeKit         /proc             /usr/bin/nologin
usbmux             system        140   140 usbmux user         /                 /usr/bin/nologin
nvidia-persistenc… system        143   143 NVIDIA Persistence… /                 /usr/bin/nologin
i2pd               system        966   966 i2pd user           /var/lib/i2pd     /usr/bin/nologin
mysql              system        967   967 MariaDB             /var/lib/mysql    /usr/bin/nologin
openvpn            system        968   968 OpenVPN             /                 /usr/bin/nologin
postgres           system        969   969 PostgreSQL user     /var/lib/postgres /bin/bash
dhcpcd             system        970   970 dhcpcd privilege s… /                 /usr/bin/nologin
redis              system        971   971 Redis in-memory da… /var/lib/redis    /usr/bin/nologin
geoclue            system        973   973 Geoinformation ser… /var/lib/geoclue  /usr/bin/nologin
colord             system        974   974 Color management d… /var/lib/colord   /usr/bin/nologin
avahi              system        975   975 Avahi mDNS/DNS-SD … /                 /usr/bin/nologin
dhcp               system        976   976 DHCP daemon         /                 /usr/bin/nologin
git                system        977   977 git daemon user     /                 /usr/bin/git-shell
systemd-coredump   system        978   978 systemd Core Dumper /                 /usr/bin/nologin
systemd-timesync   system        979   979 systemd Time Synch… /                 /usr/bin/nologin
systemd-resolve    system        980   980 systemd Resolver    /                 /usr/bin/nologin
systemd-network    system        981   981 systemd Network Ma… /                 /usr/bin/nologin
systemd-journal-r… system        982   982 systemd Journal Re… /                 /usr/bin/nologin
aravinth           regular      1000  1000 -                   /home/aravinth    /usr/bin/zsh
```

## List files and attributes

```bash
ls -lag
```

### Output

```bash
total 8.0K
drwxr-xr-x 2 aravinth aravinth 4.0K Feb 13 11:51  .
drwxr-xr-x 4 aravinth aravinth 4.0K Feb 20 18:17  ..
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51  File1
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(0)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(1)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(10)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(11)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(12)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(13)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(14)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(15)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(16)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(17)'
-rw-r--r-- 1 aravinth aravinth    0 Feb 13 11:51 'File1(18)'

# <----snip--->
```

## Sort

```bash
➜  lab2 git:(master) ✗ cat wordlist
───────┬───────────────────────────────────────────────────────────────────────────────────────────
       │ File: wordlist
───────┼───────────────────────────────────────────────────────────────────────────────────────────
   1   │ echo
   2   │ echo
   3   │ echo
   4   │ echo
   5   │ test
   6   │ apple
   7   │ echo
   8   │ echo
   9   │ orange
  10   │ echo
  11   │ echo
───────┴───────────────────────────────────────────────────────────────────────────────────────────
➜  lab2 git:(master) ✗ sort -u wordlist
apple
echo
orange
test
➜  lab2 git:(master) ✗
```

## Directory traversal with `pushd` and popd`

```bash
➜  lab2 git:(master) ✗ mkdir -p 1/2/3/4/5/
➜  lab2 git:(master) ✗ pushd 1
~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  1 git:(master) ✗ pushd 2
~/code/uni-stuff/cse2010/lab2/1/2 ~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010/lab2/1/2/3/4 ~/code/uni-stuff/cse2010/lab2/1/2/3 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  2 git:(master) ✗ pushd 3
~/code/uni-stuff/cse2010/lab2/1/2/3 ~/code/uni-stuff/cse2010/lab2/1/2 ~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010/lab2/1/2/3/4 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  3 git:(master) ✗ pushd 4
~/code/uni-stuff/cse2010/lab2/1/2/3/4 ~/code/uni-stuff/cse2010/lab2/1/2/3 ~/code/uni-stuff/cse2010/lab2/1/2 ~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  4 git:(master) ✗ popd
~/code/uni-stuff/cse2010/lab2/1/2/3 ~/code/uni-stuff/cse2010/lab2/1/2 ~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  3 git:(master) ✗ popd
~/code/uni-stuff/cse2010/lab2/1/2 ~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  2 git:(master) ✗ popd
~/code/uni-stuff/cse2010/lab2/1 ~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  1 git:(master) ✗ popd
~/code/uni-stuff/cse2010/lab2 ~/code/uni-stuff/cse2010 ~ /tmp ~/Syncthing/Books ~/code/uni-stuff/cse2010/lab3/infected ~/code/uni-stuff/cse2010/lab3 ~/code/uni-stuff/cse2010/lab1 ~/code/uni-stuff ~/code/uni-stuff/CSE4004 ~ ~/code/uni-stuff/CSE4004/LAB4 ~/code/uni-stuff/CSE4004/LAB4/p /srv/batsense/vikunja-frontend /srv/batsense /srv
➜  lab2 git:(master) ✗
```
