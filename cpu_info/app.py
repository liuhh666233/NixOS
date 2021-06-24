import time
import os
import click

def cpu_info_check(free_type = "m", interval = 5):
    while True:
        print(time.ctime())
        os.system("duf")
        os.system(f"free -{free_type}")
        time.sleep(interval)

@click.command()
@click.option('free_type', '--f', type = click.STRING,
                help = "The free_type will asign to free -free_type")
@click.option('interval', '--i',
              type = click.INT,
              help = 'Greet the person every interval seconds.')

def main(free_type, interval):
    cpu_info_check(free_type, interval)


if __name__ == '__main__':
    main()
