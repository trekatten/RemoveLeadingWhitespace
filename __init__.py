from aqt import mw
from anki.hooks import addHook
import re

# Of course anki uses &nbsp instead of " " for spaces in the fields
regex = re.compile(r"(&nbsp;){1,}")

def onFocusLost(flag, n, fidx):
    fieldIndex = False
    # does the note have a 'meaning' field?
    for c, name in enumerate(mw.col.models.fieldNames(n.model())):
        if name.lower() == "meaning":
            src = name
            fieldIndex = c
    if not fieldIndex:
        return flag

    # is the event comming from the "meaning" field?
    if fidx != fieldIndex:
        return flag

    # grab the text and remove leading spaces
    n[src] = regex.sub("", n[src])
    return True

addHook('editFocusLost', onFocusLost)
