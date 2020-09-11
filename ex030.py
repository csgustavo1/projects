import PySimpleGUI as gg


class TelaPython:

    def __init__(self):
        layout = [

            [gg.Text('BUSCAR ARQUIVO')],
            [gg.Input()], [gg.FileBrowse()],
            [gg.Ok()], [gg.Cancel()],
            [gg.Text('INSIRA OS DADOS A SEREM ANALISADOS.')],
            [gg.Text('Nome', size=(5, 0)), gg.Input(size=(50, 0), key='nome')],
            [gg.Text('Idade', size=(5, 0)), gg.Input(size=(50, 0), key='idade')],
            [gg.Text('Sexo', size=(5, 0)), gg.Input(size=(50, 0), key='sexo')],
            [gg.Text('CPF', size=(5, 0)), gg.Input(size=(50, 10), key='cpf')],
            [gg.Text('Nascimento', size=(5, 0)), gg.Input(size=(50, 0), key='data')],
            [gg.Text('Qual o seu estado civil?')],
            [gg.Checkbox('Casado', key='casado'), gg.Checkbox('Solteiro', key='solteiro')],
            [gg.Text('Selecione a escolaridade:')],
            [gg.Combo(['Ensino medio completo',   'Graduando', 'Ensino medio incompleto', 'Sem escolaridade'])],
            [gg.Button('Enviar Dados', size=(20, 0))],
            [gg.Output(size=(50, 20))],
            [gg.CloseButton('Cancelar', size=(20, 0))]




        ]
        self.janela = gg.Window("Analisador de Dados", size=(1024, 768)).layout(layout)
        gg.popup('Olá seja bem vindo!', 'Desenvolvido por Gustavo Carvalho', 'Clique em OK para continuar!')



    def Iniciar(self):
        while True:
         self.button, self.values = self.janela.Read()
         nome = self.values['nome']
         idade = self.values['idade']
         sexo = self.values['sexo']
         cpf = self.values['cpf']
         data = self.values['data']
         aceita_casado = self.values['casado']
         aceita_solteiro = self.values['solteiro']
         print(f'nome: {nome}')
         print(f'idade: {idade}')
         print(f'sexo: {sexo}')
         print(f'cpf: {cpf}')
         print(f'Data de Nascimento: {data}')
         print(f'Casado: {aceita_casado}')
         print(f'Solteiro: {aceita_solteiro}')





tela = TelaPython()
tela.Iniciar()
