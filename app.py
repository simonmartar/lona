from scanner import Scanner

from monitor import Monitor

from report import print_report

scanner = Scanner()

disks = scanner.scan()

report = Monitor().analyze(

    disks

)

print_report(

    report

)
