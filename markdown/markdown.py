import re
from typing import Tuple, List


def parse(markdown: str) -> str:
    # We do things per line
    lines = markdown.splitlines()
    return group_list_items(parse_line(line) for line in lines)
    
def group_list_items(lines: List[str]) -> str:
    # Kudos to https://exercism.io/tracks/python/exercises/markdown/solutions/03d05c56ba7c45b698f25b4976de1832
    return re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", "".join(lines))
    
def parse_line(line: str) -> str:
    line = parse_heading(line)
    line = parse_list_item(line)
    line = parse_paragraph(line)
    line = parse_bold(line)
    line = parse_italics(line)
    return line
    
def parse_heading(markdown: str) -> str:
    def matching(match):
        hashes, text = match.groups()
        length = len(hashes)
        return f"<h{length}>{text}</h{length}>"
    return re.sub(r"^(#{1,6}) (.*)", matching, markdown)
    
def parse_bold(markdown: str) -> str:
    return re.sub(r'(.*)__(.*)__(.*)', r"\1<strong>\2</strong>\3", markdown)
    
def parse_italics(markdown: str) -> str:
    return re.sub(r'(.*)_(.*)_(.*)', r"\1<em>\2</em>\3", markdown)
    
def parse_list_item(markdown: str) -> Tuple[str, bool]:
    return re.sub(r'^\* (.*)', r"<li>\1</li>", markdown)
    
def parse_paragraph(markdown: str) -> str:
    matching = re.match('<h|<ul|<p|<li', markdown)
    if not matching:
        return f'<p>{markdown}</p>'
    return markdown
