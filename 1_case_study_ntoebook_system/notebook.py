from datetime import datetime
from typing import List
# import datetime

class Note():
    """
    筆記本中的一項筆記，可用字串或是標籤搜尋。
    """
    note_id = 0
    def __init__(self, memo, tage=''):
        self.memo = memo
        self.creation_date = datetime.now()
        self.tage = tage
        Note.note_id += 1
        self.id = Note.note_id

    def match(self, search_filter: str) -> bool:
        """
        搜尋區分大小寫，並同時搜尋內容及標籤。
        """
        return (search_filter in self.memo) or (search_filter in self.tage)


class Notebook:
    """對Note做操作，可以修改會增加Note，做控制。"""
    def __init__(self):
        """Empty Note List."""
        self.notes: list(Note) = []

    def new_note(self, memo, tage=''):
        """Add new note."""
        self.notes.append(Note(memo, tage))

    def _find_note(self, note_id):
        """找出特定的note."""
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """修改memo."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
        else:
            print('This note_id is not exist.')
    
    def search(self, filter):
        return (note for note in self.notes if note.match(filter))


                
        

if __name__ == '__main__':
    n1 = Note('Yes1', 'test')
    n2 = Note('Go')
    print(n2.id)
    print(n2.creation_date)
    print(n2.__dict__)
