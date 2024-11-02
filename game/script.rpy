define bgm = "audio/musicas/jogo.mp3"
default estrelas = 3

define yuri = Character("Yuri")
define leo = Character("Léo")
define ana = Character("Ana")
define pedro = Character("Pedro")
define bia = Character("Bia")
define miguel = Character("Miguel")
define aisha = Character("Aisha")
define mariana = Character("Mariana")
define pablo = Character("Pablo")
define prof = Character("Professora")
define narradora = Character("Narração")

###### Imagens de pontuação #######
image final_3_estrelas = im.Scale("imagens/pontuacoes/tres.png", 1920, 1180)
image final_2_estrelas = im.Scale("imagens/pontuacoes/duas.png", 1920, 1180)
image final_1_estrelas = im.Scale("imagens/pontuacoes/uma.png", 1920, 1180)
image final_0_estrelas = im.Scale("imagens/pontuacoes/zero.png", 1920, 1180)

image creditos = "creditos.png"

####### Imagens de fundo ########
image fachada = im.Scale("imagens/cenarios/fachada.png", 1920, 1180)
image porta = im.Scale("imagens/cenarios/porta.png", 1920, 1180)
image canto = im.Scale("imagens/cenarios/canto.png", 1920, 1180)
image sala = im.Scale("imagens/cenarios/sala.png", 1920, 1180)
image parede = im.Scale("imagens/cenarios/parede.png", 1920, 1180)
image patio = im.Scale("imagens/cenarios/patio.png", 1920, 1180)

####### Imagens de personagens com tamanhos ajustados #######

#yuri
image yuri normal = im.Scale("imagens/personagens/yuri/yurinormal.png", 800, 920)
image yuri feliz = im.Scale("imagens/personagens/yuri/yurifeliz.png", 800, 920)
image yuri triste = im.Scale("imagens/personagens/yuri/yuritriste.png", 800, 920)
image yuri surpreso = im.Scale("imagens/personagens/yuri/yurisurpreso.png", 800, 920)
image yuri bravo = im.Scale("imagens/personagens/yuri/yuribravo.png", 800, 920)

#leo
image leo normal = im.Scale("imagens/personagens/leo/leonormal.png", 800, 920)
image leo feliz = im.Scale("imagens/personagens/leo/leofeliz.png", 800, 920)
image leo triste = im.Scale("imagens/personagens/leo/leotriste.png", 800, 920)
image leo surpreso = im.Scale("imagens/personagens/leo/leosurpreso.png", 800, 920)
image leo bravo = im.Scale("imagens/personagens/leo/leobravo.png", 800, 920)

#ana
image ana normal = im.Scale("imagens/personagens/ana/ananormal.png", 800, 920)
image ana feliz = im.Scale("imagens/personagens/ana/anafeliz.png", 800, 920)
image ana triste = im.Scale("imagens/personagens/ana/anatriste.png", 800, 920)
image ana surpresa = im.Scale("imagens/personagens/ana/anasurpresa.png", 800, 920)
image ana brava = im.Scale("imagens/personagens/ana/anabrava.png", 800, 920)

#prof
image prof normal = im.Scale("imagens/personagens/prof/profnormal.png", 800, 920)
image prof feliz = im.Scale("imagens/personagens/prof/proffeliz.png", 800, 920)
image prof brava = im.Scale("imagens/personagens/prof/profbrava.png", 800, 920)

#bia
image bia normal = im.Scale("imagens/personagens/bia/bianormal.png", 800, 920)
image bia feliz = im.Scale("imagens/personagens/bia/biafeliz.png", 800, 920)
image bia triste = im.Scale("imagens/personagens/bia/biatriste.png", 800, 920)
image bia surpresa = im.Scale("imagens/personagens/bia/biasurpresa.png", 800, 920)
image bia brava = im.Scale("imagens/personagens/bia/biabrava.png", 800, 920)

#pedro
image pedro normal = im.Scale("imagens/personagens/pedro/pedronormal1.png", 800, 920)
image pedro feliz = im.Scale("imagens/personagens/pedro/pedrofeliz1.png", 800, 920)
image pedro triste = im.Scale("imagens/personagens/pedro/pedrotriste1.png", 800, 920)
image pedro surpreso = im.Scale("imagens/personagens/pedro/pedrosurpreso1.png", 800, 920)
image pedro bravo = im.Scale("imagens/personagens/pedro/pedrobravo1.png", 800, 920)

#aisha
image aisha normal = im.Scale("imagens/personagens/aisha/aishanormal.png", 800, 920)
image aisha feliz = im.Scale("imagens/personagens/aisha/aishafeliz.png", 800, 920)
image aisha triste = im.Scale("imagens/personagens/aisha/aishatriste.png", 800, 920)
image aisha surpresa = im.Scale("imagens/personagens/aisha/aishasurpresa.png", 800, 920)
image aisha brava = im.Scale("imagens/personagens/aisha/aishabrava.png", 800, 920)

#mariana
image mariana normal = im.Scale("imagens/personagens/mariana/mariananormal.png", 800, 920)
image mariana feliz = im.Scale("imagens/personagens/mariana/marianafeliz.png", 800, 920)
image mariana triste = im.Scale("imagens/personagens/mariana/marianatriste.png", 800, 920)
image mariana surpresa  = im.Scale("imagens/personagens/mariana/marianasurpresa.png", 800, 920)
image mariana brava = im.Scale("imagens/personagens/mariana/marianabrava.png", 800, 920)

#pablo
image pablo normal = im.Scale("imagens/personagens/pablo/pablonormal.png", 800, 920)
image pablo feliz = im.Scale("imagens/personagens/pablo/pablofeliz.png", 800, 920)
image pablo triste = im.Scale("imagens/personagens/pablo/pablotriste.png", 800, 920)
image pablo surpreso = im.Scale("imagens/personagens/pablo/pablosurpreso.png", 800, 920)
image pablo bravo = im.Scale("imagens/personagens/pablo/pablobravo.png", 800, 920)

#miguel
image miguel normal = im.Scale("imagens/personagens/miguel/miguelnormal.png", 800, 920)
image miguel feliz = im.Scale("imagens/personagens/miguel/miguelfeliz.png", 800, 920)
image miguel triste = im.Scale("imagens/personagens/miguel/migueltriste.png", 800, 920)
image miguel surpreso = im.Scale("imagens/personagens/miguel/miguelsurpreso.png", 800, 920)
image miguel bravo = im.Scale("imagens/personagens/miguel/miguelbravo.png", 800, 920)

