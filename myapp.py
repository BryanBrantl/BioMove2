import streamlit as st
import base64


# Título ou seção
st.markdown("## Projeto")
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])


# Carrega o arquivo de estilo customizado
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Vetor com os GIFs
gifs = ["image/gif3.gif", "image/gif3.gif", "image/gif3.gif"]

# Exibe os GIFs um a um com o estilo aplicado
for gif in gifs:
    with open(gif, "rb") as f:
        data = f.read()
        encoded_gif = base64.b64encode(data).decode("utf-8")

    st.markdown(
        f"""
        <div class="centered">
            <img src="data:image/gif;base64,{encoded_gif}" class="custom-img" alt="GIF">
        </div>
        """,
        unsafe_allow_html=True
    )

    
st.markdown("""
<div style="display: flex; align-items: center; margin: 20px 0;">
    <img src="data:image/gif;base64,{encoded_gif}" style="width: 150px; border-radius: 8px; margin-right: 20px;">
    <div>
        <h4 style="margin-bottom: 5px;">Título do GIF</h4>
        <p style="margin: 0;">Esse é um texto descritivo que explica o que está acontecendo no GIF.</p>
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
