from typing import List
from datetime import datetime
from dataclasses import dataclass, field


class Note:
    def __init__(self):
        pass

    title: str
    text: str
    creation_time: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        return f"Creation date: {self.creation_time}\n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
class Notebook:
    notes: List[Note] = field(default_factory=list)

    def add_note(self, title: str, text: str) -> str:
        new_note = Note(title=title, text=text)
        self.notes.append(new_note)
        return id(new_note)

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes if note.importance() in ['HIGH', 'MEDIUM']]

    def tags_note_count(self) -> dict:
        tags_count = {}
        for note in self.notes:
            for tag in note.tags:
                tags_count[tag] = tags_count.get(tag, 0) + 1
        return tags_count

notebook = Notebook()
notebook.add_note("Title 1", "Text 1")
notebook.add_note("Title 2", "Text 2")
notebook.add_note("Title 3", "Text 3")
notebook.notes[0].add_tag("tag1")
notebook.notes[0].add_tag("tag2")
notebook.notes[1].add_tag("tag2")
notebook.notes[1].add_tag("tag3")
notebook.notes[2].add_tag("tag1")

print(notebook.tags_note_count())


