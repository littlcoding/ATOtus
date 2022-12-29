import socket
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

status_codes = []
for status in list(HTTPStatus):
    status_codes.append(status.value)


def status_code_to_http_response_status(status_code):
    if status_code in status_codes:
        index = status_codes.index(status_code)
        status_for_search = list(HTTPStatus)

        return f'{status_code} {status_for_search[index].phrase}'

    return '200 OK'


if __name__ == '__main__':
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)

    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        parts = request.split('\n')
        headers = parts[2:]
        first_part = parts[0]
        first_part_separated = first_part.split(" ")

        method = first_part_separated[0]

        req_address = parts[1].split(': ')[1]
        req_host = req_address.split(':')[0].strip()
        req_port = req_address.split(':')[1].strip()

        response_code = '200 OK'
        try:
            parse_result = urlparse(f'{SERVER_HOST}{first_part_separated[1]}')
            query_params = parse_qs(parse_result.query)
            if query_params.get('status'):
                response_code = status_code_to_http_response_status(int(query_params.get('status')[0]))
        except:
            print("Failed to parse query status param, keep 200 OK")

        data_to_response = [
            f"Request Method: {method}",
            f"Request Source: ('{req_host}', {req_port})",
            f"Response Status: {response_code}"
        ]

        for header in headers:
            data_to_response.append(f"{header}")

        response_body = "\n".join(data_to_response)

        # Send HTTP response
        response = f'HTTP/1.0 {response_code}\n\n{response_body}'
        client_connection.sendall(response.encode())
        client_connection.close()

    # Close socket
    server_socket.close()
