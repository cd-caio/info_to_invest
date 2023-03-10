from datetime import date
import datetime


class TesouroDireto():
    pass


class TesouroPreFixado(TesouroDireto):

    def pega_data_hoje(self):
        return date.today()

    def meses_de_diferenca(
        self,
        data_atual: datetime.date,
        data_vencimento: datetime.date
    ):
        import pdb
        pdb.set_trace()

    def simular_investimento(
        self,
        data_vencimento: datetime.date,
        juros,
        aporte_unitario,
        aporte_mensal,
        data_resgate: datetime.date = None
    ):
        if data_resgate is None:
            data_resgate = data_vencimento

        data_atual = self.pega_data_hoje()
        self.meses_de_diferenca(data_atual, data_vencimento)

        #https://riconnect.rico.com.vc/blog/rentabilidade-do-tesouro-direto/#:~:text=Tesouro%20Prefixado,ser%C3%A1%20de%200%2C5%25.

tesouro_obj = TesouroPreFixado()

tesouro_obj.simular_investimento(
    datetime.date(day=1, month=1, year=2024),
    0.12,
    1000,
    1000,
    None
)