label start:
    scene fachada with fade
    play music bgm loop

    show yuri feliz
    voice "audio/vozes/yuri/yuri1.mp3"
    yuri "Olá! / (Para passar o diálogo clique na tela!)" 

    voice "audio/vozes/yuri/yuri2.mp3"
    yuri "Eu sou o Yuri! Eu estudo na Escola de Ensino Fundamental Ruth Rocha. Hoje, vou aprender algo muito importante sobre como resolver conflitos de um jeito gentil e respeitoso. Vamos nessa? / (Para selecionar a opção a seguir clique nela!)"
    
    play sound "audio/efeitos/menu1.mp3"
    menu:
        "Começar!":
            jump entrada

label entrada:

    scene porta
    show yuri feliz
    voice "audio/vozes/yuri/yuri3.mp3"
    yuri "Estou animado para o dia de hoje! Vamos ver o que vai acontecer!"

    voice "audio/vozes/yuri/yuri4.mp3"
    yuri "Ei, olha lá! Parece que já estão entrando na sala. Vamos entrar também! A professora deve chegar logo..."

    scene sala
    hide yuri feliz
    show yuri normal
    voice "audio/vozes/yuri/yuri5.mp3"
    yuri "Humm... Não parece ter muita gente aqui dentro."
    voice "audio/vozes/yuri/yuri6.mp3"
    yuri "Espera! Acho que tem algo acontecendo ali no fundo..."
    voice "audio/vozes/yuri/yuri7.mp3"
    yuri "Parece que o Léo e a Ana estão brigando!"

    scene canto
    hide yuri normal
    show leo bravo at right
    show ana brava at left
    voice "audio/vozes/leo/leo1.mp3"
    leo "Você está copiando muito devagar, Ana!"
    voice "audio/vozes/ana/ana1.mp3"
    ana "Pode parar de me apressar? Você é muito chato!"
    voice "audio/vozes/leo/leo2.mp3"
    leo "Eu preciso do meu caderno! Você é muito lerda!"

    hide ana brava
    hide leo bravo
    show yuri triste at center
    voice "audio/vozes/yuri/yuri8.mp3"
    yuri "O que será que devo fazer?"


play sound "audio/efeitos/menu2.mp3" loop
menu:
    "Oi, Léo, por que você e a Ana estão brigando? Podemos resolver isso!":
        play sound "audio/efeitos/certo.mp3"
        jump leo_ana1
    "Pare de gritar, Léo! Não seja mal educado.":
        play sound "audio/efeitos/errado.mp3"
        $ estrelas -= 1
        jump leo_ana2
    "Ana, você está bem? Léo, vamos conversar sobre isso.":
        play sound "audio/efeitos/certo.mp3"
        jump leo_ana3


label leo_ana1:
    show yuri triste
    voice "audio/vozes/yuri/yuri9.mp3"
    yuri "Oi, Léo, por que você e a Ana estão brigando? Podemos resolver isso!"
    voice "audio/vozes/yuri/yuri10.mp3"
    yuri "Falando desse jeito vocês nunca vão se entender. Sejam gentis um com o outro e tentem conversar."

    hide yuri triste
    show ana triste
    voice "audio/vozes/ana/ana2.mp3"
    ana "...eu não devia ter te chamado de chato, Léo. Me desculpe..."
    hide ana triste
    show leo triste
    voice "audio/vozes/leo/leo3.mp3"
    leo "Eu também não queria ter te xingado...Desculpa."

    hide leo triste
    show yuri normal
    voice "audio/vozes/yuri/yuri11.mp3"
    yuri "Léo, você precisa desse caderno agora?"

    show leo surpreso at right
    voice "audio/vozes/leo/leo4.mp3"
    leo "Sim."

    hide yuri normal
    show yuri surpreso
    voice "audio/vozes/yuri/yuri12.mp3"
    yuri "Hmmm..." 

    hide yuri surpreso
    show ana surpresa at left
    voice "audio/vozes/ana/ana3-10.mp3"
    ana "Já sei!"
    hide ana surpresa
    show ana normal
    voice "audio/vozes/ana/ana4-11.mp3"
    ana "Léo, quando você chegar em casa você pode me mandar uma foto do seu caderno? Assim eu posso copiar a máteria que perdi depois da aula e você pode usar seu caderno agora!"

    hide leo surpreso
    show leo normal at right
    voice "audio/vozes/leo/leo5.mp3"
    leo "...pode ser!"
    hide leo normal
    show leo feliz at right
    voice "audio/vozes/leo/leo6.mp3"
    leo "Parece uma boa ideia!"

    hide leo feliz
    hide ana normal
    show yuri normal
    voice "audio/vozes/yuri/yuri13.mp3"
    yuri "Viram só? Quando vocês não gritam um com o outro é muito mais fácil resolver as coisas!"

    hide yuri normal
    show ana feliz
    voice "audio/vozes/ana/ana5.mp3"
    ana "Obrigada por nos ajudar, Yuri!"

    hide ana feliz
    show yuri feliz
    voice "audio/vozes/yuri/yuri14.mp3"
    yuri "De nada!"

    hide yuri feliz
    voice "audio/vozes/narradora/narradora1.mp3"
    narradora "(Usando de uma comunicação não violenta, Yuri conseguiu ajudar Léo e Ana a se resolverem. Parabéns!)"
    jump intervalo

