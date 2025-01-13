import paramiko

def backup_fortigate_config(hostname, port, username, password, backup_command):
    """
    Faz o backup da configuração do FortiGate usando SSH.
    
    :param hostname: Endereço IP ou hostname do FortiGate.
    :param port: Porta SSH do FortiGate (normalmente 22 ou customizada).
    :param username: Nome de usuário para a conexão SSH.
    :param password: Senha para a conexão SSH.
    :param backup_command: Comando de backup a ser executado.
    """
    try:
        # Cria o cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)

        # Executa o comando de backup
        stdin, stdout, stderr = ssh.exec_command(backup_command)

        # Captura a saída e os erros do comando
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(f"Saída do comando:\n{output}")
        if error:
            print(f"Erro ao executar o comando:\n{error}")

        print("Backup realizado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar fazer o backup: {e}")

    finally:
        ssh.close()

if __name__ == "__main__":
    # Configurações do FortiGate
    fortigate_hostname = "192.168.255.254"  # Endereço IP do FortiGate
    fortigate_port = 22911                   # Porta SSH (alterar se necessário)
    fortigate_username = "xxx"  # Nome de usuário SSH
    fortigate_password = "xxx"        # Senha SSH

    # Comando de backup
    backup_command = "execute backup config sftp /NETWORK/Automation/MAI_FGT01_SYS.conf 192.168.11.27 joao.clemente Apstndp"

    # Realiza o backup
    backup_fortigate_config(fortigate_hostname, fortigate_port, fortigate_username, fortigate_password, backup_command)
