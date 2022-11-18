import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

from io import BytesIO
import requests

#ANALISE DE DADOS
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjhdfDYTI3HNP0wpxBAp_YePhfyBj9GlLAmFgW2zUsTQiWJwkY_iUvVuhiT9AD2X81uJQalB89rYlw/pub?gid=2112212887&single=true&output=csv')
DB = r.content
df = pd.read_csv(BytesIO(DB), index_col=0)
df.columns = ['Curso', 'Nome', 'CPF', 'Endereco', 'Telefone', 'e-mail']
curso = df['Curso']
nome = df['Nome']
#mail = df['email'][[0]
#st.write(df)
#st.write(df['email'])

image = Image.open('desenvolvimento.jpg')
image1 = Image.open('BibliografiaBASICA.jpg')
image2 = Image.open('BibliografiaComplementar1.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":books:")	
st.title("LINGUAGENS DE PROGRAMAÇÃO - OI ISABELA")
SUB_TITULO = '<p style="font-family:tahoma; color:Blue; font-size: 28px;">Desenvolvido pelo prof. Massaki de O. Igarashi</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)

mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''
st.markdown(mystyle, unsafe_allow_html=True)
# Generate tree equal columns
#col1, col2, col3 = st.columns((1, 1, 1))
col1, col2 = st.columns((1,1))
with col1:
    st.info(
       """
    ### ***Atenção, principiante!***
    Para você que é leigo e está começando agora a programar, este material introdutório, uma espécie de **guia rápido**, está estruturado **com um passo-a-passo a ser seguido** com se fosse uma "receita de bolo". Então, por favor, siga um passo de cada vez e tome cuidado para o bolo não desandar!
    """    
    )
with col2:
    st.info(
    """
    ### ***Aprendizado colaborativo***
    Projetado para fornecer aos usuários um espaço sobre algumas Linguagens de Programação. O objetivo não é substituir o conteúdo institucional disponível para aulas, mas servir de suporte complementar ao aprendizado compartilhado. Espero que você faça bom uso!
    """
    )

st.markdown("""
#### ***Para referenciar este material:*** """)
st.warning("IGARASHI, Massaki de O. LINGUAGENS DE PROGRAMAÇÃO. Campinas - SP, 2022, v.1 01 de agosto de 2022. Disponível em: [link](endereço).")
    
task1 = st.selectbox("👈 Selecione a linguagem desejada:",
                    ["Linguagem de Programação C++", 
                    "Análise de Dados",
                    "Linguagem de Programação R"])                                  
if task1 == "Análise de Dados": 
    #st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

    st.markdown("# DataFrame Demo")
    st.sidebar.header("DataFrame Demo")
    st.write(
        """This demo shows how to use `st.write` to visualize Pandas DataFrames.
    (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
    )


    @st.cache
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")


    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

if task1 == "Linguagem de Programação C++": 
    
    st.sidebar.markdown(
    """
    ### CONTEÚDO:
    - [**CAP 01**](#cap-01)
    ##### Conceitos Básicos / Primeiros passos
    - [**CAP 02**](#cap-02)
    ##### Saída e Entrada de Dados / Tipos de Variáveis
    - [**CAP 03**](#cap-03)
    ##### Operadores e Operações básicas
    - [**BIBLIOGRAFIA**](#bibliografia)    
    """, unsafe_allow_html=True)
    
    st.header('CAP 01')
    st.header("PRIMEIROS PASSOS")
    #st.title("01 - PRIMEIROS PASSOS")
    cols01 = st.columns(1)    
    cols01[0].write('Os primórdios do C++ datam de 1979, quando originalmente era conhecido como C com classes. Ou seja, os arquivos de classe (usados na programação orientada a objetos) passaram a ser adicionados à linguagem C. Em 1983, finalmente passou a ser denominado C ++. A linguagem C ++ existe sob a administração de um comitê de padrões e se tornou um padrão ISO em 1998 com uma revisão em 2011; outra revisão menor em 2014; 2017; e continua sendo atualizado como parte do trabalho do comitê de padrões.')
    st.markdown(
    """
    A linguagem de Programação C++ é uma linguagem de programação de uso geral com tendência para a programação de sistemas que é:
    - uma evolução  da linguagem C
    - suporta abstração de dados
    - suporta programação orientada a objetos
    - suporta programação genérica  
    """)  
    Texto01 = '<p style="font-family:tahoma; color:Blue; font-size: 18px;">A seguir, serão apresentados a você os 5 passos principais para você iniciar, rapidamente, a programar em C++. Espero que faça bom uso!</p>'
    st.markdown(Texto01, unsafe_allow_html=True)    
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 01 - FERRAMENTAS NECESSÁRIAS</p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)

    cols02 = st.columns(1)
    cols02[0].write('Antes de iniciar você precisa saber que precisará de um compilador; este compilador pode ser instalado no seu desktop, no seu celular ou simplesmente executado ambiente de núvem da internet (esta última opção pode ser executada de qualquer plataforma, basta acessar o navegador de internet do seu dispositivo).')
    st.markdown(
    """
    ###### Compiladores para S.O WINDOWS:
    - [Bloodshed Dev-C++](https://www.bloodshed.net/download.html)
    - [Code::Blocks](http://www.codeblocks.org/downloads/26)
    
    **OBSERVAÇÃO:** Instale a versão codeblocks-XX.XX ***mingw-setup.exe***. Pois ela inclui o compilador GCC/G++/GFortran e o GDB debugger necessários para a execução do seu programa 

    
    ###### Compiladores para S.O. ANDROID: 
    - [CppDroid](https://play.google.com/store/apps/details?id=name.antonsmirnov.android.cppdroid)
    - [CxxDroid](https://play.google.com/store/apps/details?id=ru.iiec.cxxdroid)
     
    ###### Compiladores WEB ONLINE:  
    - [Repl.it ](https://repl.it)
    - [OnlineGDBbeta](https://www.onlinegdb.com/online_c++_compiler)
    - [C++ Shell] (http://cpp.sh)
    - [myCompiler] (https://www.mycompiler.io/online-c++-compiler)
    - [Paiza.IO] (https://paiza.io/en/projects/new?language=cpp)
    - [CodeChef] (https://www.codechef.com/ide) 

   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 3 | ?h | ? a ?
    Dia 2 de 3 | ?h | ? a ?
    Dia 3 de 3 | ?h | ? a ?  
    
    """
    )
    SUB_TITULO1_2 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 02: Estrutura básica de um programa C++</p>'
    st.markdown(SUB_TITULO1_2, unsafe_allow_html=True)
    
    cols03 = st.columns(1)
    cols03[0].write('Ao ingressar no copilador, você precisa da estrutura básica, a seguir, para que seu programa seja executado:')
    
    coluna1, coluna2 = st.columns((1,1))
    with coluna1:
        st.info(
        """
        ###### #include <iostream>
        ###### using namespace std;
        ###### int main()
        ###### {
        ######     return 0;
        ###### }
        """
        )
    with coluna2:
        st.code(
        """
        //Nosso 1º Programa é Hello prof. Massaki!
        #include <iostream>
        using namespace std;
        int main()
        {
            cout<<"Hello prof. Massaki";
            return 0;
        }
        """)
    
    SUB_TITULO1_3 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 03: Explicações Básicas</p>'
    st.markdown(SUB_TITULO1_3, unsafe_allow_html=True)

    cols04 = st.columns(1)
    cols04[0].write('Na verdade isto é um comando que informa que no resto do seu código o compilador deve considerar que você está usando o namespace padrão. Ou seja, serve para definir escopos para as estruturas do C++.')
    
    a1, a2 = st.columns((1,1))
    with a1:
        st.info(
        """
        ##### ***using namespace std;***
        Por exemplo, no caso de dois programadores em um mesmo projeto, digamos que cada um crie uma função void Funcao(void) que façam coisas absolutamente diferentes, uma forma de resolver esse conflito é usando um namespace diferente para cada programador.
        Se você não usasse esse using namespace std quase todas as funções ou classes da biblioteca padrão que você usasse você teria que colocar um std:: antes. ***Os dois comandos mais usados do C++ sem declarar using namespace std precisao da palavra std na frente:***
        ##### std::cout <<
        ##### std::cin>> 
        ##### Isso serve para te poupar de ficar digitando tanto!
        """
        )
    with a2:
        st.info(
        """
        ##### ***<iostream>***
        O cabeçalho padrão <iostream> declara objetos que controlam fluxos padrões de leitura e escrita de dados. Esse geralmente é o único cabeçalho você precisa incluir para executar entrada e saída de um programa C ++ console básico.
        ##### ***Alguns objetos dessa biblioteca são:***
        - cin, cout, cerr e clog
        - wcin, wcout, wcerr “wcerr”
        ##### ***<cstdlib>***
        Esta é uma das bibliotecas padrões do C++ que é responsável pelas seguintes funções úteis para conversão de string para ponto flutuante, sorteios numéricos, etc. 
        ##### ***Principais funções contidas nesta biblioteca:***
        - size_t; div_t; ldiv_t; abort; abs; atexit; atof; atoi; atol; bsearch; calloc; div; exit; free; getenv; labs; ldiv; malloc; mblen; mbstowcs; mbtowc; qsort; rand; realloc; srand; strtod; strtol; strtoul; system; wcstombs; wctomb;
        ##### ***<iomanip>***
        Esta biblioteca inclui vários manipuladores que permitem formar a escrita. 
        ##### ***Dentre eles merecem destaque:***
        - setw;
        - setfill;
        - e setprecision.
        """
        )
        
    SUB_TITULO1_4 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 04: Comentários no programa</p>'
    st.markdown(SUB_TITULO1_4, unsafe_allow_html=True)

    b1, b2 = st.columns((1,1))
    with b1:
        st.subheader("Numa única linha")
        st.info(
        """
        Os comentários de linha única começam com duas barras "//". 
        ***Exemplo:***
        ###### #include <iostream>
        ###### using namespace std;
        ###### int main()
        ###### {
        ######       //Este comentario nesta linha não executa!
        ######       cout << "Hello World!"; //Exibe Hello World na tela console
        ######       return 0;
        ###### }
        """
        )
    with b2:
        st.subheader("Em várias linhas")
        st.info(
        """
        Os comentários de várias linhas começam com " /* " e terminam com " */ ".
        ***Exemplo:*** 
        ######    /* Assim você pode inserir o enunciado 
        ######       ou explicação do funcionamento de um 
        ######       programa usanod várias linhas */
        ######
        ######       #include <iostream>
        ######       using namespace std;
        ######       int main()
        ###### {     cout << "Hello World!";  //Exibe Hello World na tela
        ######       return 0;
        ###### }
        """
        )
    
    SUB_TITULO1_5 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 05: Compilando um Hello World</p>'
    st.markdown(SUB_TITULO1_5, unsafe_allow_html=True)

    cols05 = st.columns(1)
    cols05[0].write('O primeiro questionamento que se faz quando se tenta aprender uma linguagem de programação é por que o mundo inteiro faz como 1º programa (em qualquer linguagem de programação) a famosa exibição da palavra “Hello World”, que em português significa “Olá Mundo”. Não obstante, se você também quiser aprender qualquer coisa ligada ao mundo da eletrônica, precisa saber que todos mundo afora consideram como exemplo básico inicial exibir um “Hello  world”. Então aqui vão dois exemplos básicos de sintaxe de programa C++ que exibem na tela do console “Hello World”.')

    st.info("""
    Clique na [:arrow_forward:](https://replit.com/@MassakiIgarash1/011HelloWorld?v=1) 
    para executar o exemplo 
    """)
    st.code(
    """
    //Sem o using namespace é preciso usar std::
    #include <iostream>
    int main()
    {
        std::cout <<"Hello Prof.Massaki!";
        return 0;
    }
    """)
    
    st.info(
    """
    ***//Com o using namespace não precisa inserir std:: na frente dos comandos cout e cin
    ###### include <iostream>
    ###### **using namespace std;**
    ###### int main()
    ###### {
    ######     **cout<<**"Hello Prof. Massaki";
    ######     return 0;
    ###### }
    """)
    
    st.header('CAP 02')
    st.header("INTRODUÇÃO") 
    #st.title("02 - INTRODUÇÃO")    
    SUB_TITULO2_1 = '<p style="font-family:tahoma; color:Black; font-size: 26px;">2.1 - SAÍDA DE DADOS (Texto a exibir na tela).</p>'
    st.markdown(SUB_TITULO2_1, unsafe_allow_html=True)
    st.write("O objeto ***cout***, junto com o operador **<<**, é usado para exibir valores/texto de exibição:")  
    st.code("""
    //Diferentes utilizações do cout
    #include <iostream>
    using namespace std;
    int main()
    {
        cout<< "Texto a exibir";
        cout<< "5";
        cout<< 5;
        cout<< 5+2;
        return 0;
    }
    """)
    
    SUB_TITULO2_2 = '<p style="font-family:tahoma; color:Black; font-size: 26px;">2.2 - VARIÁVEIS</p>'
    st.markdown(SUB_TITULO2_2, unsafe_allow_html=True)
    st.write("Variáveis ​​são contêineres usados para armazenar valores de dados.")
    st.write("Em C++, existem diferentes tipos de variáveis ​​(definidas com diferentes palavras-chave), por exemplo:")
    st.info("""
    - ***int*** armazena inteiros (números inteiros), sem decimais, como 123 ou -123
    - ***float*** armazena números de ponto flutuante com até 7 dígitos significativos, como 3.141592 ou -3.141592
    - ***double*** armazena números de ponto flutuante com até 15 dígitos significativos, como 3.1415926535897932 ou -3.1415926535897932
    - ***char*** armazena caracteres únicos, como 'a' ou 'B'. Os valores de caractere são cercados por aspas simples
    - ***string*** armazena texto, como "Hello World". Os valores de string são cercados por aspas duplas
    - ***bool*** armazena valores com dois estados: verdadeiro(1) ou falso(0)
    
    ##### Para criar uma variável, especifique o tipo e atribua um valor a ela:
    """)
    
    st.write(" #### SINTAXE: ")      
    st.warning("***type*** **variableName** = value;")       
    st.write("Onde ***type*** é um dos tipos C++ (como int) e variableName é o nome da variável (como x ou myName ). O sinal de igual é usado para atribuir valores à variável. Para criar uma variável que deve armazenar um número, veja o exemplo a seguir:")
    
    st.write("### Exemplo2.2.1:") 
    st.write("""
    Crie uma variável chamada v1 do tipo INT e atribua a ela o valor 5 [:arrow_forward:](https://replit.com/@MassakiIgarash1/0221AtribuindoValornaVariavel?v=1)
    """)    
    st.code("""
    //Atribuindo valor à variável já no momento da sua declaração
    #include <iostream>
    using namespace std;
    int main()
    {
        int v1 = 5;
        cout<< v1;
        return 0;
    }
    """)
    
    st.write("""
    Você também pode declarar uma variável sem atribuir o valor e atribuir o valor posteriormente: [:arrow_forward:](https://replit.com/@MassakiIgarash1/0222AtribuindoValornaVariavel?v=1)
    """)    

    st.code("""
    //Atribuindo valor à variável após sua declaração
    #include <iostream>
    using namespace std;
    int main()
    {
        int v1;
        v1 = 5;
        cout<< v1;
        return 0;
    }
    """)
    st.write("""
    Mas é **IMPORTANTE** você saber também que, se você atribuir um novo valor a uma variável existente, ele substituirá o valor anterior:
    [:arrow_forward:](https://replit.com/@MassakiIgarash1/0223AtribuindoValornaVariaveleModificando?v=1)
    """)      
    st.code("""
    //Modificando valor de variável mesmo após atribuição inicial
    #include <iostream>
    using namespace std;
    int main()
    {
        int v1 = 5;
        v1 = 10;
        cout<< v1;
        return 0;
    }
    """)
    
    st.write(" #### Outros tipos de dados: ") 
    st.info("""
    ###### **int** Num = 5;               // Valor inteiro sem casas decimais
    ###### **double** FloatNum = 5.99;    // número com ponto flutuante (com casas decimais)
    ###### **char** Letter = 'D';         // Caracteres
    ###### **string** Texto = "Hello";    // Texto
    ###### **bool** Boolean = true;       // Booleano, Verdadeiro (1) ou Falso (0)
    """)   
    
    SUB_TITULO2_3 = '<p style="font-family:tahoma; color:Black; font-size: 26px;">2.3 - ENTRADA DE DADOS (Valor digitado com o teclado).</p>'
    st.markdown(SUB_TITULO2_3, unsafe_allow_html=True)
    st.write("Você já aprendeu que ***cout*** é usado para exibir valores na tela. Agora vamos usar ***cin*** para obter a entrada do usuário. ***cin*** é um objeto usado com uma variável para ler os dados digitados com o teclado; vem sempre junto ao operador de extração (>>).")
    st.write("No exemplo a seguir, o usuário pode inserir um número, que é armazenado na variável x. Em seguida, exibir o valor de x:")  
    st.write("""
    #### Exemplo 02.3.1 [:arrow_forward:](https://replit.com/@MassakiIgarash1/0231EntradadedadoscomCIN?v=1)
    """) 
    st.code("""
    //Exemplo de inserção de dados a partir do teclado com o comando cin
    #include <iostream>
    using namespace std;
    int main()
    {
        int x;
        cout<< "Insira o valor: ";
        cin >> x;
        cout<< "O valor inserido é = " << x;
        return 0;
    }
    """)
    
    st.write("## Tipos de dados")
    st.write("O tipo de dados especifica o tamanho alocado na memória e o tipo de informação que a variável armazenará:")
    st.info("""
    TIPO DE DADO | ESPAÇO ALOCADO | DESCRIÇÃO
    :---------: | :------: | :-------
    boolean	    | 1 byte  | Armazena Verdadeiro (1) ou Falso (0)
    char	    | 1 byte  | Armazena caracter/Letra/Número, or Valores ASCII {-128,..., -1, 0, 1,..., 127}
    int	        | 4 bytes | Armazena números inteiros {-2147483648,..., -1, 0, 1,..., 2147483648} 
    float	    | 4 bytes |	Armazena números decimais com até 7 dígitos significativos
    double	    | 8 bytes |	Armazena números decimais com até 15 dígitos significativos
    long double	| 10 bytes|	Armazena números decimais com até 19 dígitos significativos
    void        |    -    | Não representa valor, usado em FUNÇÕES sem retorno
    """)

    st.header('CAP 03')
    st.header("OPERADORES E OPERAÇÕES BÁSICAS")
    SUB_TITULO3_1 = '<p style="font-family:tahoma; color:Black; font-size: 26px;">3.1 - OPERADORES NO C++.</p>'
    st.markdown(SUB_TITULO3_1, unsafe_allow_html=True)
    st.write("Os operadores são usados ​​para realizar operações em variáveis ​​e valores")    
    st.write("##### C++ divide os operadores nos seguintes grupos:") 
    st.info("""
    - [Aritmeticos](#aritmeticos)
    - [Atribuicao](#atribuicao)
    - [Comparacao](#comparacao)
    - [Logicos](#logicos)
    - [Bit-a-Bit](#bit-a-bit)
    """)
    st.header('Aritmeticos') 
    st.write("Operadores aritméticos são usados ​​para realizar operações matemáticas comuns.")

    st.info("""
    OPERAÇÃO            | OPERADOR       | DESCRIÇÃO | EXEMPLO
    :-----------        | :--:| :-------- |:-----:
    ADIÇÃO              | +   | AdIciona um valor y a x                   | x + y
    SUBTRAÇÃO-          | -   | Subtrai um valor y de x                   | x - y
    MULTIPLICAÇÃO       | *   | Multiplica dois valores                   | x * y
    DIVISÃO             | /   | Fraciona ou divide um valor y por y       | x / y
    RESTO               | %   | Retorna o resto de uma divisão de x por y | x % y
    INCREMENTO UNITÁRIO | ++  | Incrementa 1 unidade no valor da variável | x++
    DECREMENTO UNITÁRIO | --  | Decrementa 1 unidade no valor da variável | x--
    """)
    st.header('Atribuicao')
    st.header('Comparacao')
    st.header('Logicos')
    st.header('Bit-a-Bit')
   
    st.title("BIBLIOGRAFIA")
    st.subheader("**Bibliografia Básica**")
    st.image(image1, width=200, caption='Bibliografia Básica')    
    st.write("- PAMBOUKIAN, Sérgio V. D.; ZAMBONI, Lincoln C.; BARROS, Edson A. R. Aplicações Científicas em C++. 4. ed. São Paulo: Páginas & Letras, 2015. V1. 230 p.")
    
    st.write("**Bibliografia Complementar**")
    st.image(image2, width=700, caption='Bibliografia Complementar')
    st.write("- CAPRON, Harriet L.; JOHNSON, J. A. Introdução à informática. 8. ed. São Paulo: Pearson/Prentice Hall, 2008.")
    st.write("- DEITEL, Harvey M.; DEITEL, Paul J. C++: como programar. 5. ed. São Paulo: Pearson Prentice Hall, 2008. 1163 p.")
    st.write("- HORSTMANN, Cay. Conceitos de computação com o essencial de C++. Tradução: Carlos A. L. Lisbôa e Maria Lúcia B. Lisbôa. Porto Alegre: Bookman Editora (Grupo A), 2005.p.36; p.157-199.Disponível em: < https://integrada.minhabiblioteca.com.br/#/books/9788577801770/pageid/155>")
    st.write("- JOYANES AGUILAR, Luis. Programação em C++: algoritmos, estruturas de dados e objetos. 2. ed. São Paulo: McGraw-Hill, 2008. 768 p.")
    st.write("- MIZRAHI, Victorine Viviane. Treinamento em linguagem C++: módulo 1. 2. ed. São Paulo: Pearson Prentice Hall, 2009. 234 p.")
    st.write("- MIZRAHI, Victorine Viviane. Treinamento em linguagem C++: módulo 2. 2. ed. São Paulo: Pearson Prentice Hall, 2009. 309 p.")
    st.write("- SAVITCH, Walter J. C++ absoluto. São Paulo: Pearson/Addison Wesley, 2004. 612 p.")
    st.write("- STROUSTRUP, B. The C++ programming language. Special ed., 12th printing Boston: Addison-Wesley, 2005.")
   
# Security
#passlib,hashlib,bcrypt,scrypt

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
	"""Simple Login App"""

	st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

	menu = ["Cursos",
            "Admin",
            "Contato",
            #"SignUp"
            ]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Cursos":       
		st.subheader("ACESSO RESTRITO (em desenvolvimento): \n Preencha os dados abaixo:")
	elif choice == "Admin":
		st.subheader("Login Section")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')        
		if st.sidebar.checkbox("Logar!"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				task = st.selectbox("Task",["Add Post","PERFIL","Panorama_INSCRITOS"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "PERFIL":
					st.subheader("PERFIL DE USUÁRIO \n Linha 01 - Texto do perfil.")
				elif task == "Panorama_INSCRITOS":
					st.subheader(str(curso))                    
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					#st.dataframe(clean_db)                    
			else:
				st.warning("Incorrect Username/Password") 
	elif choice == "Contato":
		st.subheader("Massaki de O. Igarashi / e-mail: prof.massaki@gmail.com")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

if __name__ == '__main__':
	main()
