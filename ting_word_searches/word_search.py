def exists_word(word, instance):

    results = []

    current_node = instance.first
    while current_node is not None:
        file = current_node.value
        occurrences = []

        for i, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({"linha": i + 1})

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

        current_node = current_node.next

    return results


def search_by_word(word, instance):
    pass
