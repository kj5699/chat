import socket
HOST='134.209.106.40'
PORT=443

request='''GET / HTTPS/1.0
Host: www.pyjaipur.org


'''

with socket.socket() as s:
	s.connect((HOST,PORT))
	s.sendall(request.encode())
	doc=''
	while True:
		data=s.recv(4096)
		if not data:
			break
		doc+=data.decode()

print(doc)
