import os
import sys


def txt_importer(filename):
    if not os.path.isfile(filename):
        sys.stderr.write(f"Arquivo {filename} não encontrado\n")
        return

    _, extension = os.path.splitext(filename)
    if extension != ".txt":
        sys.stderr.write("Formato inválido\n")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.rstrip('\n') for line in lines]

    return lines
