# convert pdf to Audio
import PyPDF2, pyttsx3

# path o pdf file
path = open("files/readMe.pdf", "rb")

# read pdf file
pdfReader = PyPDF2.PdfReader(path)

# create and initialise speaker object
speaker = pyttsx3.init()

num_pages = pdfReader.numPages
title_text = "page "

if __name__ == '__main__':
    for page in range(num_pages):
        # extract text pag by page
        page_text = pdfReader.getPage(page).extractText()
        print(page_text)

        # convert page text to audio
        speaker.say(title_text + str(page+1))
        speaker.runAndWait()
        speaker.say(page_text)
        speaker.runAndWait()

    speaker.stop()


