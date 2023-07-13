class TV:
    def __init__(self, tamanho: int):
        self.__tamanho = tamanho
        self.__volume = 50
        self.__canal = 1
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 1:
            self.__volume -= 1

    def modificar_canal(self, canal: int):
        if self.__canal < 1 and self.__canal > 99:
            raise ValueError("Canal deve ser entre 1 e 99")
        self.__canal = canal

    def ligar_desligar(self):
        self.__ligada = not self.__ligada

    def get_canal(self) -> int:
        return self.__canal

    def get_volume(self) -> int:
        return self.__volume
