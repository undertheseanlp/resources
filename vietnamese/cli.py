import os

import click
import jinja2
from os.path import join, dirname
import subprocess

from vietnamese.task import check_is_in_correct_directory


@click.group()
def main(args=None):
    """Cùng dạy máy tính thông minh hơn"""
    pass

SUPPORTED_TASKS = {
    'add_sentence'
}

template_folder = join(dirname(__file__), "templates")
template_loader = jinja2.FileSystemLoader(searchpath=template_folder)
template_env = jinja2.Environment(loader=template_loader)

@main.command()
@click.argument('task', required=True)
def propose(task):
    check_is_in_correct_directory()
    template_file = "PROPOSE_TASK.tpl"
    template = template_env.get_template(template_file)
    outputText = template.render()  # this is where to put args to the template renderer
    if task not in SUPPORTED_TASKS:
        print(f'Hiện tại hệ thống không hỗ trợ task {task}')
    else:
     print(outputText)
    # create file
    cwd = os.getcwd()
    f = open(join(cwd, "propose", "add_sentence.txt"), "w")
    template = template_env.get_template("ADD_SENTENCE.tpl")
    content = template.render()
    f.write(content)

@main.command()
def submit():
    output = subprocess.check_output(["git", "add", "-A"])
    output = subprocess.check_output(["git", "commit", "-m", "'update'"])
    output = subprocess.check_output(["git", "push", "origin", "master"])
    print("Submit")

if __name__ == "__main__":
    main()