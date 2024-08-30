from datetime import datetime
import pytz


class ContaCorrente:


    @staticmethod
    def _data_hora():
        horario = datetime.now(pytz.timezone('Brazil/East'))
        return horario.strftime('%d/%m/%Y %H:%M')
    
    def __init__(self, name:str, cpf:str) -> None:
        self._name = name
        self._cpf = cpf
        self._saldo = 0
        self._agencia = None
        self._historico = []
        self.cartoes = []

    def mostrar_saldo(self):
        print(f'Seu saldo é R${self._saldo:,.2f}')

    def deposito(self, valor:float):
        self._saldo += valor
        self._historico.append((valor, 'Deposito', ContaCorrente._data_hora()))

    def _operacao_valida(self, valor):
            if valor > self._saldo:
                print('Não é possivel realizar essa operação')
                return False
            else: return True

    def saque(self, valor:float):
            valido = self._operacao_valida(valor)
            if valido:
                self._saldo -= valor
                self._historico.append((-valor, 'Saque', ContaCorrente._data_hora()))

    def pix(self, destinatario, valor:float):
        valido = self._operacao_valida(valor)
        if valido:
             self._saldo -= valor
             self._historico.append((-valor, 'Pix', ContaCorrente._data_hora()))
             destinatario._saldo += valor
             destinatario._historico.append((valor, 'Pix', ContaCorrente._data_hora()))
             print('Pix efetuado com sucesso')
        else: print('deu merda')

    def mostrar_historico(self):
        print('EXTRATO:')
        print('')
        print('Valor, Tipo de transação, Data e hora')
        for extrato in self._historico:
            print(extrato)
        print(f'Saldo final: R${self._saldo}')


class CartaoCredito:
     
     def __init__(self) -> None:
          pass


conta_1 = ContaCorrente('Thiago', '111.222.333-45')
conta_2 = ContaCorrente('Adalberto', '222.111.444-45')

conta_1.deposito(1000)
conta_1.mostrar_saldo()
conta_1.saque(100)
conta_1.pix(conta_2, 200)

# print('-'*20)
conta_1.mostrar_historico()
conta_2.mostrar_historico()