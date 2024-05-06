import psutil
import math
import logging


def CPU_usage():
    usage = psutil.cpu_percent(interval=1,percpu=True)
    cpu = 0
    for i in usage:
        cpu += i
    if cpu > 80:
        print("Alert! ...CPU usage exceeded")
        logging.basicConfig(filename="alert.log", filemode='w')
        logging.warning("Alert! ...CPU usage exceeded")


def memory_usage():
    mem_usage = psutil.virtual_memory().percent
    mem_swap_usage = psutil.swap_memory().percent
    mem = mem_usage + mem_swap_usage
    mem_unused = 200 - mem
    if mem_unused < 10:
        print("Alert! ... Memory Storage Avalability critically low")
        logging.basicConfig(filename="alert.log", filemode='w')
        logging.warning("Alert! ... Memory Storage Avalability critically low")


def disk_space():
    #Disk: free space < 10GB
    disk_mountpoint = []
    sdisk = psutil.disk_partitions()
    total_free_disk_space_in_gb = 0
    for disk in sdisk:
       disk_mountpoint.append(disk.mountpoint)
    for mount in disk_mountpoint:
        free_disk_space = psutil.disk_usage(mount).free
        free_disk_space_in_gb = free_disk_space/math.pow(10,9)
        total_free_disk_space_in_gb += free_disk_space_in_gb

    if total_free_disk_space_in_gb < 10:
        print("Alert!...Disk space Availability critically low")
        logging.basicConfig(filename="alert.log", filemode='w')
        logging.warning("Alert!...Disk space Availability critically low")


def running_processes():
#running process limit is 1064
  no_of_running_processes = len(psutil.pids())
  if no_of_running_processes > 1064: #for macos
      print("Alert!... Number of running processes simultaneously very high")
      logging.basicConfig(filename="alert.log", filemode='w')
      logging.warning("Alert!... Number of running processes simultaneously very high")
  else:
      for proc in psutil.process_iter(['pid', 'name', 'username']):
        #print(proc.info)
        logging.basicConfig(filename="alert.log", filemode='w')
        logging.warning(proc)

if __name__ == '__main__':
    CPU_usage()
    memory_usage()
    disk_space()
    running_processes()



