import sys
from dataclasses import dataclass, field
from datetime import datetime
from subprocess import run, PIPE


@dataclass
class SystemInfo:
    users_processes_count: dict = field(init=False, default_factory=dict)  # {string(user): int(processes count)}
    total_cpu: float = 0.0
    total_mem: float = 0.0
    max_cpu: float = 0.0
    max_mem: float = 0.0
    total_processes: int = 0
    max_cpu_command: str = ''
    max_mem_command: str = ''

    def get_report(self):
        return "\n".join([
            "SYSTEM INFO REPORT\n",
            f'system users: {", ".join(self.users_processes_count.keys())}',
            f'total processes count: {self.total_processes}',
            f'total user processes:',
            f'{self.get_users_processes_string()}',
            f'total memory using: {self.total_mem}',
            f'total cpu using: {self.total_cpu}',
            f'max memory using process: {self.max_mem_command[:20]}',
            f'max cpu using process: {self.max_cpu_command[:20]}',
        ])

    def get_users_processes_string(self):
        result_array = []

        for user, count in self.users_processes_count.items():
            result_array.append(f'\t{user}: {count}')

        return "\n".join(result_array)


def get_system_info():
    ps_aux_result = run(["ps", "aux"], stdout=PIPE)
    ps_aux_result_lines = str(ps_aux_result.stdout).split('\\n')

    column_names_line_skipped = False

    info = SystemInfo()

    for line in ps_aux_result_lines:
        if not column_names_line_skipped:
            column_names_line_skipped = True
            continue

        if len(line) < 10:  # skip invalid lines
            continue

        info.total_processes += 1

        line_values = line.split()

        line_cpu = float(line_values[2])
        line_mem = float(line_values[3])

        info.total_cpu += line_cpu
        info.total_mem += line_mem

        line_command = " ".join(line_values[10:])

        if line_cpu > info.max_cpu:
            info.max_cpu = line_cpu
            info.max_cpu_command = line_command

        if line_mem > info.max_mem:
            info.max_mem = line_mem
            info.max_mem_command = line_command

        line_user = line_values[0]

        if info.users_processes_count.get(line_user) is None:
            info.users_processes_count[line_user] = 0

        info.users_processes_count[line_user] += 1

    return info


def export_system_info_report(data: str, path: str):
    with open(path, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    print("Getting system info")
    system_info = get_system_info()
    system_info_report = system_info.get_report()

    print("Print system info report to stdout:")
    print(system_info_report, file=sys.stdout)

    export_filename = f'./{datetime.now().isoformat()}-report.txt'
    print(f'\nExport system info report to file: {export_filename}')
    export_system_info_report(system_info_report, export_filename)

    print("Done")
