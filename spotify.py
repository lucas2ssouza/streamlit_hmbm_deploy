import pandas as pd
import streamlit as st
import os
from PIL import Image





#if "df_page1" not in st.session_state:
df= pd.read_csv('dataset/01 Spotify.csv')
st.session_state["df_page1"]= df


st.set_page_config(
    layout="wide",
    page_title="teste"

    )




GENERO= df['SEXO'].value_counts().index
SEXO=st.sidebar.selectbox("GENERO USUARIO",GENERO)
filtrar =st.checkbox('Filtrar')

CAMINHO="Z:\RH\Cargos e Salários\LUCAS\AUTOMAÇÕES\PYTHON\streamlit\imagem"

if filtrar:

    df= df[df['SEXO']==SEXO]

    st.write(SEXO)



USUARIO= df['NOME'].value_counts().index
USU=st.selectbox(" USUARIO",USUARIO)
df= df[df['NOME']==USU]
lista=["a",'b','c']
letra=st.radio("caixa",lista)
st.title(df['NOME'].iloc[0])
LOGRADOURO= df['LOGRADOURO'].iloc[0]

col1, col2 = st.columns(2)

col1.markdown("**logradouro:** {}".format(LOGRADOURO))



btn = st.button("SALVAR")
    

carregar_arquivo= st.file_uploader(
    "arquivo",type=['png', 'jpg','pdf']
    )
df
#=df_filtrado['novo_s']==letra
#print(df_filtrado)
try:
    img = Image.open(carregar_arquivo)
    img = img.convert("RGB")  # Converter para RGB se necessário
    st.image(img)
    
    if btn == True:
        salvar_arquivo(img,USU,"jpeg",CAMINHO)

        
    
    
    
    #salvar_arquivo(image,USU,"jpeg",CAMINHO)
except:
    pass

with st.sidebar:
    st.title(121)
    st.write(SEXO)

with st.form("my_form"):

    checkbox_val = st.radio("genero",lista)

    telefone = int(st.number_input("qual seu telefone"))
 

    st.form_submit_button()
st.write(telefone)
    

    #st.write[COLABORADOR]
    #carregar_arquivo= st.file_uploader("arquivo")

#img.save(f"Z:\RH\Cargos e Salários\LUCAS\AUTOMAÇÕES\PYTHON\streamlit\{SEXO}.jpg","JPEG")

