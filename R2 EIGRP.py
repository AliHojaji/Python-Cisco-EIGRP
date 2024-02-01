from netmiko import ConnectHandler

r14 = {
    'device_type': 'cisco_ios',
    'ip': '11.11.11.5',
    'username': 'Ali',
    'password': 'Hojaji',
}
net_connect = ConnectHandler(**r14)

config_commands = ['router EIGRP 90', 'no auto-summary', 'network 11.11.11.4 0.0.0.3', 'network 11.11.11.8 0.0.0.3']
output = net_connect.send_config_set(config_commands)
print(output)