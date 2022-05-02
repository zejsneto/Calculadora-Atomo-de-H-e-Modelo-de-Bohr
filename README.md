# Calculadora-Atomo-de-H-e-Modelo-de-Bohr

## Projeto NL2 de Tópicos de Óptica e Física Moderna.
<br>2022.1

Escreva um programa em linguagem Python relacionado com o átomo de hidrogênio e o modelo de Bohr. O programa terá vários cálculos, portanto o time deverá incluir um menu de opções para que o usuário possa escolher a ferramenta que ele necessite (por ex., conversão de energia de elétron-volt para joule, cálculo dos níveis quânticos do átomo de H, etc). 

O programa deve ser compartilhado entre os membros do time: não será aceita nenhuma desculpa sobre o acesso ao programa, caso um dos integrantes falte à aula. Cada projeto deve ser desenvolvido pelo próprio time: programas com plágio parcial ou integral não serão considerados para a avaliação.

## Instruções gerais: 

• Saídas com valores numéricos em notação científica para números muito grandes ou muito pequenos; devem ter 3 algarismos significativos. Isso não se aplica para o número quântico, que deve ser um número inteiro.

• Parâmetros físicos devem ser mostrados com unidades, tanto na entrada quanto na saída. 

• Tenha empatia pelo usuário: exponha menus bem organizados e saídas que sejam atualizadas para cada nova entrada ou que sejam facilmente identificadas após vários cálculos

• Tenha empatia pelo usuário: após a finalização de um cálculo, exiba o menu de opções novamente para outros estudos. (Para que o usuário não precise compilar o programa cada vez que quiser fazer um cálculo).

## Funções mínimas do programa:

Usar as constantes com 4 algarismos significativos no programa: constante
de Planck, carga elementar, massa do elétron, constante de Rydberg, etc.
1) Para um dado valor de n, calcular
  <br>a. o raio da órbita do elétron,
  <br>b. velocidade do elétron na órbita,
  <br>c. comprimento de onda de De Broglie do elétron no nível n,
  <br>d. a energia cinética no nível n,
  <br>e. energia potencial no nível n,
  <br>f. energia total no nível n.
  
Atenção aos sinais das energias e n deve ser um número inteiro. Retornar uma mensagem de erro, caso o usuário digite um número não inteiro. Algumas energias podem ser negativas, por ex., no caso de energia de ligação.

2) Calcular a energia, o comprimento de onda e frequência do fóton emitido/absorvido pelo átomo de hidrogênio na transição de um nível inicial ni para outro nível nf, ou seja, ao fazer um “salto quântico”. Como ni pode ser maior ou menor que nf, deve-se tomar cuidado para não retornar valores negativos. 

3) Calcular o nível n final (nf) após o átomo de hidrogênio no nível inicial (ni) absorver um fóton com um determinado comprimento de onda ou frequência digitado pelo usuário. Note que: i) o átomo de hidrogênio irá absorver apenas fótons com energias específicas; ii) o valor de n deve ser inteiro, portanto, seria interessante mostrar o nf calculado com duas casas decimais e o arredondado para um número inteiro.

4) Calcular o nível n inicial (ni) do elétron no átomo de hidrogênio a partir do qual ocorre o decaimento para o nível (nf) com a emissão de um fóton com um determinado comprimento de onda ou frequência digitado pelo usuário. Como o valor de n deve ser um inteiro, seria interessante mostrar o ni calculado, com duas casas decimais, e o arredondado para um número inteiro.

## Checklist das funções do programa:

1. Entrada do número quântico (n) do átomo de hidrogênio. Calcular:
  <br>a. rn
  <br>b. vn
  <br>c. n
  <br>d. Kn
  <br>e. Un
  <br>f. En
  
2. Entrada do estado ni inicial e estado final nf do elétron no átomo de H. Dependendo se o processo é de decaimento ou excitação, ni pode ser maior ou menor que nf, portanto, cuidado para não retornar valores negativos). Calcular:
  <br>a. E do fóton absorvido ou emitido
  <br>b.  do fóton absorvido ou emitido
  <br>c. f do fóton absorvido ou emitido
  
3. 
    i) Entrada do nível ni inicial do elétron no átomo de H e frequência do fóton absorvido.
    <br>ii) Entrado de ni inicial do elétron no átomo de H e  do fóton absorvido.

Calcular:
  a. Nível n após a absorção do fóton (mostrar valor calculado com duas casas decimais e arredondado de n)

4. 
    i) Entrada da frequência do fóton emitido na transição para o nível
final nf digitado pelo usuário.
    <br>iii) Entrada de  do fóton emitido na transição para o nível final nf digitado pelo usuário.
  
  Calcular:
    b. Nível n antes da emissão do fóton (mostrar valor calculado com duas casas decimais e arredondado de n)
  
  Não é obrigatório que os cálculos estejam organizados na forma mostrada acima. Foi organizado desta forma para servir de checklist. Por funções mínimas: significa que a equipe pode implementar outros recursos que facilitem responder o questionário na parte b da atividade.

  
