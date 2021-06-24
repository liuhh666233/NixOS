import time
import os
import click

def cpu_info_check(free_type = "m"):
    while True:
        os.system("duf")
        os.system("free -{free_type}")
        time.sleep(5)

@click.command()
@click.option('free_type', '--t', type = click.STRING,
                help = "The free_type will asign to free -free_type")
def main(free_type):
    cpu_info_check(free_type)


if __name__ == '__main__':
    main()
