import paramiko
import psutil


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.1.102", 80, 'username', 'password')
channel = client.invoke_shell()
channel.settimeout(0.0)

# CPU Utilization
psutil.cpu_times()

# Memory Utilization
psutil.virtual_memory()
psutil.swap_memory()

# Disks Usage
psutil.disk_usage('/')

# Networks
psutil.net_io_counters(pernic=True)
psutil.net_connections()
psutil.net_if_addrs()
psutil.net_if_stats()


# Running Processes
p = psutil.Process(7055)
print (p.name(), p.pid, p.status(), p.memory_info())

# Sensors
psutil.sensors_temperatures()

# Users
psutil.users()

channel.close()
client.close()
