# pip install azure-cognitiveservices-speech
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "YOUR KEY HERE"
SPEECH_REGION = "YOUR REGION HERE"

NOTES_FILE = "notes.txt"
REPORT_FILE = "report.txt"

def gather_lines():
    print("Enter up to 5 lines (blank line to stop):")
    lines = []
    while len(lines) < 5:   # 0,1,2,3,4
        try:
            text = input(f"Line {len(lines) + 1}: ").strip()
            if text == "":
                break
            if all(ch for ch in text) and not any(c.isalnum() for c in text):
                raise ValueError("Line cannot be only symbols. ")
            lines.append(text)
        except ValueError as e:
            print(f"Invalid input: {e} Try again")
    return lines

def save_notes(lines, filename=NOTES_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def build_report(infile=NOTES_FILE, outfile=REPORT_FILE):
    total_lines = 0
    total_words = 0
    longest = ""
    try:
        with open(infile, "r", encoding="utf-8") as f:
            for line in f:
                s = line.rstrip("\n")
                total_lines +=1
                words = s.split()
                total_words += len(words)
                if len(s) > len(longest):
                    longest = s
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing input file:n{infile}") from e

    summary = (
        f"SUMMARY REPORT\n"
        f"Lines: {total_lines}\n"
        f"Words: {total_words}\n"
        f"Longest line length: {len(longest)}\n"
        f"Longest line: {longest if longest else '(none)'}\n"
    )
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(summary)
    return summary

def speak_text(text: str):
    speech_key = SPEECH_KEY
    speech_region = SPEECH_REGION


    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)


    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text).get()








