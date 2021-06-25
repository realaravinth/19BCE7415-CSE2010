# Lab3

- Name: Aravinth TM
- Registration Number: 19BCE7415

## Script

### browser location

```bash
which firefox
```

### file replication

#### multiple ways to do it:

###### if root:

```bash
sudo updatedb
locate File1(*
```

##### if not root

```bash
cd /
find | grep "File1("
```

### File replication script

#### Script

```bash
#!/bin/bash

touch File1

for i in {0..50}
do
	cp File1 File1
	cp File1 File1\($i\)
done

ls
```

#### Output

```bash
 File1       'File1(15)'  'File1(22)'  'File1(3)'   'File1(37)'  'File1(44)'  'File1(6)'
'File1(0)'   'File1(16)'  'File1(23)'  'File1(30)'  'File1(38)'  'File1(45)'  'File1(7)'
'File1(1)'   'File1(17)'  'File1(24)'  'File1(31)'  'File1(39)'  'File1(46)'  'File1(8)'
'File1(10)'  'File1(18)'  'File1(25)'  'File1(32)'  'File1(4)'   'File1(47)'  'File1(9)'
'File1(11)'  'File1(19)'  'File1(26)'  'File1(33)'  'File1(40)'  'File1(48)'
'File1(12)'  'File1(2)'   'File1(27)'  'File1(34)'  'File1(41)'  'File1(49)'
'File1(13)'  'File1(20)'  'File1(28)'  'File1(35)'  'File1(42)'  'File1(5)'
'File1(14)'  'File1(21)'  'File1(29)'  'File1(36)'  'File1(43)'  'File1(50)'
```

## Scheduling tasks

# Schedule a task

```bash
➜  lab3 git:(master) ✗ crontab 19bce7415_Task1
➜  lab3 git:(master) ✗ crontab -l
30 10 * * 7 /usr/bin/notify-send "running cron job"
```

Executes at 10:30 every day

## Change time of the previous task

```bash
➜  lab3 git:(master) ✗ crontab 19bce7415_Task1
➜  lab3 git:(master) ✗ crontab -l
30 17 * * 7 /usr/bin/notify-send "running cron job"
```

Executes at 17:30 every day

### Schedule new task to run only on weekdays

```bash
➜  lab3 git:(master) ✗ crontab 19bce7415_Task1
➜  lab3 git:(master) ✗ crontab -l
30 17 * * 7 /usr/bin/notify-send "running cron job"
30 17 * * 1-5 /usr/bin/notify-send "running weekdays only cron job"
```

Executes at 17:30 every weekday
