import click
import subprocess
import re


@click.command()
@click.option('--dirname', default='.')
@click.option('--size', default=0)


def show_files_greater(dirname, size):
    whole_output = subprocess.check_output(f'ls -Sla --block-size=MB {dirname}', shell=True).decode('utf-8')
    for line in whole_output.split("\n")[1:-1]:
        file_size = line.split()
        if int(file_size[4][:-2]) > size:
            print(line)
        else:
            break

if __name__ == '__main__':
    show_files_greater()

# example of executing:
# python3 ./script1.py --dirname=/ --size=1 
