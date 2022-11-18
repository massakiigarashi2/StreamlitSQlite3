import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

from io import BytesIO
import requests

st.sidebar.markdown(
    """
    ### CONTEÚDO:
    - [**CAP 01**](#cap-01)
    ##### Tópico 01
    - [**CAP 02**](#cap-02)
    ##### Tópico 02
    - [**CAP 03**](#cap-03)
    ##### Tópico 03
    """, unsafe_allow_html=True)

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
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":books:")	
st.title("Prof. Massaki Igarashi")
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

st.markdown("""
#### ***Para referenciar este material:*** """)
st.warning("IGARASHI, Massaki de O. LINGUAGENS DE PROGRAMAÇÃO. Campinas - SP, 2022, v.1 01 de agosto de 2022. Disponível em: [link](endereço).")
    
task1 = st.selectbox("👈 Selecione a linguagem desejada:",
                    ["Linguagem de Programação C++"])                                  

if task1 == "Linguagem de Programação C++": 
    st.header('CAP 01')
    st.header("PRIMEIROS PASSOS")
   
    Texto01 = '<p style="font-family:tahoma; color:Blue; font-size: 18px;">A seguir, serão apresentados a você os 5 passos principais para você iniciar, rapidamente, a programar em C++. Espero que faça bom uso!</p>'
    st.markdown(Texto01, unsafe_allow_html=True)    
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Blue; font-size: 26px;">PASSO 01 - FERRAMENTAS NECESSÁRIAS</p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)

    cols02 = st.columns(1)
    cols02[0].write('Antes de iniciar você precisa saber que precisará de um compilador; este compilador pode ser instalado no seu desktop, no seu celular ou simplesmente executado ambiente de núvem da internet (esta última opção pode ser executada de qualquer plataforma, basta acessar o navegador de internet do seu dispositivo).')
    st.markdown(
    """
       
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
            "SignUp"
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
