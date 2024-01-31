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
    if instance._size == 0:
        return print("Não há elementos")

    text = instance.dequeue()
    return print(f"Arquivo {text['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    pass
