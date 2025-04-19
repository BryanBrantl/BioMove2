import streamlit as st
import os

st.set_page_config(page_title="Projeto BioMove", layout="wide")

# Estilo customizado para dark mode e centralização
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .custom-section {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            gap: 50px;
            padding: 40px 20px;
        }
        .custom-gif {
            max-width: 200px;
            border-radius: 10px;
            box-shadow: 0 0 10px #00ffff55;
        }
        .custom-text {
            max-width: 600px;
            font-size: 18px;
            line-height: 1.6;
            text-align: justify;
        }
        .custom-text strong {
            color: #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

with abas[0]:
    st.title("BioMove – Carrinho Controlado por Sinais EMG para Fisioterapia Interativa")

    st.markdown("""
        <div class="custom-section">
            <img src="image/gif3.gif" class="custom-gif" alt="GIF de sinal EMG">
            <div class="custom-text">
                <p><strong>O BioMove</strong> é um sistema terapêutico interativo que utiliza sinais EMG (eletromiográficos)
                para controlar os movimentos de um carrinho robô. O objetivo principal é oferecer uma forma <strong>lúdica</strong> 
                e <strong>engajadora</strong> de fisioterapia muscular, especialmente para pacientes em <strong>reabilitação motora</strong>.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


    

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
