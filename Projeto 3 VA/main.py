ccTLD = ['.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.bm', '.bo', '.br', '.bs', '.bt', '.bv', '.bw', '.by', '.bz', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cu', '.cv', '.cx', '.cy', '.cz', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.ee', '.eg', '.er', '.es', '.et', '.eu', '.fi', '.fj', '.fk', '.fm', '.fo', '.fr', '.ga', '.gb', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gn', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.il', '.im', '.in', '.io', '.iq', '.ir', '.is', '.it', '.je', '.jm', '.jo', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz', '.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly', '.ma', '.mc', '.md', '.me', '.mg', '.mh', '.mk', '.ml', '.mm', '.mn', '.mo', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.mv', '.mw', '.mx', '.my', '.mz', '.nb', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu', '.nz', '.om', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pl', '.pm', '.pn', '.pr', '.ps', '.pt', '.pw', '.py', '.qa', '.re', '.ro', '.ru', '.rw', '.sa', '.sb', '.sc', '.scot', '.sd', '.se', '.sg', '.sh', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tr', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.wf', '.ws', '.ye', '.yt', '.yu', '.za', '.zm', '.zw']
gTLD = ['aero', 'arpa', 'biz', 'cam', 'com', 'coop', 'edu', 'gov', 'info', 'int', 'mil', 'museum', 'name', 'net', 'org', 'pro', 'tel']

def verificar_Dominio (entrada):
    entrada = entrada.lower().strip()
    a = []
    somente1 = 0

    for i in range(len(entrada)):            
        if entrada[i] == '@':
            a.append(True)
            somente1 += 1
        if somente1 >= 2:
            a.append(False)
        if entrada[i] == ' ':
            a.append(False)
    
    if False in a:
        return False
    else:
        if confirmacao_TLD(entrada):
            return True 
        else:
            return False

def confirmacao_TLD (entrada):    
    dominio = entrada[(entrada.find('@')+1):]
    if dominio.find('.') == -1 :
        return False
    else:
        email = dominio[:dominio.find('.')]
        dominio = dominio[(dominio.find('.')+1):]
        if dominio.find('.') == -1:
            if dominio in gTLD:
                return True
            else: 
                return False
        else:
            dominio1 = dominio[:dominio.find('.')]
            pais = dominio[dominio.find('.'):]
            resto = pais[(pais.find('.')+1):]
            if dominio1 in gTLD:
                if resto.find('.') != -1:
                    return False
                else:
                    if pais in ccTLD:
                        return True
                    else:
                        return False
            else:
                return False

while True:
    try:
        arquivo_Desejado = str(input("Digite o nome do arquivo: "))
        arquivo = open(arquivo_Desejado,'r')

        lista = []

        for linha in arquivo.readlines():
            
            conteudo = linha.split(',')
            conteudo[2] = conteudo[2].replace('\n','')
            
            if verificar_Dominio(conteudo[2]):
                conteudo.append(' Valido')
            else:
                conteudo.append(' Invalido')

            lista.append(conteudo)


        arquivo = open(arquivo_Desejado,'w')

        for linha in range(len(lista)):
            texto ='{}  ,  {}  ,  {}  ,  {}\n'.format(str(lista[linha][0]) , str(lista[linha][1]) , str(lista[linha][2]) , str(lista[linha][3]))
            arquivo.write(texto)

        arquivo.close()

        arquivo = open(arquivo_Desejado,'r')

        print('---\---\---\---\---\---\---\---\---\---\---\---\---\---\---\---\---')
        print('   NOME     \     Telefone  \     Email      \  Validade do email     ')

        for linha in arquivo:
            print(linha)

        break

    except BaseException as ex:
        print('Erro desconhecido. Erro: {}'.format(ex))
    except:
        print('---/---/---/---/---/---/---')
        print('  Arquivo não encontrado')
        print('---/---/---/---/---/---/---')
