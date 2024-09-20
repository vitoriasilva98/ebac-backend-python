class Carro():
    def __init__(self, fabricante: str, modelo: str, ano_fabricacao: int):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def info(self) -> None:
        print(f'Fabricante: {self.fabricante},'
              f'\nModelo: {self.modelo},'
              f'\nAno de fabricação: {self.ano_fabricacao}')

    def motor(self, is_ligado: bool):
        if is_ligado:
            print("Motor ligado")
        else:
            print("Motor desligado")

    def __str__(self):
        return super().__str__()

