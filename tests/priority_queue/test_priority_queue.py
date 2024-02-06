import pytest
from ting_file_management.priority_queue import PriorityQueue


@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_enqueue_priority(priority_queue):
    priority_queue.enqueue({
        'nome_do_arquivo': 'file1.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': ['line1', 'line2', 'line3', 'line4']
    })
    priority_queue.enqueue({
        'nome_do_arquivo': 'file2.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [
            'line1', 'line2', 'line3', 'line4', 'line5', 'line6'
        ]
    })
    assert len(priority_queue) == 2


def test_dequeue_priority(priority_queue):
    priority_queue.enqueue({
        'nome_do_arquivo': 'file1.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': ['line1', 'line2', 'line3', 'line4']
    })
    priority_queue.enqueue({
        'nome_do_arquivo': 'file2.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [
            'line1', 'line2', 'line3', 'line4', 'line5', 'line6'
        ]
    })
    assert priority_queue.dequeue()['nome_do_arquivo'] == 'file1.txt'


def test_dequeue_regular(priority_queue):
    priority_queue.enqueue({
        'nome_do_arquivo': 'file1.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': ['line1', 'line2', 'line3', 'line4']
    })
    priority_queue.enqueue({
        'nome_do_arquivo': 'file2.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [
            'line1', 'line2', 'line3', 'line4', 'line5', 'line6'
        ]
    })

    assert priority_queue.dequeue()['nome_do_arquivo'] == 'file1.txt'
    assert priority_queue.dequeue()['nome_do_arquivo'] == 'file2.txt'


def test_search_priority(priority_queue):
    priority_queue.enqueue({
        'nome_do_arquivo': 'file1.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': ['line1', 'line2', 'line3', 'line4']
    })
    priority_queue.enqueue({
        'nome_do_arquivo': 'file2.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [
            'line1', 'line2', 'line3', 'line4', 'line5', 'line6'
        ]
    })
    assert priority_queue.search(0)['nome_do_arquivo'] == 'file1.txt'


def test_search_regular(priority_queue):
    priority_queue.enqueue({
        'nome_do_arquivo': 'file1.txt',
        'qtd_linhas': 4,
        'linhas_do_arquivo': ['line1', 'line2', 'line3', 'line4']
    })
    priority_queue.enqueue({
        'nome_do_arquivo': 'file2.txt',
        'qtd_linhas': 6,
        'linhas_do_arquivo': [
            'line1', 'line2', 'line3', 'line4', 'line5', 'line6'
        ]
    })
    assert priority_queue.search(1)['nome_do_arquivo'] == 'file2.txt'
