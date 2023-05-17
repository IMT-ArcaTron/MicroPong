# Pong em MicroPython

Este projeto consiste na criação de um jogo de Pong utilizando o MicroPython em uma placa de desenvolvimento com suporte a MicroPython e uma tela OLED. O jogo contará com botões para iniciar e reiniciar a partida, e dois potenciômetros que serão utilizados para controlar as paletas.
![image](https://github.com/AhmadKmahfoud/MicroPong/assets/82835417/e1a74199-1585-48f5-9bf5-7263e9f90bc3)

### 🚀 Esquema Eletrico
![image](https://github.com/AhmadKmahfoud/MicroPong/assets/82835417/c6cc07fa-4265-47e7-8c5a-74f701d13826)


### 🧱 Diagrama de blocos
![image](https://user-images.githubusercontent.com/82835417/235049069-e432b852-4df9-42a7-923d-1500570943a5.png)


### 📋 Pré-requisitos
- Ser compacto
- Placa de desenvolvimento com suporte a MicroPython;
- Display grafico (Tela OLED);
- utilizar entradas analogicas (2 potenciometros)
- Botões para start e reset.

## ⚙️ Executando os testes
Para testar o funcionamento do Raspberry Pi Pico, podemos começar com um teste simples de piscar o LED integrado. Para isso, execute o seguinte código no Raspberry Pi Pico:

**********************************************************************************************************************************************************************
![image](https://user-images.githubusercontent.com/82835417/235049382-6a7e1c97-7ff9-48c1-a9c9-099474b79bff.png)

**********************************************************************************************************************************************************************
Esse código fará com que o LED integrado pisque em um intervalo de 0,5 segundos.

### 🛠️Analisando os testes de ponta a ponta
Os testes de ponta a ponta podem ser executados ao jogar o jogo do Pong completo e verificar se todos os componentes (botões, potenciômetros, tela OLED) estão funcionando corretamente e se o jogo está sendo executado sem erros.


### 🔧 Instalação
Para instalar e executar corretamente o projeto de Pong em Micropython com Raspberry Pi Pico, é importante ter conhecimento sobre o esquema de pinos para conectar cada componente.

Tela OLED: a tela OLED deve ser conectada nas GPIOs 0 e 1 (ou seja, a placa deve estar configurada para I2C).

Botões de Start e Reset: os botões devem ser conectados nas GPIOs 16 e 17, respectivamente.

Potenciômetros: os potenciômetros devem ser conectados nas GPIOs 26 e 27.

Certifique-se de que todas as conexões estejam corretas antes de prosseguir com a instalação das bibliotecas e do código do projeto.

(Cabe ressaltar que o codigo possui comentarios que torna intuitivo a mudança das pinagens)

### 📦implantação
Para implantar o projeto em um sistema ativo, basta copiar todos os arquivos do projeto para o Raspberry Pi Pico.


### 🎮Video funcional


https://github.com/AhmadKmahfoud/MicroPong/assets/82835417/b3d12c3b-8503-437b-9c47-501fbb684a49



https://github.com/AhmadKmahfoud/MicroPong/assets/82835417/79712438-7010-4a3e-92bf-f296b0e5b02b




## 🛠️ Construído com
- MicroPython - a linguagem de programação usada
- Raspberry Pi Pico - o microcontrolador utilizado
- Bibliotecas do python:
    - uTime
    - Ssd1306
### 💸 Analise de custo
Lista de custos:
- 2 Potenciômetros: R$ 2,00 cada.
- 1 Raspberry Pi Pico: R$ 50,00 cada.  
- 1 Tela OLED I2C: R$ 35,00 cada.
- 2 PUSH button: R$ 3,00 10 unidades.
- 1 Placa padrão 5cm x 10cm: R$ 7,90 cada.
- 1 Suporte de pilhas 3x AA: R$ 5,50 cada.
- 2 Capas de potenciômetro: R$ 1,50 cada.
- 1 Caixa 3D: R$ 10,00 cada.
- Componentes adicionais com baixo custo. Ex: Solda, fios, cola quente. R$ 5,00.
- Estima-se que podemos vender cada unidade no valor de R$ 170,00 (Com uma margem de lucro de aproximadamente 25%)

## 📌 Versão

O projeto se encontra na Versão 1.0

## ✒️ Autores
- Caio Rabinovich 20.00255-6
- Felippe Onishi  20.00255-6
- Ahmad Mahfoud   20.01323-0
- Lucas Romanato  20.00313-7
![image](https://github.com/AhmadKmahfoud/MicroPong/assets/82835417/24e8a13e-b8ae-4654-ac77-243a514ce574)


## 🎁 Expressões de gratidão
Gostaríamos de agradecer aos nossos professores Sergio e Rodrigo pela orientação e suporte durante o desenvolvimento deste projeto.
