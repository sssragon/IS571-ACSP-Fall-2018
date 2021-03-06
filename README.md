# IS571-ACSP-Fall-2018 

> The goal of the course is raising up the ability of security vulnerability analysis. We will practice debugging and exploitation of the vulnerability examples. Each student will analyze, exploit and present assigned vulnerabilities which are patched vulnerabilities of the web browsers.

### About the course
* Instructor
	* Jaeseo Lee (jaeseo.lee@kaist.ac.kr)
	* (macOS Part) Sunghun Kim (wanhuns@kaist.ac.kr)
* Course: IS571 Advanced Cyber Security Practice
* Time: Mon. 14:30 ~ 15:45 / Wed. 14:30 ~ 15:45
* Location: N1 #317
* Office hour: 4:00 pm - 5:30 pm (Mon. and Wed.) at N5 2218
* Grading
	* <del>20%</del> 30% Lab assignments
	* 20% Reports
	* <del>20%</del> 30% Project 
	* <del>20% Mid-term Exam</del>
	* 20% macOS Part
* Late submission policy 
	* Lab: late assignments will be assessed a late penalty of 50%.
	* Report: a late penalty of 10% per day.
* If you want to know slide key, email me

### Schedule
| Date       |  No.    | Topic           | Notes 
|------------|-----------------|-----------------|-------
| 27/08/2018 | 01 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec01/01-Introduction.pdf'>Introduction</a>
| 29/08/2018 | 02 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec02/02-Security Vulnerability.pdf'>Security Vulnerability</a> (1/2)
| 03/09/2018 | | Security Vulnerability (2/2)
| 05/09/2018 | 03 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec03/03-Windows Debugger.pdf'>Windows Debugger</a> | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec03/WinDbg_A_to_Z.pdf'>WinDbg_A_to_Z</a>
| 10/09/2018 | 04 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec04/04-Windows Heap Internals.pdf'>Windows Heap Internals</a> (1/2) - Standard Heap
| 12/09/2018 | | Windows Heap Internals (2/2) - LFH Heap | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec04/Understanding_the_Low_Fragmentation_Heap.pdf'>Win7 LFH Heap</a><br><a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec04/Windows_8_Heap_Internals.pdf'>Win8 Heap Internals</a><br><a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec04/Windows_10_Internals.pdf'>Win10 Segment Heap Internals</a><br><a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec04/04-Windows Heap Internals-Report01.pdf'>Report #1</a> (~9.30.)
| 17/09/2018 | 05 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec05/05-Custom Heap Manager.pdf'>Custom Heap Manager</a> (1/3) - About Flash
| 19/09/2018 | | Custom Heap Manager (2/3) - About Chrome
| 24/09/2018 | | No class (Chuseok, Korean Harvest Day)
| 26/09/2018 | | No class (Chuseok, Korean Harvest Day)
| 01/10/2018 | | Custom Heap Manager (3/3) - Extra | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec05/05-Custom Heap Manager-Report02.pdf'>Report #2</a> (~10.21.)
| 03/10/2018 | | No class (National Foundation Day)
| 08/10/2018 | 06 | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec06/06-Objects Tracking.pdf'>Objects Tracking</a> (1/4) - C++ Objects | <a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec06/bh-dc-07-Sabanal_Yason-WP.pdf'>Reversing C++</a>
| 10/10/2018 | | Objects Tracking (2/4) - Flash Objects
| 15/10/2018 | | No class (Midterm week)
| 17/10/2018 | | No class (Midterm week)
| 22/10/2018 | | Objects Tracking (3/4) - Chrome Objects
| 24/10/2018 | 07 | Objects Tracking (4/4) - Chrome Objects<br><a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec07/07-Heap Exploitation.pdf'>Heap Exploitation</a> (1/2)
| 29/10/2018 | 08 | Heap Exploitation (2/2)<br><a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec08/08-RW Primitives.pdf'>RW Primitives</a> (1/2)
| 31/10/2018 | | RW Primitives (2/2) | Report #3 (~11.18.)
| 05/11/2018 | | No class | Supplementary class<br>(12/11/2018 and 14/11/2018)
| 07/11/2018 | | No class | Supplementary class<br>(03/12/2018 and 05/12/2018)
| 12/11/2018 | 09 | Control Flow Hijacking<br>ROP - Return-Oriented Programming | - 14:00\~15:45<br>Calling Conventions<br>Intel® 64 and IA-32 Architectures
| 14/11/2018 | 10 | Shellcode | - 14:00\~15:45
| 19/11/2018 | 11 | macOS Architecture | Mac OS X and IOS Internals: To the Apple's Core
| 21/11/2018 | | macOS March-O and Dynamic Linker
| 26/11/2018 | | macOS Process Internals, Memory Mgmt.,<br> and Objective-C
| 28/11/2018 | | macOS LaunchD, Mach, and Sandbox
| 03/12/2018 | 12 |<a href='https://github.com/jaeseolee/IS571-ACSP-Fall-2018/raw/master/lec12/12-Project.pdf'>Project Presentation</a> (1/2) | - 14:00\~14:25<br>\- 14:25\~14:50<br>\- 14:50\~15:15<br>\- 15:15\~15:40<br>(25 minutes/team)
| 05/12/2018 | | Project Presentation (2/2) | \- 14:00\~14:25<br>\- 14:25\~14:50<br>\- 14:50\~15:15<br>\- 15:15\~15:40
| 10/12/2018 | | No class (Final week)
| 12/12/2018 | | No class (Final week)

### Project Teams
| Team   | Members                      | CVEs                | Notes   |
|--------|------------------------------|---------------------|---------|
| 1 | 20185327, 20183165 | CVE-2017-8548 | Edge |
| 2 | 20183355, 20183218 | Bug-Number: 789393 | Chrome |
| 3 | 20185115, 20183300 | Bug-Number: 789393 | Chrome |
| 4 | 20174323, 20183543, 20185438 | CVE-2015-0311 | Flash |
| 5 | 20183410, 20183669 | CVE-2016-0189 | Internet Explorer |
| 6 | 20183237, 20184276 | CVE-2016-3210 | Internet Explorer |
| 7 | 20183170, 20145347 | CVE-2016-7200, 7201 | Edge |
| 8 | 20183421, 20185403 | Bug-Number: 716044  | Chrome |

Copyright 2017 Jaeseo Lee