label leo_ana2:
    hide yuri triste
    show yuri bravo
    voice "audio/vozes/yuri/yuri15.mp3"
    yuri "Pare de gritar, Léo! Não seja mal educado."

    hide yuri bravo
    show leo bravo 
    voice "audio/vozes/leo/leo7.mp3"
    leo "Mas foi ela quem começou! Sempre sou eu o culpado de tudo."
    hide leo bravo
    show ana brava
    voice "audio/vozes/ana/ana6.mp3"
    ana "Talvez seja porque você realmente sempre é o culpado!"

    hide ana brava
    show yuri bravo
    voice "audio/vozes/yuri/yuri16.mp3"
    yuri "Ana você é grossa igual ele! Vocês estão sempre brigando!"

    hide yuri bravo
    show prof brava
    voice "audio/vozes/narradora/narradora2.mp3"
    narradora "(A professora acaba de entrar na sala e percebe a briga)"
    voice "audio/vozes/prof/prof1.mp3"
    prof "Posso saber o motivo dos três estarem brigando aqui atrás?"

    hide prof brava
    show leo bravo at right
    show ana brava at left
    show yuri bravo at center
    voice "audio/vozes/narradora/narradora3.mp3"
    narradora "(Os alunos tentam explicar o que aconteceu mas apenas continuam gritando.)"

    hide yuri bravo
    hide leo bravo
    hide ana chateada
    show prof normal
    voice "audio/vozes/prof/prof2.mp3"
    prof "Crianças, vocês precisam parar de gritar para que eu entenda vocês. Certo?"

    hide prof normal
    show leo triste at right
    show ana triste at left
    show yuri triste at center
    voice "audio/vozes/narradora/narradora4.mp3"
    narradora "(Eventualmente as crianças param de gritar umas com as outras e conseguem explicar a situação.)"

    hide yuri triste
    hide ana triste
    hide leo triste
    show leo bravo at center
    voice "audio/vozes/leo/leo8.mp3"
    leo "Eu preciso do meu caderno de volta mas a Ana é muito lerda! Ela não terminou de copiar ainda!"
    show leo bravo at right
    show prof brava at center
    voice "audio/vozes/prof/prof3-8.mp3"
    prof "Léo, não chame sua colega assim."
    hide leo bravo
    hide prof brava
    show prof normal
    voice "audio/vozes/prof/prof4.mp3"
    prof "Léo e Ana, vocês não podem falar assim um com o outro."
    voice "audio/vozes/prof/prof5.mp3"
    prof "Quanto mais vocês xingam um ao outro, mais irritados ficam. Tentem conversar da próxima vez. Sem gritarem!"
    voice "audio/vozes/prof/prof6.mp3"
    prof "Yuri, você também. Da próxima vez me chame para ajudar a resolver o conflito. Não se junte a gritaria."

    hide prof normal
    show leo triste at right
    show ana triste at left
    voice "audio/vozes/leo/leo9.mp3"
    leo "...desculpe ter te chamado de lerda, Ana. Não foi legal da minha parte."
    voice "audio/vozes/ana/ana7-9.mp3"
    ana "Eu te chamei de chato também... desculpa."

    show yuri surpreso at center
    voice "audio/vozes/yuri/yuri17.mp3"
    yuri "Léo, você precisa desse caderno agora?"
    hide leo triste
    show leo surpreso at right
    voice "audio/vozes/leo/leo10.mp3"
    leo "Sim."
    hide yuri surpreso
    show yuri triste at center
    voice "audio/vozes/yuri/yuri18.mp3"
    yuri "Hmmm..."
    hide yuri triste
    hide leo surpreso
    hide ana triste
    show ana surpresa at center
    voice "audio/vozes/ana/ana3-10.mp3"
    ana "Já sei!"
    hide ana surpresa
    show ana normal
    voice "audio/vozes/ana/ana4-11.mp3"
    ana "Léo, quando você chegar em casa pode me mandar uma foto do seu caderno? Assim eu posso copiar a matéria que perdi depois da aula e você pode usar seu caderno agora."
    hide ana normal
    show leo feliz
    voice "audio/vozes/leo/leo11.mp3"
    leo "Claro, Ana. Isso resolve o problema."

    hide leo feliz
    show yuri feliz
    voice "audio/vozes/yuri/yuri19.mp3"
    yuri "Que bom que vocês se entenderam!"
    voice "audio/vozes/narradora/narradora5.mp3"
    narradora "(Comunicando-se de forma não violenta, a professora conseguiu reolver a situação. Da próxima vez, quem sabe podemos tentar a mesma coisa?)"

    jump intervalo

label leo_ana3:
    show yuri triste
    voice "audio/vozes/yuri/yuri20.mp3"
    yuri "Ana, você está bem? Léo, vamos conversar sobre isso."

    hide yuri triste
    show ana brava at left
    show leo bravo at right
    voice "audio/vozes/leo/leo12.mp3"
    leo "Yuri! Ela não quer me devolver o meu caderno! Eu preciso dele."
    voice "audio/vozes/ana/ana8.mp3"
    ana "E eu preciso copiar a matéria que perdi!"
    show yuri surpreso at center
    voice "audio/vozes/yuri/yuri21.mp3"
    yuri "Humm...Olha! A professora chegou. Vamos chamar ela para nos ajudar"

    hide yuri surpreso
    show prof normal at center
    voice "audio/vozes/prof/prof7.mp3"
    prof "O que está acontecendo aqui?"
    voice "audio/vozes/leo/leo13.mp3"
    leo "Eu preciso do meu caderno de volta mas a Ana é muito lerda! Ela não terminou de copiar ainda!"
    hide prof normal
    show prof brava
    voice "audio/vozes/prof/prof3-8.mp3"
    prof "Léo, não chame sua colega assim."
    voice "audio/vozes/prof/prof9.mp3"
    prof "Falando desta forma vocês realmente não vão resolver nada, só vão irritar um ao outro."

    hide prof brava
    hide leo bravo
    hide ana brava
    show leo triste at right
    voice "audio/vozes/leo/leo14.mp3"
    leo "...desculpe ter te chamado de lerda, Ana. Não foi legal da minha parte."
    hide leo triste
    show ana triste at left
    voice "audio/vozes/ana/ana7-9.mp3"
    ana "Eu te chamei de chato também...desculpa."

    hide ana triste
    show prof normal
    voice "audio/vozes/prof/prof10.mp3"
    prof "Muito bem. Agora, alguém tem uma ideia para resolvermos essa briga?"
    hide prof normal
    show yuri surpreso
    voice "audio/vozes/yuri/yuri22.mp3"
    yuri "A Ana não pode tirar uma foto do caderno do Léo, prof? Assim ela copia a matéria em casa e ele pode usar o caderno agora."
    hide yuri surpreso
    show prof feliz
    voice "audio/vozes/prof/prof11.mp3"
    prof "Boa ideia, Yuri!"
    voice "audio/vozes/prof/prof12.mp3"
    prof "Viram? Quando conversamos as coisas são resolvidas mais facilmente"

    hide prof feliz
    voice "audio/vozes/narradora/narradora6.mp3"
    narradora "(A situação é resolvida com a ajuda de Yuri. No início da aula a professora acaba falando um pouco sobre a importância de tratar uns aos outros com respeito.)"

    jump intervalo


