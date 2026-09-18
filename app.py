import streamlit as st
import json
import os

# 1. Configuración de la página web
st.set_page_config(page_title="Mi Banco de Tests", page_icon="📚", layout="centered")

st.title("📚 Mi Tests para oposicion subalterno de Cadiz")
st.write("Selecciona el examen que deseas realizar en el menú de abajo.")
st.divider()

# --- NUEVO: MENÚ DE SELECCIÓN DE TEST ---
# Aquí defines el nombre que se ve en la pantalla y qué archivo JSON le corresponde
opciones_test = {
    "Test 1: Constitución Española (20 preguntas)": "test1.json",
    "Test 2: Constitución Española (20 preguntas)": "test2.json",
    "Test 3: Constitución Española (20 preguntas)": "test3.json",
    "Test 4: Constitución Española (20 preguntas)": "test4.json",
    "Test 5: Constitución Española (20 preguntas)": "test5.json"
}

# Creamos el selector visual al inicio de la página
test_seleccionado = st.selectbox(
    "¿Qué examen quieres hacer hoy?",
    options=list(opciones_test.keys()),
    key="selector_global_test"
)

# Obtenemos el nombre del archivo del test elegido
archivo_json = opciones_test[test_seleccionado]

# --- FIN DEL MENÚ ---

# 2. Cargar las preguntas desde el archivo JSON seleccionado
def cargar_preguntas(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        st.error(f"❌ No se encontró el archivo '{nombre_archivo}'. Asegúrate de crearlo en la misma carpeta.")
        return []

# Pasamos el archivo del test elegido por el usuario
cuestionario = cargar_preguntas(archivo_json)

# 3. Inicializar el estado del test (Memoria de la aplicación)
if "test_enviado" not in st.session_state:
    st.session_state.test_enviado = False

if "intento" not in st.session_state:
    st.session_state.intento = 1

# Si el usuario cambia de test en el menú, reiniciamos el estado para que empiece limpio
if "ultimo_test" not in st.session_state:
    st.session_state.ultimo_test = archivo_json
elif st.session_state.ultimo_test != archivo_json:
    st.session_state.test_enviado = False
    st.session_state.intento += 1
    st.session_state.ultimo_test = archivo_json

def reiniciar_test():
    st.session_state.test_enviado = False
    st.session_state.intento += 1
    for key in list(st.session_state.keys()):
        if key.startswith("pregunta_"):
            del st.session_state[key]

# 4. Estructura para guardar las respuestas
respuestas_usuario = {}

# 5. Mostrar las preguntas dinámicamente
if cuestionario:
    st.info(f"📋 Cargadas {len(cuestionario)} preguntas de: {test_seleccionado}")
    st.divider()
    
    for item in cuestionario:
        st.subheader(f"Pregunta {item['id']}: {item['pregunta']}")
        
        # Clave dinámica que incluye el nombre del archivo para que no se mezclen las respuestas
        clave_dinamica = f"pregunta_{archivo_json}_{item['id']}_int_{st.session_state.intento}"
        
        opcion_elegida = st.radio(
            "Selecciona tu respuesta:",
            options=item["opciones"],
            key=clave_dinamica,
            index=None,
            disabled=st.session_state.test_enviado
        )
        
        respuestas_usuario[item["id"]] = opcion_elegida
        
        if st.session_state.test_enviado:
            if opcion_elegida == item["correcta"]:
                st.success(f"✅ ¡Correcto! Tu respuesta: {opcion_elegida}")
            else:
                st.error(f"❌ Incorrecto. Tu respuesta: {opcion_elegida if opcion_elegida else 'Dejada en blanco'}")
                st.info(f"💡 La respuesta correcta es: **{item['correcta']}**")
                
        st.divider()

    # 6. Zona de calificación y reinicio
    if not st.session_state.test_enviado:
        if st.button("Terminar y Calificar", type="primary"):
            if None in respuestas_usuario.values():
                st.warning("⚠️ Todavía te quedan preguntas por responder. ¡No dejes ninguna en blanco!")
            else:
                st.session_state.test_enviado = True
                st.rerun() 
                
    else:
        aciertos = 0
        total_preguntas = len(cuestionario)
        
        for item in cuestionario:
            if respuestas_usuario[item["id"]] == item["correcta"]:
                aciertos += 1
        
        nota_sobre_10 = round((aciertos / total_preguntas) * 10, 2)
        porcentaje = (aciertos / total_preguntas)
        
        st.subheader("📊 Resultado del Examen")
        st.success(f"🎯 Aciertos: {aciertos} de {total_preguntas} correctas.")
        st.metric(label="Nota Final", value=f"{nota_sobre_10} / 10") 
        st.progress(porcentaje)
        
        if nota_sobre_10 >= 5.0:
            st.write("👍 ¡Buen trabajo! Has aprobado el test.")
        else:
            st.write("📚 Necesitas repasar un poco más. ¡Inténtalo de nuevo!")
            
        st.divider()
        
        if st.button("🔄 Reiniciar este test", type="secondary"):
            reiniciar_test()
            st.rerun()
