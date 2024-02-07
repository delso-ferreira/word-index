def verify_content(line, word, verify: bool):
    if verify:
        return {
            "linha": line + 1,
            "conteudo": word
        }
    return {
        "linha": line + 1
    }


def exists_word(word, instance, verify: bool = False):

    results = []

    current_node = instance.first
    while current_node is not None:
        file = current_node.value
        occurrences = []

        for i, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append(verify_content(i, line, verify))

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

        current_node = current_node.next

    return results


def search_by_word(word, instance):
    return exists_word(word, instance, True)
