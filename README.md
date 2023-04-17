# Espaço de Características
Nesta atividade realizamos a construção do espaço de características. Para isto, foram extraídas 15 características de um registro de EEG (canal Fp-Cz). Uma característica pode ser interpretada como uma medida quantitativa do nosso sinal biológico (ex: média de BPM em um exame físico) ou uma medida qualitativa do indivíduo (ex: fumante = 1, não fumante = 0). 
<br><br>
Neste registro temos 1179 trechos de 30 segundos cada, armazenados na variável SINAL e classificados previamente (labels) na variável estagios. As características extraídas foram, respectivamente: Média, Variância, Mobilidade, Complexidade Estatística, Freq Central do Espectro, Potência na Freq Central, Largura de Banda, Freq de Margem e Potências Espectrais Normalizadas nas Bandas delta 1 (0.5 a 2.5Hz), delta 2 (2.5 a 4 Hz), teta 1 (4 a 6Hz), teta 2 (6 8Hz), alfa (8 a 12 Hz), beta (12 a 20 Hz) e gama (20 a 45Hz).
<br><br>
Em um primeiro momento foi realizada a extração das características de cada trecho do sinal (onde cada um dos 1179 trechos resultaram em 15 características) e foi plotado o histograma das mesmas, com o intuito de realizar uma primeira inspeção visual das características isoladas.

<div>
  <div>
    <img src="https://user-images.githubusercontent.com/86500603/229982573-1217aef3-339d-41cc-bd06-887cabdf2c00.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982576-48d9250e-e034-448f-b971-5554381effc6.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982578-87dba60d-fa8c-485a-bec4-8536e7e74004.png" height = "200">
  </div>
  <div>
    <img src="https://user-images.githubusercontent.com/86500603/229982579-889deac4-b1ec-4244-b480-4f35966fff7c.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982580-4825aefd-e3cf-40f2-972c-a543236c94ad.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982583-312ea8f8-9f7e-4624-a8d0-7257d0b36c8d.png" height = "200">
  </div>
  <div>
    <img src="https://user-images.githubusercontent.com/86500603/229982587-3d8db0d7-e539-4648-8aaf-eae3d76e7935.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982589-9059cd5d-3399-4571-88d3-35509f4e462e.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982553-4b8e8264-abdd-4a06-aaf9-a5e9dafbdc4b.png" height = "200">
  </div>
  <div>
    <img src="https://user-images.githubusercontent.com/86500603/229982557-3dab200f-291f-4af1-bcb3-c5cff354cc44.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982560-4fcb636c-aa07-4fdf-a88a-f2b72407a62a.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982563-cdcfdb8c-a796-43fb-ae9c-a0be9f954aba.png" height = "200">
  </div>
  <div>
    <img src="https://user-images.githubusercontent.com/86500603/229982567-f08f34c6-51a0-4a42-938c-afbac9bf7fb4.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982568-ecb87d4f-76aa-49d0-afbd-80b8cc7135a1.png" height = "200">
    <img src="https://user-images.githubusercontent.com/86500603/229982571-61486563-1b19-4da9-9991-81cf6daead50.png" height = "200">
  </div>
</div>

<br>
Em um segundo momento foi realizada a construção do espaço de características em 2D, exibindo cada classe (etapa do sono) com cores distintas e selecionando as características de Complexidade Estatística e Mobilidade como eixos Y e X, respectivamente. Esta escolha arbitrária é um primeiro passo para visualizarmos a forma com que os padrões se distribuem dentro de um espaço de características, sendo a escolha das características muito importante para uma boa otimização na separação das classes.

<img src="https://user-images.githubusercontent.com/86500603/232620224-1156b41d-6f7b-47cb-a079-86e692e30478.png" width = "600">

<br>
Por fim, foi realizada a construção do espaço de características em 3D, exibindo apenas as classes de vigília, sono REM e sono não REM. As características escolhidas para este espaço foram Mobilidade, Freq Central e Potência Espectral Normalizadas nas Bandas delta 1. 

<img src="https://user-images.githubusercontent.com/86500603/232621399-29c1e623-18fc-4d6f-8a95-b81dd5b3f0e1.png" width = "600">

Com isso, demos mais um passo em direção a criação de classificadores. No caso de espaços em 2 dimensões, podemos separar as classes com retas e curvas. Já no caso de espaços em 3 dimensões, podemos separar as classes com planos e hiperplanos.
