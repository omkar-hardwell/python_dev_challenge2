from django.shortcuts import render


def index(request):
    return render(request, 'analytics_app/index.html')


def add(request):
    return render(request, 'analytics_app/add_connection.html')


def create_connection(request):
    host = request.POST.get('ip_address', '')
    port = request.POST.get('port', '')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    import paramiko
    import psutil

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
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
    p = psutil.Process()
    print(p.name(), p.pid, p.status(), p.memory_info())

    # Sensors
    psutil.sensors_temperatures()

    # Users
    psutil.users()

    channel.close()
    client.close()

    # All metrics
    analytics_data = []

    return render(
        request, 'analytics_app/view_connections.html', analytics_data)
