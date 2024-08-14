import re  # Expressões Regulares


class Ipv4NetWorkCalculator():
    def __init__(self, ip='', prefixo='', mascara='', rede='', broadcast='', numero_ips=''):
        self.ip = ip
        self.prefixo = prefixo
        self.mascara = mascara
        self.rede = rede
        self.broadcast = broadcast
        self.numero_ips = numero_ips

        if self.ip == '':
            raise ValueError('IP não enviado!')

        if self.ip_tem_prefixo():
            pass

        if not self.is_ip():
            raise ValueError('IP inválido!')

        if not self.prefixo and not self.mascara:
            raise ValueError('Ou o prefixo ou a máscara devem ser enviados')

        if self.mascara:
            self.mascara_bin = ip_decimal_para_binario(ip=self.mascara)
            self.prefixo_da_mascara()
            print(mascara_bin)

    def prefixo_da_mascara(self):
        mascara_bin = self.mascara_bin.replace('.', '')
        conta = 0

        for bit in mascara_bin:

    def ip_decimal_para_binario(self, ip=''):
        if not ip:
            ip = self.ip

        bloco_ip = ip.split('.')
        ip_bin = []

        for bloco in bloco_ip:
            binario = bin(int(bloco))
            binario = binario[2:].zfill(8)
            ip_bin.append(binario)
            print(ip_bin)

        ip_bin = '.'.join(ip_bin)

    def ip_tem_prefixo(self):
        # 192.168.20.65/24
        # ^ - começa com
        # qualquer n° de 0 a 9, Que tenha entre 1 e 3 caracteres + um ponto (.)
        # $ Termina com isso
        ip_prefixo_regexp = re.compile(
            '^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

# Se n tem:
        if not ip_prefixo_regexp.search(self.ip):
            return  # Retorna. Não faz nd
# Se tem:
        divide_ip = self.ip.split('/')
        self.ip = divide_ip[0]  # É a 1° parte antes da barra
        self.prefixo = divide_ip[1]  # Parte dps da barra

    def is_ip(self):
        ip_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$')
        if ip_regexp.search(self.ip):
            return True
        return False


# Seta os atributos
if __name__ == '__main__':
    ipv4 = Ipv4NetWorkCalculator(ip='192.168.60.127', prefixo=24)