label intervalo:

    play sound "audio/efeitos/alarme.mp3"
    scene patio

    show yuri feliz with fade
    voice "audio/vozes/yuri/yuri23.mp3"
    yuri "Está na hora do intervalo! Vou achar alguém para brincar..."

    hide yuri feliz
    show yuri normal
    voice "audio/vozes/yuri/yuri24.mp3"
    yuri "Olha, parece que o Pedro e a Bia estão logo aqui na frente."
    voice "audio/vozes/yuri/yuri25.mp3"
    yuri "Vou perguntar se posso brincar com eles!"

    voice "audio/vozes/yuri/yuri26.mp3"
    yuri "Ei, Bia! Oi, Pedro!"
    show bia brava at left
    show pedro triste at right
    voice "audio/vozes/yuri/yuri27.mp3"
    yuri "Posso brincar com vocês dois?"

    hide yuri normal
    hide pedro triste
    hide bia brava
    show bia brava at center
    voice "audio/vozes/bia/bia1.mp3"
    bia "No caso você vai brincar só comigo Yuri."
    voice "audio/vozes/bia/bia2.mp3"
    bia "Não da para brincar com o Pedro! Ele só reclama das brincadeiras que eu escolho!"

    hide bia brava
    show pedro triste
    pedro "..."
    voice "audio/vozes/pedro/pedro1.ogg"
    pedro "Você sabe que eu não reclamo só por reclamar..."

    hide pedro triste
    show bia brava
    voice "audio/vozes/bia/bia3.mp3"
    bia "Ah! Agora você está me escutando? Nem me pediu pra repetir o que disse!"
    voice "audio/vozes/bia/bia4.mp3"
    bia "Quando você quer escutar, você escuta, né?"

    hide bia brava
    show pedro triste
    pedro "..."
    voice "audio/vozes/pedro/pedro2.ogg"
    pedro "É que você está gritando, Bia..."

    hide pedro triste
    show yuri triste
    voice "audio/vozes/yuri/yuri28.mp3"
    yuri "O que será que devo fazer?"

    play sound "audio/efeitos/menu3.mp3" loop
    menu:
        "Bia, por que o Pedro não pode brincar com a gente? Todos devem participar!":
            play sound "audio/efeitos/certo.mp3"
            jump bia_pedro1
        "Pedro, vem brincar comigo. Não ligue para a Bia. Ela é chata mesmo!":
            play sound "audio/efeitos/errado.mp3"
            $ estrelas -= 1
            jump bia_pedro2
        "Bia, eu acho que você não está sendo muito justa... Vamos conversar.":
            play sound "audio/efeitos/certo.mp3"
            jump bia_pedro3

label bia_pedro1:
    show yuri triste
    voice "audio/vozes/yuri/yuri29.mp3"
    yuri "Bia, por que o Pedro não pode brincar com a gente? Todos devem participar!"

    show bia brava at left
    voice "audio/vozes/bia/bia5.mp3"
    bia "Yuri! Ele reclama de todas as brincadeiras que eu sugiro!"

    show pedro triste at right
    voice "audio/vozes/pedro/pedro3.ogg"
    pedro "...eu já disse que tenho um motivo. Você sabe que-"
    voice "audio/vozes/bia/bia6.mp3"
    bia "Pare de inventer desculpinhas! Você só está sendo chato!"

    hide yuri triste
    show yuri surpreso at center
    voice "audio/vozes/yuri/yuri30.mp3"
    yuri "Ei, Bia..."
    voice "audio/vozes/yuri/yuri31.mp3"
    yuri "Não chame o Pedro assim. Você não gostaria que te xingassem desse jeito, não é?"

    hide bia brava
    show bia surpresa at left
    voice "audio/vozes/bia/bia7.mp3"
    bia "Hum..."

    hide yuri surpreso
    show yuri normal at center
    voice "audio/vozes/yuri/yuri32.mp3"
    yuri "Vamos deixar o Pedro terminar de falar."
    voice "audio/vozes/yuri/yuri33.mp3"
    yuri "O que você dizia, Pedro?"

    voice "audio/vozes/pedro/pedro4-20.ogg"
    pedro "...é que eu não reclamei por mal."
    hide yuri normal
    hide bia surpresa
    show pedro surpreso at center
    voice "audio/vozes/pedro/pedro5-21.ogg"
    pedro "Bia, você sugeriu que brincassemos de telefone sem fio."
    voice "audio/vozes/pedro/pedro6-22.ogg"
    pedro "E você sabe que eu não escuto muito bem..."
    voice "audio/vozes/pedro/pedro7-23.ogg"
    pedro "Não seria muito divertido para mim essa brincadeira."

    hide pedro surpreso
    show bia triste at center
    bia "..."
    voice "audio/vozes/bia/bia8-19.mp3"
    bia "Eu não tinha pensado por esse lado..."
    voice "audio/vozes/bia/bia9-20.mp3"
    bia "Desculpe ter falado daquela forma com você...não foi legal."

    hide bia triste
    show pedro normal at center
    voice "audio/vozes/pedro/pedro8-24.ogg"
    pedro "...tudo bem. Foi um mal entendido!"

    show bia normal at left
    voice "audio/vozes/bia/bia10-21.mp3"
    bia "Não vai acontecer de novo! Eu prometo."

    hide pedro normal
    show pedro normal at right
    show yuri normal at center
    voice "audio/vozes/yuri/yuri34.mp3"
    yuri "Que bom que vocês se entenderam!"
    voice "audio/vozes/yuri/yuri35.mp3"
    yuri "Agora podemos brincar juntos!"

    hide pedro normal
    show pedro feliz at right
    voice "audio/vozes/pedro/pedro9-25.ogg"
    pedro "Sim!"
    voice "audio/vozes/pedro/pedro10-26.ogg"
    pedro "O que vocês acham de brincar de mímica?"

    hide bia normal
    show bia feliz at left
    voice "audio/vozes/bia/bia11-22.mp3"
    bia "Parece uma boa ideia!"
    voice "audio/vozes/bia/bia12-23.mp3"
    bia "Vamos chamar os outros também!"

    hide pedro feliz
    hide bia feliz
    hide yuri normal
    show yuri feliz
    voice "audio/vozes/yuri/yuri36.mp3"
    yuri "Certo!"

    hide yuri feliz
    voice "audio/vozes/narradora/narradora7.mp3"
    narradora "(Após conversarem de forma pacífica, as crianças resolveram seus conflitos e se desculparam. A brincadeira de mímica foi muito divertida e todos adoraram as imitações que Yuri fez do Homem Aranha!)"
    jump atividade_grupo

