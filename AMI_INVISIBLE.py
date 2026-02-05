import streamlit as st
import random

st.set_page_config(page_title="AMIS INVISIBLES B1A Keyce", page_icon="🎁")

# --- ANIMATION CADEAUX ---
def pluie_de_cadeaux():
    gift_html = """
    <style>
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .gift { position: fixed; top: -5vh; font-size: 2rem; z-index: 9999; animation: falling linear infinite; }
    </style>
    """
    for i in range(30):
        left, dur, delay = random.randint(0, 95), random.uniform(2, 5), random.uniform(0, 4)
        gift_html += f'<div class="gift" style="left:{left}%; animation-duration:{dur}s; animation-delay:{delay}s;">🎁</div>'
    st.markdown(gift_html, unsafe_allow_html=True)

# --- LISTE OFFICIELLE ---
# J'ai bien écrit Astride ici !
participants = ["Astride", "Yasmine", "Josiane", "Debora", "Valdes", "Priscas"]

# On change la clé pour forcer Streamlit à oublier l'ancien tirage
CLE_STABLE = "B1A_KEYCE_FINAL_V1" 

def generer_tirage(liste, graine):
    noms = sorted(liste.copy())
    random.seed(graine)
    random.shuffle(noms)
    return {noms[i]: noms[(i + 1) % len(noms)] for i in range(len(noms))}

tirage_final = generer_tirage(participants, CLE_STABLE)

# --- AFFICHAGE ---
st.title("🎁 AMIS INVISIBLES B1A Keyce")
nom_choisi = st.selectbox("Qui es-tu ?", [""] + sorted(participants))

if nom_choisi:
    if st.button("Découvrir mon ami invisible"):
        pluie_de_cadeaux()
        cible = tirage_final[nom_choisi]
        st.write(f"### 🤫 {nom_choisi}, ton ami invisible est...")
        st.header(f"✨ {cible} ✨")
        st.balloons()
