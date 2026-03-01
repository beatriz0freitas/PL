import re
import sys

def md2html(text):
    lines = text.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # --- Títulos ---
        heading_match = re.match(r'^(#{1,6}) (.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            content = heading_match.group(2)
            result.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # --- Lista não ordenada ---
        if re.match(r'^- .+', line):
            result.append('<ul>')
            while i < len(lines) and re.match(r'^- .+', lines[i]):
                item = re.sub(r'^- ', '', lines[i])
                result.append(f' <li>{item}</li>')
                i += 1
            result.append('</ul>')
            continue

        # --- Lista ordenada ---
        if re.match(r'^\d+\. .+', line):
            result.append('<ol>')
            while i < len(lines) and re.match(r'^\d+\. .+', lines[i]):
                item = re.sub(r'^\d+\. ', '', lines[i])
                result.append(f' <li>{item}</li>')
                i += 1
            result.append('</ol>')
            continue

        result.append(line)
        i += 1

    html = '\n'.join(result)

    # --- Negrito: **texto** (antes do itálico) ---
    html = re.sub(
        r'(?<![a-zA-Z0-9])\*\*(?! )(.*?)(?<! )\*\*(?![a-zA-Z0-9])',
        r'<strong>\1</strong>',
        html
    )

    # --- Itálico: *texto* ---
    html = re.sub(
        r'(?<![a-zA-Z0-9])\*(?! )(.*?)(?<! )\*(?![a-zA-Z0-9])',
        r'<em>\1</em>',
        html
    )

    return html


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python md2html.py <ficheiro.md> [ficheiro_saida.html]")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    html_output = md2html(markdown_text)

    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"HTML guardado em: {output_file}")
    else:
        print(html_output)