label bia_pedro2:
    hide yuri triste
    show yuri bravo
    voice "audio/vozes/yuri/yuri37.mp3"
    yuri "Pedro, vem brincar comigo. Não ligue para a Bia. Ela é chata mesmo!"

    hide yuri bravo
    show bia brava
    voice "audio/vozes/bia/bia13.mp3"
    bia "Ei, Yuri! Eu vou contar para a professora que você disse isso!"

    hide bia brava
    show yuri bravo
    voice "audio/vozes/yuri/yuri38.mp3"
    yuri "Se você chamar a prof Ruth, eu vou contar para ela que você estava brigando com o Pedro!"

    hide yuri bravo
    show pedro bravo
    voice "audio/vozes/pedro/pedro11.ogg"
    pedro "Chega, vocês dois!"
    voice "audio/vozes/pedro/pedro12.ogg"
    pedro "Parem de gritar!"

    hide pedro bravo
    show bia brava
    voice "audio/vozes/bia/bia14.mp3"
    bia "Fica na sua, Pedro! Ainda estou brava com você!"

    hide bia brava
    show pedro bravo
    voice "audio/vozes/pedro/pedro13.ogg"
    pedro "Está brava porque não deixou que eu me explicasse!"
    hide pedro bravo
    show pedro triste
    voice "audio/vozes/pedro/pedro14.ogg"
    pedro "Eu não estava reclamando da brincadeira só por reclamar..."
    voice "audio/vozes/pedro/pedro15.ogg"
    pedro "Você sugeriu que brincassemos de telefone sem fio."
    voice "audio/vozes/pedro/pedro16.ogg"
    pedro "Mas você sabe que eu não escuto muito bem!"
    voice "audio/vozes/pedro/pedro17.ogg"
    pedro "Não seria uma brincadeira divertida para mim."

    hide pedro triste
    show pedro triste at right
    show bia triste at left
    bia "..."
    voice "audio/vozes/bia/bia15.mp3"
    bia "Me desculpa, Pedro..."

    hide pedro triste
    show pedro surpreso at right
    pedro "..."
    hide pedro surpreso
    show pedro triste at right
    voice "audio/vozes/pedro/pedro18.ogg"
    pedro "Tanto faz. Eu não quero mais brincar..."
    voice "audio/vozes/pedro/pedro19.ogg"
    pedro "Vou para a sala."

    hide pedro triste
    hide bia triste
    voice "audio/vozes/narradora/narradora8.mp3"
    narradora "(Pedro vai embora do pátio. Bia olha para Yuri com raiva.)"

    show bia brava at left
    voice "audio/vozes/bia/bia16.mp3"
    bia "Viu só o que você fez!"

    show yuri bravo at right
    voice "audio/vozes/yuri/yuri39.mp3"
    yuri "Eu não fiz nada! Foi você quem começou!"

    voice "audio/vozes/bia/bia17.mp3"
    bia "Quer saber? Não quero mais brincar com você!"

    voice "audio/vozes/yuri/yuri40.mp3"
    yuri "Então pode ir embora!"

    hide yuri bravo
    hide bia brava
    voice "audio/vozes/narradora/narradora9.mp3"
    narradora "(A situação saiu do controle. Yuri acabou indo conversar com a professora. Ela garantiu a ele que mais tarde conversariam com Pedro e Bia. Infelizmente a comunicação de Yuri não foi muito gentil nesse momento.)"

    jump atividade_grupo

label bia_pedro3:
    show yuri triste
    voice "audio/vozes/yuri/yuri41.mp3"
    yuri "Bia, eu acho que você não está sendo muito justa... Vamos conversar."

    hide yuri triste
    show bia surpresa
    bia "..."
    hide bia surpresa
    show bia triste
    voice "audio/vozes/bia/bia18.mp3"
    bia "Desculpa. Talvez eu tenha ido um pouco longe demais..."

    hide bia triste
    show yuri surpreso
    voice "audio/vozes/yuri/yuri42.mp3"
    yuri "Vamos deixar o Pedro terminar de falar."
    voice "audio/vozes/yuri/yuri43.mp3"
    yuri "O que você dizia, Pedro?"

    hide yuri surpreso
    show pedro surpreso
    voice "audio/vozes/pedro/pedro4-20.ogg"
    pedro "...é que eu não reclamei por mal."
    voice "audio/vozes/pedro/pedro5-21.ogg"
    pedro "Bia, você sugeriu que brincassemos de telefone sem fio."
    hide pedro surpreso
    show pedro triste
    voice "audio/vozes/pedro/pedro6-22.ogg"
    pedro "E você sabe que eu não escuto muito bem..."
    voice "audio/vozes/pedro/pedro7-23.ogg"
    pedro "Não seria muito divertido para mim essa brincadeira."

    hide pedro triste
    show bia triste
    voice "audio/vozes/bia/bia8-19.mp3"
    bia "Eu não tinha pensado por esse lado..."
    voice "audio/vozes/bia/bia9-20.mp3"
    bia "Desculpe ter falado daquela forma com você...não foi legal."

    hide bia triste
    show bia surpresa at left
    show pedro normal at right
    voice "audio/vozes/pedro/pedro8-24.ogg"
    pedro "...tudo bem. Foi um mal entendido!"
    voice "audio/vozes/bia/bia10-21.mp3"
    bia "Não vai acontecer de novo! Eu prometo."

    show yuri normal at center
    voice "audio/vozes/yuri/yuri44.mp3"
    yuri "Que bom que vocês se entenderam! Viram como é fácil resolver as coisas quando conversamos tranquilamente?"
    hide yuri normal
    show yuri feliz at center
    voice "audio/vozes/yuri/yuri45.mp3"
    yuri "Agora podemos brincar juntos!"

    hide pedro normal
    show pedro feliz at right
    voice "audio/vozes/pedro/pedro9-25.ogg"
    pedro "Sim!"
    voice "audio/vozes/pedro/pedro10-26.ogg"
    pedro "O que vocês acham de brincar de mímica?"

    hide bia surpresa
    show bia feliz at left
    voice "audio/vozes/bia/bia11-22.mp3"
    bia "Parece uma boa ideia!"
    voice "audio/vozes/bia/bia12-23.mp3"
    bia "Vamos chamar os outros também!"

    hide yuri feliz
    hide pedro feliz
    show pedro surpreso at right
    voice "audio/vozes/pedro/pedro27.ogg"
    pedro "...desculpa eu não consegui te ouvir."

    hide bia feliz
    show bia normal at left
    voice "audio/vozes/bia/bia24.mp3"
    bia "Sem problemas. Vou falar um pouco mais alto."
    voice "audio/vozes/bia/bia25.mp3"
    bia "Eu disse para chamarmos os outros também!"

    hide pedro surpreso
    show pedro normal at right
    voice "audio/vozes/pedro/pedro28.ogg"
    pedro "Ah! Certo, parece legal!"

    hide bia normal
    hide pedro normal
    voice "audio/vozes/narradora/narradora10.mp3"
    narradora "(Após conversarem de forma pacífica, as crianças resolveram seus conflitos e se desculparam. A brincadeira de mímica foi muito divertida e todos adoraram a imitação que Yuri fez da Pequena Sereia!)"

    jump atividade_grupo

