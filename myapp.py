import streamlit as st
import os

st.set_page_config(page_title="Projeto BioMove", layout="wide")

abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

with abas[0]:
    st.title("BioMove – Carrinho Controlado por Sinais EMG para Fisioterapia Interativa")

    colunas = st.columns(4)
    fotos = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]
    nomes = [
        ("Bryan A. L. Brantl", "2414139", "brantl@alunos.utfpr.edu.br", "(41) 99278-3929"),
        ("João Roberto Klassen", "2414XXX", "email@alunos.utfpr.edu.br", "41 992783929"),
        ("Leonardo Amancio", "240XXX", "email@alunos.utfpr.edu.br", "41 992783929"),
        ("Luiz Eduardo Prado de Oliveira", "2402629", "luizoliveira.2002@alunos.utfpr.edu.br", "(41) 99815-6532")
    ]

    for col, foto, (nome, ra, email, tel) in zip(colunas, fotos, nomes):
        with col:
            st.image(foto, width=500)
            st.markdown(f"""
                <div style='text-align: center;'>
                    <p><b>{nome}</b></p>
                    <p>RA: {ra}</p>
                    <p>Email: {email}</p>
                    <p>Contato: {tel}</p>
                </div>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("image/gif3.gif", caption="GIF 1", use_container_width=True)
    with col2:
        st.header("O BioMove é um sistema terapêutico interativo que utiliza sinais EMG (eletromiográficos) para controlar os "
                  "movimentos de um carrinho robô. O objetivo principal é oferecer uma forma lúdica e engajadora de fisioterapia muscular,"
                  "especialmente para pacientes em reabilitação motora.")


    

# Título e textos padrão
#st.title("🌈 Título com Emoji")
#st.header("Header com estilo normal")
#st.subheader("Subheader padrão")
#st.caption("Legenda/caption")

# Markdown com HTML para personalização
#st.markdown("""
### 🎨 Markdown com **negrito**, _itálico_ e `código`

#<p style='color:blue; font-size:20px;'>Texto azul com HTML</p>
#<p style='background-color:#ffeeba; padding:10px; border-radius:5px;'>
#Texto com fundo amarelo claro, bordas arredondadas e padding.
#</p>
#""", unsafe_allow_html=True)

# Caixas com destaque
#st.success("✅ Isso é uma mensagem de sucesso!")
#st.info("ℹ️ Isso é uma mensagem informativa.")
#st.warning("⚠️ Isso é um aviso.")
#st.error("❌ Isso é um erro.")

# Botão com estilo (usando HTML como workaround)
#st.markdown("""
#    <style>
#        .stButton>button {
#            color: white;
 #           background-color: #6a0dad;
  #          border-radius: 12px;
   #         height: 3em;
    #        width: 10em;
     #   }
   # </style>
#""", unsafe_allow_html=True)

#if st.button("Botão Estilizado"):
 #   st.write("Você clicou!")
#
# Customizar fonte e cor de fundo
#st.markdown("""
#<style>
#body {
 #   background-color: #f0f2f6;
  #  color: #333;
   # font-family: 'Arial', sans-serif;
#}
#</style>
#""", unsafe_allow_html=True)
