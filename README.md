# SAFETYOFF V1.1 (versão para Linux Python)
Desenvolvido por **SOLNAX Soluções em Internet das Coisas**.

### Requisitos e Informações

Softwares previamente instalados:

Python 2.X (Qualquer versão do Python 2, geralmente já instalado junto ao sistema Linux)

Para melhor exemplificação, vamos utilizar um nome genérico para o usuario do sistema, chamaremos de NOME-DO-USUARIO, em todos os passos que aparecerem esse texto, substituia pelo nome do usuario da maquina que está utilizando.



### Download do SAFETYOFF V1

1. Faça o download do arquivo atraves do repositorio GitHub ou pelo comando:
```
wget -c https://github.com/inobrax/nsi-safetyoff-job-v1.git
```
2. Extraia os arquivos em um pasta de sua escolha, recomendamos a pasta do usuario (/home/NOME-DO-USUARIO) 

### Preparação para instalação

1. Abra o Terminal e navegue até a pasta extraida feito no passo anterior, dentro desta pasta deverão conter 2 arquivos e uma pasta, para navegar até a paste utilize o comando:
```
cd /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main
```

2. Para checar se está dentro da pasta execute:
```
ls
```
3. A resposta do Terminal deve ser similar a:
```
Installer.sh  pyserial-3.5  SafetyScript.py
```

### Instalação do Script

1. Ainda no Terminal, execução o comando de instalação do Script (Comando root, necessario colocar a senha):
```
sudo sh install.sh
```

2. Responda o Terminal caso seja feita alguma pergunta sobre instalação utilizando a letra "Y" .

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
Role para a ultima linha e cole o proximo comando substituindo os caminhos quando necessário:
```
@reboot sudo python /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/SafetyScript.py > /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/log.txt
```
Aperte Ctrl + x, confirme com "Y" e aperte ENTER

4. Realize o SHUTDOWN ou o REBOOT de maneira manual , e confira se o processo está iniciando sozinho com o seguinte comando:
```
sudo crontab -l
```
A resposta deve ser parecida com (repare sempre as ultimas linhas):
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

Outra maneira de confirmar, é entrar na pasta que foi extraida no inicio e verificar a existencia de um novo arquivo chamado "log.txt"

### Desinstalação do processo do SAFETYOFF V1

1. Execute o comando:
```
sudo crontab -e
```
apague a ultima linha, similar a: 
```
@reboot sudo python /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/SafetyScript.py > /home/NOME-DO-USUARIO/nsi-safetyoff-job-v1-main/log.txt
```
Aperte Ctrl + x , confirme com "Y" e aperte ENTER

2. Exclua a pasta "nsi-safetyoff-job-v1-main" manualmente ou através do comando:
```
cd /home/NOME-DO-USUARIO
sudo rm -r nsi-safetyoff-job-v1-main
```