label atividade_grupo:

    play sound "audio/efeitos/alarme.mp3"
    scene sala with fade

    play sound "audio/efeitos/conversa.mp3"

    show prof feliz
    voice "audio/vozes/prof/prof13.mp3"
    prof "Certo, crianças! Acalmem-se." 
    stop sound
    voice "audio/vozes/prof/prof14.mp3"
    prof "Vamos fazer um trabalho em grupo hoje."
    voice "audio/vozes/prof/prof15.mp3"
    prof "Formem grupos de 5 pessoas. Vocês vão inventar um mascote para a escola!"
    voice "audio/vozes/prof/prof16.mp3"
    prof "Escolham um nome para o mascote e desenhem ele como imaginarem."
    voice "audio/vozes/prof/prof17.mp3"
    prof "Os trabalhos serão expostos no mural no fim do dia!"

    hide prof feliz
    scene parede
    show yuri normal
    voice "audio/vozes/yuri/yuri46.mp3"
    yuri "Vou me juntar com a Mariana, Aisha e Pablo como sempre!"
    voice "audio/vozes/yuri/yuri47.mp3"
    yuri "Ei, Aisha! Vamos fazer juntos este trabalho?"

    hide yuri normal
    show aisha feliz at left
    voice "audio/vozes/aisha/aisha1.ogg"
    aisha "Claro!"
    show mariana feliz at right
    voice "audio/vozes/mariana/mariana1.mp3"
    mariana "Junta a sua classe com as nossas Yuri."

    hide mariana feliz
    hide aisha feliz
    show yuri feliz
    voice "audio/vozes/yuri/yuri48.mp3"
    yuri "Certo!"

    hide yuri feliz
    voice "audio/vozes/narradora/narradora11.mp3"
    narradora "(Yuri, Mariana, Aisha e Pablo juntam suas classes. Mas ainda precisam de um quinto membro para o grupo.)"
    voice "audio/vozes/narradora/narradora12.mp3"
    narradora "(Um menino tímido aparece ao lado do grupo.)"

    show miguel surpreso
    voice "audio/vozes/miguel/miguel1.mp3"
    miguel "Hum...Oi, gente."
    hide miguel surpreso
    show pablo normal
    voice "audio/vozes/pablo/pablo1.mp3"
    pablo "Oi, Miguel! Você quer fazer o trabalho com a gente também?"

    hide pablo normal
    show miguel surpreso
    voice "audio/vozes/miguel/miguel2.mp3"
    miguel "Sim! Obrigado."

    show yuri normal at right
    voice "audio/vozes/yuri/yuri49.mp3"
    yuri "Não precisa agradecer!"

    hide miguel surpreso
    hide yuri normal
    voice "audio/vozes/narradora/narradora13.mp3"
    narradora "(As crianças começam a discutir como será o mascote de seu grupo. O grupo de Yuri parece estar tendo dificuldades em concordar sobre o que fazer.)"

    show pablo surpreso at center
    voice "audio/vozes/pablo/pablo2.mp3"
    pablo "Eu ainda acho que um tigre seria melhor!"
    show aisha surpresa at left
    voice "audio/vozes/aisha/aisha2.ogg"
    aisha "Você só está sugerindo isso porque tigres são seus animais favoritos!"
    show mariana surpresa at right
    voice "audio/vozes/mariana/mariana2.mp3"
    mariana "E o que um tigre tem haver com a nossa escola?"
    voice "audio/vozes/pablo/pablo3.mp3"
    pablo "Eles são maneiros..."

    hide pablo surpreso
    show miguel surpreso
    miguel "..."
    hide miguel surpreso
    show pablo surpreso at center
    voice "audio/vozes/aisha/aisha3.ogg"
    aisha "Eu tenho certeza que uma borboleta seria melhor! Elas podem ser roxas que nem nosso uniforme!"
    hide mariana surpresa
    show mariana brava at right
    voice "audio/vozes/mariana/mariana3.mp3"
    mariana "Ah não, Iaia! Borboletas nem podem contar como animais!"
    hide aisha surpresa
    show aisha brava at left
    voice "audio/vozes/aisha/aisha4.ogg"
    aisha "Claro que podem!"

    hide mariana brava
    hide aisha brava
    hide pablo surpreso
    scene sala
    show prof brava
    voice "audio/vozes/prof/profExtra.mp3"
    prof"Crianças, não gritem por favor."

    hide prof brava
    scene parede
    show pablo normal
    voice "audio/vozes/pablo/pablo4.mp3"
    pablo "Desculpa, prof!"
    hide pablo normal

    show miguel surpreso
    miguel "..."

    hide miguel surpreso
    show yuri surpreso
    voice "audio/vozes/narradora/narradora14.mp3"
    narradora "(Miguel parece querer dizer algo, mas acaba sendo interrompido todas as vezes que tenta falar. Yuri percebe isso. O que ele deve fazer?)"

    play sound "audio/efeitos/menu4.mp3" loop
    menu:
        "Ei, pessoal, vamos ouvir o que o Miguel tem a dizer. Ele parece ter uma ideia!":
            play sound "audio/efeitos/certo.mp3"
            jump miguel_mariana_aisha1
        "Miguel, você pode me contar sua ideia e eu falo para o grupo. Já que você não consegue nem falar aparentemente!":
            play sound "audio/efeitos/errado.mp3"
            $ estrelas -= 1
            jump miguel_mariana_aisha2
        "Miguel, você gostaria de compartilhar alguma ideia? Acho que todos gostariam de ouvir.":
            play sound "audio/efeitos/certo.mp3"
            jump miguel_mariana_aisha3

