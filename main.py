import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.ChangeLookAndFeel('Reddit')
        #layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='Nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='Idade')],
            [sg.Text('Quais email serao aceitos?')],
            [sg.Checkbox('Gmail', key='Gmail'), sg.Checkbox('Outlook', key='Outlook'), sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Text('Aceita cartao')],
            [sg.Radio('Sim', 'Cartoes', key='aceitacartao'), sg.Radio('Nao','Cartoes', key='naoaceitacartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20) , key='slidervelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))],
    
        ]
        self.janela = sg.Window('Dados do Usuario').layout(layout)

        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao_sim = self.values['aceitacartao']
            aceita_cartao_nao = self.values['naoaceitacartao']
            velocidade_script = self.values['slidervelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail: {aceita_gmail}')
            print(f'Outlook: {aceita_outlook}')
            print(f'Yahoo: {aceita_yahoo}')
            print(f'Aceita cartao: {aceita_cartao_sim}')
            print(f'Nao aceita cartao: {aceita_cartao_nao}')
            print(f'Velocidade Script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()