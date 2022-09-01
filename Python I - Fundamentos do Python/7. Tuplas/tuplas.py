# Tupla, é uma estrutura parecida com listas, mas com a característica de ser imutável.
# Isso significa que quando uma tupla é criada, não há a possibilidade (entre aspas)* de adicionar, remover, ou alterar seus elementos.
# Geralmente são utilizadas para adicionar tipos diferentes de informações, podemos utilizar uma tupla para adicionar, por exemplo, a sigla do estado em uma posição e o nome em outra, tornando-a boa para ser usada quando queremos trabalhar com informações diferentes em uma mesma variável.

# Sua característica de imutabilidade oferece segurança nas informações armazenadas, sendo assim, uma tupla vai ser usada para armazenar uma sequência de dados que não serão modificados no decorrer do código.
# Entretanto, *ela não é totalmente imutável, pois quando armazena outro objeto como uma lista, os dados armazenados nesse elemento podem ser modificados.
# Ah, mas é preciso entender que esse tipo de alteração não é feita na estrutura da tupla, apenas no conteúdo desse objeto, que é passado como referência.

tupla = (('MG', 'Minas Gerais'), ('SP', 'São Paulo'), [0,1,2,3])

print(f'Remove o ultimo elemento da lista da tupla e retorna: {tupla[2].pop()}')

print(f'Resultado da tupla com o objeto lista modificado: {tupla}')