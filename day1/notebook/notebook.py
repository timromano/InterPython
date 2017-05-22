import datetime

#store the last available id for all new notes
last_id = 0


class Note:
    """Represent a note in a notebook. Matach against a string in searches and store tags for each note.
    """

    def __init__(self, memo, tags=''):
        """Initialize a note iwth memo and optional space-separated tags.
        Automaticalls set the note's creation date and an unique id. """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id


    def match(self, filter):
        """Determine if this note matches the filter text. Return true if it matches, false otherwise.
        Search is case sensitive and matches text and tags. 
        """
        return filter in self.memo or filter in self.tags

class Notebook:
    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with a given id and change its memo toa  given value."""
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        """Find a note with a given id and change its tags to the given value."""
        self._find_note(note_id).tags = tags

    def search(self, filter):
        """Find all notes that match a given filter string."""
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        """Locate a note with a given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None