import osa
import math


def read_file(file_name='currencies.txt'):
    with open(file_name) as f:
        return [line.strip('\n').split(' ') for line in f]


def main():
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    costs_list = read_file()
    total_costs = 0

    for cost in costs_list:
        res = client.service.ConvertToNum(None, cost[2], 'RUB', float(cost[1]), True)
        total_costs += res
        # print('{} -> RUB, {} -> {}'.format(cost[2], cost[1], res))

    print('Всего расходов на поездку {}'.format(math.ceil(total_costs)))


if __name__ == '__main__':
    main()



