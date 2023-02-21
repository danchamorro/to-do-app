import PySimpleGUI as sg
import cli

label = sg.Text('Type in to do')
input_box = sg.InputText(tooltip='Type in to do')
add_button = sg.Button('Add', tooltip='Add to do')

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
