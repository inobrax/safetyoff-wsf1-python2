# SAFETYOFF V1.1 (versão para Linux Python)
Desenvolvido por **SOLNAX Soluções em Internet das Coisas**.

### Requisitos e Informações

Softwares previamente instalados:

**Python 2.X** (Qualquer versão do Python 2, geralmente já instalado junto ao sistema Linux)

Para melhor exemplificação, vamos utilizar um nome genérico para o usuário do sistema, chamaremos de NOME-DO-USUARIO, em todos os passos que contiverem este texto, substitua pelo nome do usuário da máquina que está utilizando.



### Download do SAFETYOFF V1

1. Para certificar que o Linux está o mais atualizado possivel, utilize o comando:
```
sudo apt-get update
sudo apt-get upgrade
```

2. Faça o download do arquivo através do repositório GitHub ou pelo comando:
```
wget https://github.com/inobrax/safetyoff-wsf1-python2/raw/main/safetyoff-wsfp-1.zip
```
3. Extraia os arquivos em uma pasta de sua escolha, recomendamos a pasta do usuário (**/home/NOME-DO-USUARIO**) 
```
unzip safetyoff-wsfp-1.zip
```

### Preparação para instalação

1. Abra o Terminal e navegue até a pasta extraída feito no passo anterior, dentro desta pasta deverão conter 3 arquivos, sendo um deles um arquivo com a extensão “.tar.gz”, para navegar até a paste utilize o comando:
```
cd safetyoff-wsfp-1
```

2. Para checar se está dentro da pasta execute:
```
ls
```
3. A resposta do Terminal deve ser similar a:
```
installer.sh  pyserial-3.5.zip  README.md  SafetyScript.py
```

### Instalação do Script

1. Após navegar até a pasta (Passo 1 da **Preparação para instalação**), execute o comando de instalação do Script (Comando root, necessário colocar a senha):
```
sudo sh install.sh
```

2. Responda o Terminal caso seja feita alguma pergunta sobre instalação utilizando a letra "Y”.

3. No fim da instalação, aparecerá um texto no Terminal parecido com:
```
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#

```
Role para a última linha e cole o próximo comando substituindo os caminhos quando necessário:
```
@reboot sudo python /home/NOME-DO-USUARIO/safetyoff-wsfp-1/SafetyScript.py > /home/NOME-DO-USUARIO/safetyoff-wsfp-1/log.txt
```
Aperte Ctrl + x, confirme com "Y" e aperte ENTER

4. Realize o SHUTDOWN ou o REBOOT de maneira manual, e confira se o processo está iniciando sozinho com o seguinte comando:
```
sudo crontab -l
```
A resposta deve ser parecida com (repare sempre as últimas linhas):
```
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

@reboot sudo python /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/SafetyScript.py > /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/log.txt
```

Outra maneira de confirmar, é entrar na pasta que foi extraída no início e verificar a existência de um novo arquivo chamado "log.txt"

### Desinstalação do processo do SAFETYOFF V1

1. Execute o comando:
```
sudo crontab -e
```
Apague a última linha, similar a: 
```
@reboot sudo python /home/NOME-DO-USUARIO/safetyoff-wsfp-1/SafetyScript.py > /home/NOME-DO-USUARIO/safetyoff-wsfp-1/log.txt
```
Aperte Ctrl + x, confirme com "Y" e aperte ENTER

2. Exclua a pasta (**safetyoff-wsfp-1**) e o arquivo zip (**safetyoff-wsfp-1**) manualmente ou através dos comandos:
```
sudo rm -r safetyoff-wsfp-1
sudo rm safetyoff-wsfp-1.zip
```