label miguel_mariana_aisha1:
    
    voice "audio/vozes/yuri/yuri50.mp3"
    yuri "Ei, pessoal, vamos ouvir o Miguel. Ele parece ter uma ideia!"

    hide yuri surpreso
    voice "audio/vozes/narradora/narradora15.mp3"
    narradora "(Miguel parece um pouco relutante em ter sido empurrado para a discussão desta forma.)"
    voice "audio/vozes/narradora/narradora16.mp3"
    narradora "(Os olhares dos seus colegas de grupo estão todos esperando que ele diga algo.)"

    show miguel surpreso
    voice "audio/vozes/miguel/miguel3-10.mp3"
    miguel "Erm...não é nada demais, sério!"

    hide miguel surpreso
    show yuri surpreso
    voice "audio/vozes/yuri/yuri51.mp3"
    yuri "Ah! Desculpa ter chamado a atenção pra você assim!"
    voice "audio/vozes/yuri/yuri52.mp3"
    yuri "Mas, sério. O que eu quis dizer é que você pode compartilhar o que pensa se quiser, é claro."

    show mariana normal at right
    voice "audio/vozes/mariana/mariana4-10.mp3"
    mariana "É, Miguel! Pode falar com a gente, prometemos ouvir o que você tem a dizer."
    show aisha normal at left
    voice "audio/vozes/aisha/aisha5-8.ogg"
    aisha "...e desculpa por essa cena que acabamos de causar."

    hide yuri surpreso
    hide mariana normal
    hide aisha normal
    show miguel normal
    voice "audio/vozes/miguel/miguel4-11.mp3"
    miguel "Tudo bem. É..."
    voice "audio/vozes/miguel/miguel5-12.mp3"
    miguel "Eu iria sugerir que o mascote fosse um camaleão."

    show yuri normal at right
    voice "audio/vozes/yuri/yuri53.mp3"
    yuri "Por que um camaleão?"

    voice "audio/vozes/miguel/miguel6-13.mp3"
    miguel "Porque ele pode mudar de cores. Ser várias coisas ao mesmo tempo que pode ser só ele mesmo."
    voice "audio/vozes/miguel/miguel7-14.mp3"
    miguel "Camaleões levam diversidade por onde passam!"

    show pablo feliz at left
    voice "audio/vozes/pablo/pablo5-8.mp3"
    pablo "Que legal!"
    voice "audio/vozes/pablo/pablo6-9.mp3"
    pablo "Nós podemos fazer uma camaleão disfarçado de tigre!"

    hide pablo feliz
    show aisha feliz at left
    voice "audio/vozes/aisha/aisha6-9.ogg"
    aisha "Só se ele puder ter asas de borboleta também!"
    hide yuri normal
    show mariana normal at right
    voice "audio/vozes/mariana/mariana5-11.mp3"
    mariana "Acho que podemos fazer isso! Não precisa ser um animal que existe!"

    hide miguel normal
    hide aisha feliz
    hide mariana normal
    show yuri normal
    voice "audio/vozes/yuri/yuri54.mp3"
    yuri "Certo!"
    voice "audio/vozes/yuri/yuri55.mp3"
    yuri "E que nome podemos dar a ele?"

    hide yuri normal
    show miguel surpreso
    voice "audio/vozes/miguel/miguel8-15.mp3"
    miguel "Humm...o que acham de Camitigo?"
    hide miguel surpreso
    show miguel normal
    voice "audio/vozes/miguel/miguel9-16.mp3"
    miguel "Lembra um pouco o nome dos dois animais!"

    hide miguel normal
    show mariana feliz
    voice "audio/vozes/mariana/mariana6-12.mp3"
    mariana "Eu gostei! Vou começar a desenhar ele!"

    hide mariana feliz
    voice "audio/vozes/narradora/narradora17.mp3"
    narradora "(Mesmo que de uma forma não muito sensivel, mas com boas intenções, Yuri conseguiu incluir Miguel na conversa do grupo. O que importa é que a comunicação foi promovida entre os amigos!)"
    voice "audio/vozes/narradora/narradora18.mp3"
    narradora "(No fim do dia os trabalhos foram expostos no mural. O trabalho do grupo foi muito elogiado!)"

    jump conclusao_episodio

label miguel_mariana_aisha2:
    hide yuri surpreso
    show yuri bravo
    voice "audio/vozes/yuri/yuri56.mp3"
    yuri "Miguel, você pode me contar sua ideia e eu falo para o grupo. Já que você não consegue nem falar aparentemente!"
    
    hide yuri bravo
    show miguel triste
    miguel "..."

    hide miguel triste
    show mariana brava at right
    voice "audio/vozes/mariana/mariana7.mp3"
    mariana "Ei, Yuri! Por que você foi grosso dessa forma?"
    show pablo triste at center
    voice "audio/vozes/pablo/pablo7.mp3"
    pablo "Cara, isso não foi legal..."
    show aisha triste at left
    voice "audio/vozes/aisha/aisha7.ogg"
    aisha "Miguel, se você quer falar algo pode falar com a gente. Não liga para o que ele diz."
    hide mariana brava
    show mariana triste at right
    voice "audio/vozes/mariana/mariana8.mp3"
    mariana "É, Miguel. Desculpa estarmos falando alto, acabamos não te ouvindo."
    voice "audio/vozes/mariana/mariana9.mp3"
    mariana "Mas pode falar agora, vamos te escutar."

    hide pablo triste
    hide mariana triste
    hide aisha triste
    show yuri bravo
    voice "audio/vozes/narradora/narradora19.mp3"
    narradora "(Yuri parece ficar bravo com a situação de ter sido repreendido.)"

    voice "audio/vozes/yuri/yuri57.mp3"
    yuri "Com licença. Vou ir falar com a professora."

    scene sala
    voice "audio/vozes/narradora/narradora20.mp3"
    narradora "(Yuri vai até a mesa da professora Ruth.)"

    hide yuri bravo
    show prof normal
    voice "audio/vozes/prof/prof18.mp3"
    prof "Oi, Yuri. O que aconteceu?"

    show yuri bravo at left
    voice "audio/vozes/yuri/yuri58.mp3"
    yuri "Meu grupo me repreendeu."
    voice "audio/vozes/prof/prof19.mp3"
    prof "Você sabe por quê?"

    hide yuri bravo
    show yuri surpreso at left
    yuri "..."
    hide yuri surpreso
    show yuri bravo at left
    voice "audio/vozes/yuri/yuri59.mp3"
    yuri "Eu fiquei irritado com o Miguel. Parece que ele não consegue falar com os outros que nem todo mundo!"

    hide prof normal
    show prof brava
    prof "..."
    voice "audio/vozes/prof/prof20.mp3"
    prof "Yuri, isso não é algo legal de se dizer. O Miguel só é um pouco mais tímido."
    voice "audio/vozes/prof/prof21.mp3"
    prof "As vezes ele precisa de um empurrãozinho para botar pra fora o que ele pensa."

    hide yuri bravo
    show yuri triste at left
    yuri "..."

    voice "audio/vozes/prof/prof22.mp3"
    prof "O que você acha que deve fazer sobre a sua atitude?"

    voice "audio/vozes/yuri/yuri60.mp3"
    yuri "...pedir desculpas pra ele?"

    hide prof brava
    show prof normal
    voice "audio/vozes/prof/prof23.mp3"
    prof "É um bom jeito de começar."
    voice "audio/vozes/prof/prof24.mp3"
    prof "Da próxima vez, tente conversar com o Miguel antes de xingá-lo. Certo?"
    voice "audio/vozes/yuri/yuri61.mp3"
    yuri "Certo..."

    hide prof normal
    scene parede
    hide yuri triste
    show yuri triste at center
    show miguel triste at right
    voice "audio/vozes/narradora/narradora21.mp3"
    narradora "(No fim, Yuri acabou se desculpando com Miguel, que aceitou suas desculpas.)"
    voice "audio/vozes/narradora/narradora22.mp3"
    narradora "(Entretanto, Yuri se sentiu envergonhado por sua atitude, então acabou não colaborando muito com o trabalho.)"
    hide yuri triste
    hide miguel triste
    voice "audio/vozes/narradora/narradora23.mp3"
    narradora "(Da próxima vez, ele tentará comunicar-se de forma menos violenta.)"

    jump conclusao_episodio

