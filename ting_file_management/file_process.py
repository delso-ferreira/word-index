from sys import stdout
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    pointer = instance.first
    while pointer is not None:
        if pointer.value['nome_do_arquivo'] == path_file:
            return
        pointer = pointer.next

    text = txt_importer(path_file)
    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(text),
        'linhas_do_arquivo': text,
        }
    instance.enqueue(data)
    print(data)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        stdout.write("Não há elementos\n")
        return
    remove = instance.dequeue()
    stdout.write(f"Arquivo {remove['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
