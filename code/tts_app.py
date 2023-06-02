import tkinter as tk    # GUI component
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image   # Image component
import pytesseract      # Convert Image to Text Component
from subprocess import call     # To prevent window from closing when using TTS
import pyttsx3           # Text to Speech Component


def open_file():
    """Open a text file."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text to Speech App - {filepath}")

def open_image():
    """Open an image file and convert to text."""
    filepath = askopenfilename(
        filetypes=[("Image Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)

    im = Image.open(filepath)
    language = "eng"
    imgtext = pytesseract.image_to_string(im, lang=language)
    
    txt_edit.insert(tk.END, imgtext)
    window.title(f"Text to Speech App - {filepath}")

def save_file():
    """Save the current file as a new text file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text to Speech App - {filepath}")

def text_to_speech():
    """Text to Speech current text in editor"""
    voiceType = get_voice_select()
    voiceSpr = get_voice_spr()
    text = txt_edit.get("1.0", tk.END)
    call(["python3", "speak.py", text, str(voiceType), str(voiceSpr), '1'])    

def save_mp3():
    """Save TTS as a new mp3 file."""
    voiceType = get_voice_select()
    voiceSpr = get_voice_spr()
    text = txt_edit.get("1.0", tk.END)
    filepath = asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("Audio Files", "*.mp3"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    call(["python3", "speak.py", text, str(voiceType), str(voiceSpr), '0', filepath])
    window.title(f"Text to Speech App - {filepath}")

def get_voice_select():
    """Get different voice"""
    voiceSelect = voicescale.get()
    return voiceSelect

def get_voice_spr():
    """Get different voice speed rate"""
    voiceSpr = voicescalespr.get()
    return voiceSpr

engine = pyttsx3.init()
voices = engine.getProperty('voices')

window = tk.Tk()
window.title("Text to Speech App")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open Text File", command=open_file)
btn_imgtotext = tk.Button(frm_buttons, text="Open Image File", command=open_image)
btn_save = tk.Button(frm_buttons, text="Save as Text File", command=save_file)
btn_tts = tk.Button(frm_buttons, text="Text to Speech", command=text_to_speech)
btn_mp3 = tk.Button(frm_buttons, text="Save TTS as MP3", command=save_mp3)
label_voiceStr = tk.Label(frm_buttons, text="Voice Selection")
voicescale = tk.Scale(frm_buttons, orient='horizontal', from_=0, to=len(voices)-1)   # how many voices there are in speak.py
#voicescale = tk.Scale(frm_buttons, orient='horizontal', from_=0, to=5)  # comment out line above and uncomment this line to limit voice selection (make sure to do the same in speak.py)
label_voicespr = tk.Label(frm_buttons, text="Voice Speed")
voicescalespr = tk.Scale(frm_buttons, orient='horizontal', from_=-50, to=50)   # Speed rate of voice
voicescalespr.set(0)
label_emptyspace = tk.Label(frm_buttons, text="")
label_emptyspace2 = tk.Label(frm_buttons, text="")
label_emptyspace3 = tk.Label(frm_buttons, text="")


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_imgtotext.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
label_emptyspace.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
btn_tts.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_mp3.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
label_emptyspace2.grid(row=6, column=0, sticky="ew", padx=5, pady=15)
label_voiceStr.grid(row=7, column=0, sticky="ew", padx=5, pady=0)
voicescale.grid(row=8, column=0, sticky="ew", padx=5, pady=0)
label_emptyspace3.grid(row=9, column=0, sticky="ew", padx=5, pady=0)
label_voicespr.grid(row=10, column=0, sticky="ew", padx=5, pady=0)
voicescalespr.grid(row=11, column=0, sticky="ew", padx=5, pady=0)


frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
