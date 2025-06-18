# AppRastreio - (nome indefinido)

## Objetivo

<p align="justify">
  O aplicativo tem como objetivo permitir que o usuário cadastre diversas chaves diferentes de rastreio, para, em um só lugar, saber a localização e status de seus pedidos de diferentes lojas virtuais, poupando tempo e evitando ansiedade. Assim que qualquer um pacote chega ao seu destino, uma notificação é disparada informando qual pacote foi entregue e o horário de chegada.
</p>
<p align="justify">
  O {nome do app} <em>não</em> tem como objetivo substituir a responsabilidade das lojas cujos códigos de rastreio são cadastrados, apenas permitir a visualização e facilitação do processo de espera. Portanto, quando um pedido for entregue, é imprescindível que o usuário busque a loja responsável — seja por aplicativo, seja por site — para seguir as instruções finais referentes ao pedido.
</p>

## Ferramentas utilizadas

### Front-End
<p align="justify">
  Para desenvolvimento do Front-End, por se tratar de uma aplicação multiplataforma — Android e IOS —, foi utilizado o framework <a href="https://reactnative.dev/">React Native</a>, em JavaScript. A partir do princípio "Learn once, write everywhere", a programação para ambas as plataformas por meio de um único código tornou-se possível, poupando tempo e recursos.
</p>
<p align="justify">
  Além do mais, a plataforma <a href="www.figma.com">Figma</a> foi utilizada para criação do protótipo da aplicação.
</p>

### Back-End
<p align="justify">
  Para desenvolvimento do Back-End, duas ferramentas utilizadas se destacam. O framework Python <a href="https://fastapi.tiangolo.com/">FastAPI</a> integrado a um banco <a href="https://www.mysql.com/">MySQL</a> para armazenamento de dados.
</p>
<p align="justify">
  O software <a href="https://www.brmodeloweb.com/lang/pt-br/index.html">brModelo</a> foi utilizado para diagramas referentes ao banco de dados (DERs e modelos físicos).
</p>

### Síntese

#### Linguagens de Programação

| Linguagens de Programação  |
| -------------------------- |
| Python (FastAPI)           |
| JavaScript (React Native)  |
| SQL (MySQL)                |

#### Extras

| Extras             |
| ------------------ |
| Visual Studio Code |
| MySQL Workbench    |
| brModelo           |
| Figma              |


## Fluxo de Desenvolvimento

- **1. Banco de Dados**
  - 1.1. Criação de diagramas relacionais e lógicos
  - 1.2. Implementação das tabelas em código SQL
  
- **2. API**
  - 2.1. Construção dos modelos de envio
  - 2.2. Codificação dos CRUDs para operação das tabelas via endpoints
  - 2.3. Conexão com APIs externas para o rastreio
  
- **3. Aplicativo Mobile**
  - 3.1. Desenvolvimento do protótipo Figma
  - 3.2. Implementação em código do protótipo

## Conclusão

<p align="justify">
  {nome do app} não possui um sistema de cadastro e login, portanto, não está em produção. Dessa forma, a única forma de rodar o projeto é localmente. Caso seja de seu interesse, <a href="">clique aqui</a> para ver as instruções de uso.
</p>
