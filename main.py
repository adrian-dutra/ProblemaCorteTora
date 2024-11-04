import time
def valorMax(n, tabelaPrecos):
    copia = tabelaPrecos.copy()  
    valorMax = [0] * (n + 1)
    for i in range(1, n + 1):
        vendaMax = 0
        for j in range(1, i + 1):
            vendaMax = max(vendaMax, copia[j] + valorMax[i - j])
        valorMax[i] = vendaMax
    return valorMax[n]

def greedy(n, tabelaPrecos):
    valor_total = 0
    while n > 0:
        melhor_densidade = 0
        melhor_comprimento = 0
        for i in range(1, n + 1):
            densidade = tabelaPrecos[i - 1] / i
            if densidade > melhor_densidade:
                melhor_densidade = densidade
                melhor_comprimento = i
        valor_total += tabelaPrecos[melhor_comprimento - 1]
        n -= melhor_comprimento
    return valor_total

def resultado_em_tabela(tamanhos, vDps, tDp, vGds, tGd):
    tabela = "{:<5} {:<8} {:<12} {:<8} {:<12} {:<8}\n".format("n", "vDP", "tDP", "vGreedy", "tGreedy", "%")
    tabela += "-" * 54 + "\n"
    for i in range(len(tamanhos)):
        percentual = (vGds[i] / vDps[i]) * 100
        linha = "{:<5} {:<8} {:<12.6f} {:<8} {:<12.6f} {:<.2f}\n".format(tamanhos[i], vDps[i], tDp[i], vGds[i], tGd[i], percentual)
        tabela += linha
    print(tabela)
    return tabela

inc = 10
fim = 110
stp = 1
tamanhos = []
vDps = []
vGds = []
tDp = []
tGd = []

for a in range(20):  
    tabelaPrecosDp = []
    tabelaPrecosGd = []
    for i in range(inc, fim + 1, stp):
        tabelaPrecosDp.append(i)
        tabelaPrecosGd.append(i)
    n = fim - inc
    inicio_dp = time.time()
    vDp = valorMax(n, tabelaPrecosDp)
    fim_dp = time.time()
    tDp.append(fim_dp - inicio_dp) 
    vDps.append(vDp)
    inicio_gd = time.time()
    vGd = greedy(n, tabelaPrecosGd)
    fim_gd = time.time()
    tGd.append(fim_gd - inicio_gd) 
    vGds.append(vGd)
    tamanhos.append(n)
    fim += 100

tabela = resultado_em_tabela(tamanhos, vDps, tDp, vGds, tGd)

with open("tabela.txt", "w") as arquivo:
    arquivo.write(tabela)
