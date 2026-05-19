import pyperclip

def copy_text(text):

    try:

        pyperclip.copy(text)

    except:
        pass
