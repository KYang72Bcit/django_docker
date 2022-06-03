import multiprocessing

bind = '0.0.0.0:8000'

workers = multiprocessing.cpu_count() * 2 + 1

backlog = 2048

work_class = 'gevent'

proc_name = 'employeeManagement' # 进程名称   

pidfile = '/tmp/employManagement.pid' # 设置进程文件目录   

timeout = 30 # 超时   
max_requests = 6000 # 最大请求数   
