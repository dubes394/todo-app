import FreeSimpleGUI as sg
from zip_creator import make_archive


label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress!!!")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1], 
                           [label2, input2, choose_button2], 
                          [compress_button],
                          [output_label]])

while True:
        event, value = window.read()
        print(event, value)
        filepaths = value["files"].split(";")
        folder = value["folder"]
        make_archive(filepaths, folder)
        window['output'].update(value="Compression Completed  ✅")
        
        if event == sg.WIN_CLOSED:
                break
        
window.close()