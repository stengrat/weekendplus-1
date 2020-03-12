# weekendplus

## Requerimentos.
* VirtualEnv
* Python 3 +
* Django 2.2.11


## Instalação
<details><summary>1. VirtualEnv</summary>
1. Em seu cmd ou Terminal do VisualCode digite o seguinte comando
** pip3 install virtualenv    
</details>
<details><summary>2. Clone nosso Projeto</summary>
1. git clone https://github.com/RicardoTaverna/weekendplus.git   
</details>

<details><summary>3. Crie uma VirtualEnv</summary>
* 1. Em seu terminal digite: virtualenv Django <br/>
* 2. Em seguida:   .\Django\Scripts\activate
</details>
<details><summary>4. Instalar dependencias Django</summary>
1. *Em seu terminal digite: cd weekendplus <br/>
2. *Em seguida:   pip install -r requirements.txt  
</details>
<details><summary>5. Finalizando</summary>
* 1. Dentro da pasta weekendplus digitepython manage.py migrate  <br/>
*2. Depois: python manage.py runserver <br/>
*3. Acesse http://127.0.0.1:8000/
</details>

## Erro
*  Caso ocorra um erro de segurança ao tentar ativar a virtual env abra o powershell em modo adiministrador e digite o seguinte comando: <br/>
 * Set-ExecutionPolicy RemoteSigned


