import os
import click
from jinja2 import Environment, FileSystemLoader


@click.command()
@click.argument('provider_name')
def main(provider_name):
    j2_env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True)
    compose = j2_env.get_template('provider_router.jinja2').render(provider_name=provider_name)

    with open(os.path.join("routes", "%s.py" % provider_name), "w") as f:
        f.write(compose)


if __name__ == "__main__":
    main()
