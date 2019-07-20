import click
import jinja2
from os.path import join, dirname


@click.group()
def main(args=None):
    """Cùng tạo nên những bộ dữ liệu thật hay"""
    pass

SUPPORTED_TASKS = {
    'add_sentence'
}

template_folder = join(dirname(__file__), "templates")
template_loader = jinja2.FileSystemLoader(searchpath=template_folder)
tempalte_env = jinja2.Environment(loader=template_loader)

@main.command()
@click.argument('task', required=True)
def propose(task):
    template_file = "PROPOSE_TASK.console"
    template = tempalte_env.get_template(template_file)
    outputText = template.render()  # this is where to put args to the template renderer
    if task not in SUPPORTED_TASKS:
        print(f'Hiện tại hệ thống không hỗ trợ task {task}')
    else:
     print(outputText)


@main.command()
@click.argument('task', required=True)
def submit():
    print("Propose a task")

if __name__ == "__main__":
    main()