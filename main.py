import code
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

svc_list = []

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    
task_list = (os.popen("tasklist").read()).split('\n')

for row in task_list:
   if 'svc' in row or 'PulseSecureService' in row: # Look for descriptor ID of application
        svc_list.append(row)
        row = ' '.join(row.split())
        pid = row.split(' ')[1]
        try:
            os.system('Taskkill /PID {} /F'.format(str(pid)))
        except:
            print ('Could not kill PID {}.\n Please review: \n{}').format(pid, row)

