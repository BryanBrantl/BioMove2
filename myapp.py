import streamlit as st

# Título ou seção
st.markdown("## Interativa")

# Estilo customizado
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .custom-img {
        border-radius: 12px;
        box-shadow: 0 0 15px #54FF9F;
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# Pré-carregamento da imagem (para garantir que apareça corretamente)
st.image("image/gif3.gif", caption="(Pré-carregamento do GIF)", use_container_width=False)

# Exibição estilizada do GIF com HTML

# Texto descritivo
st.markdown("""
<p style="text-align: justify;">
<b>O BioMove</b> é um sistema terapêutico interativo que utiliza sinais EMG (eletromiográficos) para controlar os movimentos de um carrinho robô. O objetivo principal é oferecer uma forma <span style="color:#54FF9F;">lúdica</span> e <span style="color:#54FF9F;">engajadora</span> de fisioterapia muscular, especialmente para pacientes em <span style="color:#54FF9F;">reabilitação motora</span>.
</p>
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
