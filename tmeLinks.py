# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:19:16 2023

@author: F.Tessari
"""

import os
import re

# Lista de todos os arquivos .html no diretório atual
html_files = [filename for filename in os.listdir() if filename.endswith(".html")]

# Verifica se há arquivos .html no diretório
if not html_files:
    print("Nenhum arquivo .html encontrado no diretório atual.")
else:
    # Cria uma lista para armazenar todos os links
    all_links = []

    for input_filename in html_files:
        with open(input_filename, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Use uma expressão regular para encontrar todas as linhas entre aspas
        lines_between_quotes = re.findall(r'"(.*?)"', html_content)

        # Cria uma lista para armazenar links com '@' ou 't.me'
        links = []

        for line in lines_between_quotes:
            if "@" in line or "t.me" in line:
                # Substitui "http://" por "https://"
                if line.startswith("t.me/"):
                    line = "https://" + line
                elif line.startswith("http://"):
                    line = line.replace("http://", "https://")
                links.append(line)

        # Remove linhas que contenham "return"
        links = [link for link in links if "return" not in link]

        all_links.extend(links)

    # Remove linhas duplicadas
    unique_links = list(set(all_links))

    # Organiza as linhas por ordem alfabética
    unique_links.sort()

    # Abre o arquivo de saída
    with open("lista.txt", "w", encoding="utf-8") as output_file:
        # Escreve o título "Links" e as linhas corrigidas e organizadas no arquivo
        output_file.write("Links:\n")
        for link in unique_links:
            output_file.write(link + "\n")

    print("Lista de links salva em lista.txt.")
