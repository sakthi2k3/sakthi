import PySimpleGUI as sg
from webutils import get_html_content, parse_html_using_tag
from utils import get_statistics

layout = [
    [sg.Text("Web Page Analyzer", font=("Arial", 18))],
    [sg.Text("Enter URL", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), key='url'),
     sg.Button("Get Data", font=("Arial", 14), key='get')],
    [sg.Multiline("", font=("Arial", 14), size=(60, 15), key='output')]
]


def get_details(url):
    html_content = get_html_content(url)
    data = parse_html_using_tag(html_content, 'p')
    statistics = get_statistics(data)
    return (statistics)
    # ToDo - include a function display_data(statistics) to display the data in the GUI


if __name__ == '__main__':
    window = sg.Window("WebPageAnalyser", layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'get':
            s=get_details(values['url'])
            window['output'].print(s)
    window.Close()
