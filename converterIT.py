import sys
import json
import yaml
import xmltodict
from PyQt5 import QtWidgets, uic

def convert_data(input_file, output_file, input_format, output_format):
    with open(input_file, 'r') as file:
        content = file.read()

    if input_format == 'json':
        data = json.loads(content)
    elif input_format == 'xml':
        data = xmltodict.parse(content)
    elif input_format == 'yaml':
        data = yaml.safe_load(content)

    if output_format == 'json':
        output_data = json.dumps(data, indent=4)
    elif output_format == 'xml':
        output_data = xmltodict.unparse(data, pretty=True)
    elif output_format == 'yaml':
        output_data = yaml.dump(data, default_flow_style=False)

    with open(output_file, 'w') as file:
        file.write(output_data)

class ConverterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConverterApp, self).__init__()
        uic.loadUi('converter.ui', self)  # Ładuje UI z pliku .ui
        self.convertButton.clicked.connect(self.perform_conversion)
        self.statusLabel.setText("Gotowy do konwersji...")

    def perform_conversion(self):
        input_file = self.inputFile.text()
        output_file = self.outputFile.text()
        input_format = self.inputFormat.currentText().lower()
        output_format = self.outputFormat.currentText().lower()
        try:
            convert_data(input_file, output_file, input_format, output_format)
            self.statusLabel.setText(f'Konwersja {input_file} na {output_file} zakończona sukcesem!')
        except Exception as e:
            self.statusLabel.setText(f'Błąd: {str(e)}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())
