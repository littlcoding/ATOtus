import json
import os
import re
from dataclasses import dataclass
from datetime import datetime


# Custom json encoder to serialize request info objects
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


@dataclass
class RequestInfo:
    generation_time: int = 0
    method: str = ''
    ip: str = ''
    url: str = ''
    datetime: str = ''


def get_path_from_user_input():
    file_path = input("Enter the path: ")
    is_path = os.path.exists(file_path)

    if not is_path:
        raise Exception("Enter the valid path!")

    return file_path


def get_all_file_names_from_path(file_path):  # get all files from path, return file names
    is_file = os.path.isfile(file_path)  # checks if path is a file
    is_directory = os.path.isdir(file_path)  # checks if path is a directory

    if is_file:
        return [file_path]

    if is_directory:
        return list(
            map(
                lambda x: os.path.join(os.path.abspath(file_path), x),
                os.listdir(file_path)
            )
        )

    raise Exception("File path must be file or directory")


def get_imploded_data_from_files(file_paths):
    data = ''

    for file_path in file_paths:
        with open(f'{file_path}') as f:
            data += '\n' + f.read()

    return data


def parse_data_as_log_requests(data):
    regex = r"(?P<ip>.*?) (?P<remote_log_name>.*?) (?P<userid>.*?) \[(?P<date>.*?)(?= ) (?P<timezone>.*?)\] " \
            r"\"(?P<request_method>.*?) (?P<path>.*?)(?P<request_version> HTTP/.*)?\" (?P<status>.*?) " \
            r"(?P<length>.*?) \"(?P<referrer>.*?)\" \"(?P<user_agent>.*?)\" (?P<generation_time_micro>.*)"

    matches = re.finditer(regex, data)
    infos = []

    for matchNum, match in enumerate(matches):
        info = RequestInfo()
        info.generation_time = int(match.group('generation_time_micro'))
        info.method = match.group('request_method')
        info.ip = match.group('ip')
        info.url = match.group('referrer')
        info.datetime = match.group('date')

        infos.append(info)

    return infos


def get_requests_statistic(infos):
    valid_http_methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']
    http_methods_counter = dict.fromkeys(valid_http_methods, 0)
    request_ips_counter = {}

    total_requests = len(infos)
    for request in infos:
        if request.method in valid_http_methods:
            http_methods_counter[request.method] += 1

        if request.ip not in request_ips_counter:
            request_ips_counter[request.ip] = 0
        request_ips_counter[request.ip] += 1

    most_frequency_ips = list(
        dict(
            sorted(
                request_ips_counter.items(),
                key=lambda item: item[1],
                reverse=True
            )[:3]
        ).keys()
    )
    longest_generation_time = sorted(infos, key=lambda info: info.generation_time, reverse=True)[:3]

    return {
        'Total requests': total_requests,
        'Requested methods count': {
            'GET': http_methods_counter['GET'],
            'HEAD': http_methods_counter['HEAD'],
            'POST': http_methods_counter['POST'],
            'PUT': http_methods_counter['PUT'],
            'DELETE': http_methods_counter['DELETE'],
            'CONNECT': http_methods_counter['CONNECT'],
            'OPTIONS': http_methods_counter['OPTIONS'],
            'TRACE': http_methods_counter['TRACE'],
        },
        'Top 3 requests by ip': most_frequency_ips,
        'Top 3 requests by generation time': longest_generation_time,
    }


def export_system_info_report(data: str, path: str):
    with open(path, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    try:
        path = get_path_from_user_input()
        file_names = get_all_file_names_from_path(path)
        data_from_files = get_imploded_data_from_files(file_names)
        requests = parse_data_as_log_requests(data_from_files)
        stats = get_requests_statistic(requests)
        json_data = json.dumps(stats, indent=4, cls=CustomEncoder)

        print(json_data)

        export_filename = f'./{datetime.now().isoformat()}-requests-stats.json'
        export_system_info_report(json_data, export_filename)
    except Exception as e:
        print(f'Failed to parse logs files: {str(e)}')