label miguel_mariana_aisha3:
    hide yuri surpreso
    show yuri normal
    voice "audio/vozes/yuri/yuri62.mp3"
    yuri "Miguel, você gostaria de compartilhar alguma ideia? Acho que todos gostariam de ouvir."

    hide yuri normal
    voice "audio/vozes/narradora/narradora24.mp3"
    narradora "(Miguel parece feliz de que tenham falado com ele.)"

    show miguel normal
    voice "audio/vozes/miguel/miguel3-10.mp3"
    miguel "Erm...não é nada demais, sério!"

    show mariana normal at right
    voice "audio/vozes/mariana/mariana4-10.mp3"
    mariana "Miguel, pode falar com a gente, prometemos ouvir o que você tem a dizer."
    show aisha normal at left
    voice "audio/vozes/aisha/aisha5-8.ogg"
    aisha "...e desculpa por essa cena que acabamos de causar."

    voice "audio/vozes/miguel/miguel4-11.mp3"
    miguel "Tudo bem. É..."
    voice "audio/vozes/miguel/miguel5-12.mp3"
    miguel "Eu iria sugerir que o mascote fosse um camaleão."

    hide mariana normal
    hide aisha normal
    show yuri surpreso at left
    voice "audio/vozes/yuri/yuri63.mp3"
    yuri "Por que um camaleão?"

    voice "audio/vozes/miguel/miguel6-13.mp3"
    miguel "Porque ele pode mudar de cores. Ser várias coisas ao mesmo tempo que pode ser só ele mesmo."
    voice "audio/vozes/miguel/miguel7-14.mp3"
    miguel "Camaleões levam diversidade por onde passam!"

    show pablo surpreso at right
    voice "audio/vozes/pablo/pablo5-8.mp3"
    pablo "Que legal!"
    voice "audio/vozes/pablo/pablo6-9.mp3"
    pablo "Nos podemos fazer uma camaleão disfarçado de tigre!"

    hide yuri surpreso
    hide miguel normal
    hide pablo surpreso
    show pablo normal at center
    show aisha feliz at left
    voice "audio/vozes/aisha/aisha6-9.ogg"
    aisha "Só se ele puder ter asas de borboleta também!"
    show mariana feliz at right
    voice "audio/vozes/mariana/mariana5-11.mp3"
    mariana "Acho que podemos fazer isso! Não precisa ser um animal que existe!"

    hide pablo normal
    hide aisha feliz
    hide mariana feliz
    show yuri feliz
    voice "audio/vozes/yuri/yuri64.mp3"
    yuri "Certo!"
    voice "audio/vozes/yuri/yuri65.mp3"
    yuri "E que nome podemos dar a ele?"

    hide yuri feliz
    show miguel surpreso
    voice "audio/vozes/miguel/miguel8-15.mp3"
    miguel "Humm...o que acham de Camitigo?"
    hide miguel surpreso
    show miguel feliz
    voice "audio/vozes/miguel/miguel9-16.mp3"
    miguel "Lembra um pouco o nome dos dois animais!"

    hide miguel feliz
    show mariana feliz
    voice "audio/vozes/mariana/mariana6-12.mp3"
    mariana "Eu gostei! Vou começar a desenhar ele!"

    hide mariana feliz
    voice "audio/vozes/narradora/narradora25.mp3"
    narradora "(Yuri conseguiu incluir Miguel na conversa do grupo de forma educada e sensivel, respeitando seu espaço.)"
    voice "audio/vozes/narradora/narradora26.mp3"
    narradora "(No fim do dia os trabalhos foram expostos no mural. O trabalho do grupo foi muito elogiado!)"
    jump conclusao_episodio

label conclusao_episodio:
    if estrelas == 3:
        scene final_3_estrelas with dissolve
        voice "audio/vozes/narradora/narradora27.mp3"
        narradora "Parabéns pelas escolhas jogador! Hoje você fez de Yuri um cidadão melhor. Aqui está sua pontuação final. Continue assim!"
    elif estrelas == 2:
        scene final_2_estrelas with dissolve
        voice "audio/vozes/narradora/narradora28.mp3"
        narradora "Parabéns pelas escolhas jogador! Hoje você fez de Yuri um cidadão melhor. Aqui está sua pontuação final. Continue assim!"
    elif estrelas == 1:
        scene final_1_estrelas with dissolve
        voice "audio/vozes/narradora/narradora29.mp3"
        narradora "Infelizmente, hoje suas escolhas não foram as melhores, jogador. Yuri terá que pensar um pouco sobre suas atitudes e tentar fazer melhor da próxima vez. Tente também! Aqui está sua pontuação final."
    else:
        scene final_0_estrelas with dissolve
        voice "audio/vozes/narradora/narradora30.mp3"
        narradora "Infelizmente, hoje suas escolhas não foram as melhores, jogador. Yuri terá que pensar um pouco sobre suas atitudes e tentar fazer melhor da próxima vez. Tente também! Aqui está sua pontuação final."
    scene creditos with dissolve
    pause 10
    return