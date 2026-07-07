"""Extract translatable string values (and source pairs where available) from locale files."""
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional


@dataclass
class Entry:
    location: str
    value: str
    source: Optional[str] = None  # for formats that carry a source string


def extract(path: Path) -> Iterator[Entry]:
    suffix = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".json":
        yield from _from_json(path, text)
    elif suffix == ".po":
        yield from _from_po(path, text)
    elif suffix in (".xliff", ".xlf"):
        yield from _from_xliff(path, text)
    elif suffix == ".ftl":
        yield from _from_fluent(path, text)
    else:
        return


def _from_json(path: Path, text: str) -> Iterator[Entry]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return
    for key, value in _walk(data):
        if isinstance(value, str):
            yield Entry(location=f"{path}:{key}", value=value)


def _walk(node, prefix=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _walk(v, f"{prefix}.{k}" if prefix else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _walk(v, f"{prefix}[{i}]")
    else:
        yield prefix, node


def _from_po(path: Path, text: str) -> Iterator[Entry]:
    # msgid / msgstr pairs; msgid is the source, msgstr the translation.
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        msgid = re.search(r'msgid\s+(.*)', block)
        msgstr = re.search(r'msgstr\s+(.*)', block)
        if not msgstr:
            continue
        source = _unquote(msgid.group(1)) if msgid else None
        translation = _unquote(msgstr.group(1))
        if translation == "":
            continue
        yield Entry(location=f"{path}:{source[:30]!r}", value=translation, source=source)


def _from_xliff(path: Path, text: str) -> Iterator[Entry]:
    for m in re.finditer(r"<target[^>]*>(.*?)</target>", text, re.DOTALL):
        value = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if value:
            yield Entry(location=str(path), value=value)


def _from_fluent(path: Path, text: str) -> Iterator[Entry]:
    for line in text.splitlines():
        m = re.match(r"^\s*\w[\w\-]*\s*=\s*(.*)$", line)
        if m:
            yield Entry(location=str(path), value=m.group(1).strip())


def _unquote(s: str) -> str:
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1].encode().decode("unicode_escape")
    return s
