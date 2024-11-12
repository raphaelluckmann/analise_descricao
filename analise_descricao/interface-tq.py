import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, 
    QFileDialog, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from analise_descricao import analise_produtos



class SelecaoBaseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selecione uma base")
        self.setGeometry(100, 100, 650, 300)
        
        # Layout e widgets
        layout = QVBoxLayout()

        # Seletor de arquivo
        self.label_file = QLabel("Selecione a base:")
        layout.addWidget(self.label_file)
        
        self.input_file = QLineEdit(self)
        layout.addWidget(self.input_file)
        
        self.browse_button = QPushButton("Buscar")
        self.browse_button.clicked.connect(self.selecionar_arquivo)
        layout.addWidget(self.browse_button)

        # Opções de precisão
        self.label_precision = QLabel("Escolha precisão")
        layout.addWidget(self.label_precision)
        
        self.radio_50 = QRadioButton("50%")
        self.radio_65 = QRadioButton("65%")
        self.radio_75 = QRadioButton("75%")
        layout.addWidget(self.radio_50)
        layout.addWidget(self.radio_65)
        layout.addWidget(self.radio_75)

        # Botões de ação
        self.analyze_button = QPushButton("Analisar")
        self.analyze_button.clicked.connect(self.analisar)
        layout.addWidget(self.analyze_button)
        
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)

        # Label final
        self.label_footer = QLabel("Raphael Luckmann - Tecnologia")
        layout.addWidget(self.label_footer, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def selecionar_arquivo(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo", "", "Todos os Arquivos (*)", options=options)
        if file_name:
            self.input_file.setText(file_name)

    def analisar(self):
        file_path = self.input_file.text()
        selected_value = None

        if self.radio_50.isChecked():
            selected_value = 0.50
        elif self.radio_65.isChecked():
            selected_value = 0.65
        elif self.radio_75.isChecked():
            selected_value = 0.75

        if file_path and selected_value:
            analise_produtos.analise_descricao(file_path, selected_value)
            QMessageBox.information(self, "Sucesso", "Análise concluída!")
        else:
            QMessageBox.warning(self, "Erro", "Você deve selecionar um arquivo e uma precisão!")


def main():
    app = QApplication(sys.argv)
    window = SelecaoBaseApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
