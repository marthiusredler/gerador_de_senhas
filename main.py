from PySide6.QtGui import QIcon
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from interface.ui_main import Ui_MainWindow
from database import Data_base
from password import generatePassword as gpass
import pyperclip
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("KeyFortress - Gerenciador de Senhas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        
        #Toggle Menu Button
        self.btn_toggle.clicked.connect(self.LeftMenu)
        
        #SystemPages
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.btn_gerar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_gerar))
        self.btn_cadastrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cadastrar))

        #Cadastro de Senhas
        self.btn_cadastrarsenha.clicked.connect(self.Cadastro)
        
        #Gerar Senha
        self.pushButton_8.clicked.connect(self.GerarSenha)
        self.pushButton_7.clicked.connect(lambda: pyperclip.copy(self.label_resultado_gerar.text()))
        
        #Atualizaçao de estado da tabela
        self.Buscar()
        
        #Atualizar dados
        self.btn_alterar.clicked.connect(self.Update)
        
        #Apagar dados
        self.btn_excluir.clicked.connect(self.Delete)
        
    def LeftMenu(self):
        
        width = self.left_frame.width()
        if width == 0:
            newwidth = 200
        else:
            newwidth = 0
        
        self.animation = QtCore.QPropertyAnimation(self.left_frame, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    
    def GerarSenha(self):
        char = int(self.spinBox.text())
        havespecial = self.btn_radio.isChecked()
        self.label_resultado_gerar.setText(gpass(char, havespecial))
        
    def Cadastro(self):
        
        db = Data_base()
        db.connect()
        
        #Coletando Dados
        dados = (
            self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()
        )
        resp = db.resgistra_senha(dados)
        
        
        if resp == "ok":
            msg = QMessageBox()
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com Sucesso!")
            msg.exec()
            db.close_connection()
            self.Buscar()
            return
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("Erro ao Cadastrar, verifique se as informações estão corretas")
            msg.exec()
            db.close_connection()
            self.Buscar()
            return
            
    def Buscar(self):
        
        db = Data_base()
        db.connect()
        
        result = db.select_dados()
        
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()
    
    def Update(self):
        
        dados = []
        update_dados = []
        
        #Iterando Sobre lista
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())
            update_dados.append(dados)
            dados = []
            
        bd = Data_base()
        bd.connect()
        
        #Adicionando Novos Dados
        for item in update_dados:
            bd.update_dado(tuple(item))       
        
        #Alerta e Atualização
        msg = QMessageBox()
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()
        
        self.tableWidget.reset()
        self.Buscar()

        bd.close_connection()
    
    def Delete(self):
        db = Data_base()
        db.connect()
        
        #Alerta e Atualização
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Esse Registro será excluido")
        msg.setInformativeText("Você Tem Certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()
        
        if resp == QMessageBox.Yes:
            titulo = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_dado(titulo)
            self.Buscar()
        
            msg = QMessageBox()
            msg.setWindowTitle("Excluir")
            msg.setText(result)
            msg.exec()

        db.close_connection()
      
if __name__ == "__main__":
    
    #Ligando o Data Base
    db = Data_base()
    db.connect()
    db.create_table_keys()
    db.close_connection()
    
    #Criando a Interface
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    