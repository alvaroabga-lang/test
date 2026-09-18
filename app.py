import streamlit as st
import json
import os

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Oposición Subalterno de Cádiz",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Oposición Subalterno de Cádiz")
st.write("Estudia el temario y practica con tests.")
st.divider()


# ============================================================
# CARPETA DONDE ESTÁ app.py
# ============================================================

CARPETA_APP = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# FUNCIÓN PARA CARGAR JSON
# ============================================================

def cargar_json(ruta):
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)

        except json.JSONDecodeError:
            st.error(
                f"❌ El archivo '{ruta}' no tiene un JSON válido."
            )
            return None

        except Exception as e:
            st.error(
                f"❌ Error al abrir el archivo: {e}"
            )
            return None

    return None


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

seccion = st.radio(
    "¿Qué quieres hacer?",
    ["📖 TEMARIO", "📝 TESTS"],
    horizontal=True
)

st.divider()


# ============================================================
# =========================
#         TEMARIO
# =========================
# ============================================================

if seccion == "📖 TEMARIO":

    st.header("📖 Temario")

    # --------------------------------------------------------
    # LOS TEMAS ESTÁN EN LA MISMA CARPETA QUE app.py
    # --------------------------------------------------------

    archivos_temario = [
        archivo
        for archivo in os.listdir(CARPETA_APP)
        if archivo.lower().startswith("tema")
        and archivo.lower().endswith(".json")
    ]

    # Ordenar por número de tema
    def numero_tema(nombre):

        try:
            numero = (
                nombre.lower()
                .replace("tema", "")
                .replace(".json", "")
                .strip()
            )

            return int(numero)

        except ValueError:
            return 9999

    archivos_temario.sort(key=numero_tema)

    # --------------------------------------------------------
    # SI NO HAY TEMAS
    # --------------------------------------------------------

    if not archivos_temario:

        st.warning(
            "⚠️ No se han encontrado archivos de temas."
        )

        st.info(
            "Los archivos deben estar en la misma carpeta que "
            "app.py.\n\n"
            "Por ejemplo:\n\n"
            "app.py\n"
            "tema1.json\n"
            "tema2.json\n"
            "tema3.json"
        )

    else:

        # ----------------------------------------------------
        # CREAR NOMBRES PARA EL SELECTOR
        # ----------------------------------------------------

        nombres_temas = {}

        for archivo in archivos_temario:

            numero = (
                archivo.lower()
                .replace("tema", "")
                .replace(".json", "")
                .strip()
            )

            nombres_temas[
                f"📖 Tema {numero}"
            ] = archivo

        # ----------------------------------------------------
        # SELECCIONAR TEMA
        # ----------------------------------------------------

        tema_seleccionado = st.selectbox(
            "Selecciona un tema:",
            list(nombres_temas.keys())
        )

        archivo_tema = nombres_temas[
            tema_seleccionado
        ]

        # Ruta completa al JSON
        ruta_tema = os.path.join(
            CARPETA_APP,
            archivo_tema
        )

        # ----------------------------------------------------
        # CARGAR TEMA
        # ----------------------------------------------------

        contenido_tema = cargar_json(
            ruta_tema
        )

        if contenido_tema is not None:

            st.divider()

            # =================================================
            # SI EL JSON ES UN OBJETO
            # =================================================

            if isinstance(contenido_tema, dict):

                titulo = contenido_tema.get(
                    "titulo",
                    tema_seleccionado
                )

                st.header(titulo)

                contenido = contenido_tema.get(
                    "contenido",
                    ""
                )

                if contenido:
                    st.markdown(
                        contenido
                    )

                apartados = contenido_tema.get(
                    "apartados",
                    []
                )

                for apartado in apartados:

                    if isinstance(
                        apartado,
                        dict
                    ):

                        titulo_apartado = apartado.get(
                            "titulo",
                            "Apartado"
                        )

                        texto_apartado = apartado.get(
                            "contenido",
                            ""
                        )

                        with st.expander(
                            f"📌 {titulo_apartado}",
                            expanded=True
                        ):

                            st.markdown(
                                texto_apartado
                            )

            # =================================================
            # SI EL JSON ES UNA LISTA
            # =================================================

            elif isinstance(
                contenido_tema,
                list
            ):

                for i, apartado in enumerate(
                    contenido_tema
                ):

                    if isinstance(
                        apartado,
                        dict
                    ):

                        titulo_apartado = apartado.get(
                            "titulo",
                            f"Apartado {i + 1}"
                        )

                        texto_apartado = apartado.get(
                            "contenido",
                            ""
                        )

                        with st.expander(
                            f"📌 {titulo_apartado}",
                            expanded=True
                        ):

                            st.markdown(
                                texto_apartado
                            )

                    else:

                        st.markdown(
                            str(apartado)
                        )


# ============================================================
# =========================
#          TESTS
# ============================
# ============================================================

else:

    st.header("📝 Tests")

    st.write(
        "Selecciona un examen y responde las preguntas."
    )

    # --------------------------------------------------------
    # TESTS DISPONIBLES
    # --------------------------------------------------------

    opciones_test = {

        "Test 1: Constitución Española (20 preguntas)":
            "test1.json",

        "Test 2: Constitución Española (20 preguntas)":
            "test2.json",

        "Test 3: Constitución Española (20 preguntas)":
            "test3.json",

        "Test 4: Constitución Española (20 preguntas)":
            "test4.json",

        "Test 5: Constitución Española (20 preguntas)":
            "test5.json"
    }

    test_seleccionado = st.selectbox(
        "¿Qué examen quieres hacer?",
        options=list(
            opciones_test.keys()
        ),
        key="selector_global_test"
    )

    archivo_json = opciones_test[
        test_seleccionado
    ]

    # --------------------------------------------------------
    # RUTA COMPLETA DEL TEST
    # --------------------------------------------------------

    ruta_test = os.path.join(
        CARPETA_APP,
        archivo_json
    )

    # --------------------------------------------------------
    # CARGAR TEST
    # --------------------------------------------------------

    cuestionario = cargar_json(
        ruta_test
    )

    if cuestionario is None:

        st.error(
            f"❌ No se encontró el archivo "
            f"'{archivo_json}'."
        )

        st.info(
            "Los archivos test1.json, test2.json, "
            "test3.json, test4.json y test5.json "
            "deben estar en la misma carpeta que app.py."
        )

        st.stop()

    # --------------------------------------------------------
    # COMPROBAR QUE EL TEST ES UNA LISTA
    # --------------------------------------------------------

    if not isinstance(
        cuestionario,
        list
    ):

        st.error(
            "❌ El archivo del test debe contener "
            "una lista de preguntas."
        )

        st.stop()

    # --------------------------------------------------------
    # ESTADO DEL TEST
    # --------------------------------------------------------

    if "test_enviado" not in st.session_state:

        st.session_state.test_enviado = False

    if "intento" not in st.session_state:

        st.session_state.intento = 1

    # --------------------------------------------------------
    # DETECTAR CAMBIO DE TEST
    # --------------------------------------------------------

    if "ultimo_test" not in st.session_state:

        st.session_state.ultimo_test = archivo_json

    elif (
        st.session_state.ultimo_test
        != archivo_json
    ):

        st.session_state.test_enviado = False

        st.session_state.intento += 1

        st.session_state.ultimo_test = (
            archivo_json
        )

    # --------------------------------------------------------
    # FUNCIÓN PARA REINICIAR
    # --------------------------------------------------------

    def reiniciar_test():

        st.session_state.test_enviado = False

        st.session_state.intento += 1

        for key in list(
            st.session_state.keys()
        ):

            if key.startswith(
                "pregunta_"
            ):

                del st.session_state[key]

    # --------------------------------------------------------
    # RESPUESTAS DEL USUARIO
    # --------------------------------------------------------

    respuestas_usuario = {}

    # --------------------------------------------------------
    # MOSTRAR PREGUNTAS
    # --------------------------------------------------------

    st.info(
        f"📋 Cargadas {len(cuestionario)} preguntas"
    )

    st.divider()

    for item in cuestionario:

        st.subheader(
            f"Pregunta {item['id']}: "
            f"{item['pregunta']}"
        )

        clave_dinamica = (
            f"pregunta_{archivo_json}_"
            f"{item['id']}_"
            f"int_{st.session_state.intento}"
        )

        opcion_elegida = st.radio(

            "Selecciona tu respuesta:",

            options=item["opciones"],

            key=clave_dinamica,

            index=None,

            disabled=(
                st.session_state.test_enviado
            )
        )

        respuestas_usuario[
            item["id"]
        ] = opcion_elegida

        # ----------------------------------------------------
        # CORREGIR PREGUNTA
        # ----------------------------------------------------

        if st.session_state.test_enviado:

            indice_correcto = (
                ord(
                    item[
                        "respuesta_correcta"
                    ]
                )
                - ord("A")
            )

            respuesta_correcta_texto = (
                item["opciones"][
                    indice_correcto
                ]
            )

            if (
                opcion_elegida
                == respuesta_correcta_texto
            ):

                st.success(
                    "✅ ¡Correcto! "
                    f"Tu respuesta: "
                    f"{opcion_elegida}"
                )

            else:

                st.error(
                    "❌ Incorrecto. "
                    "Tu respuesta: "
                    f"{opcion_elegida if opcion_elegida else 'Dejada en blanco'}"
                )

                st.info(
                    "💡 La respuesta correcta es: "
                    f"**{respuesta_correcta_texto}**"
                )

        st.divider()

    # ========================================================
    # TERMINAR Y CALIFICAR
    # ========================================================

    if not st.session_state.test_enviado:

        if st.button(
            "🏁 Terminar y Calificar",
            type="primary"
        ):

            if None in respuestas_usuario.values():

                st.warning(
                    "⚠️ Todavía te quedan preguntas "
                    "por responder. "
                    "¡No dejes ninguna en blanco!"
                )

            else:

                st.session_state.test_enviado = True

                st.rerun()

    # ========================================================
    # RESULTADOS
    # ========================================================

    else:

        aciertos = 0

        total_preguntas = len(
            cuestionario
        )

        for item in cuestionario:

            indice_correcto = (
                ord(
                    item[
                        "respuesta_correcta"
                    ]
                )
                - ord("A")
            )

            respuesta_correcta_texto = (
                item["opciones"][
                    indice_correcto
                ]
            )

            if (
                respuestas_usuario[
                    item["id"]
                ]
                == respuesta_correcta_texto
            ):

                aciertos += 1

        # ----------------------------------------------------
        # NOTA
        # ----------------------------------------------------

        nota_sobre_10 = round(
            (
                aciertos
                / total_preguntas
            ) * 10,
            2
        )

        porcentaje = (
            aciertos
            / total_preguntas
        )

        # ----------------------------------------------------
        # MOSTRAR RESULTADO
        # ----------------------------------------------------

        st.divider()

        st.header(
            "📊 Resultado del Examen"
        )

        st.success(
            f"🎯 Aciertos: {aciertos} "
            f"de {total_preguntas}"
        )

        st.metric(
            label="Nota Final",
            value=f"{nota_sobre_10} / 10"
        )

        st.progress(
            porcentaje
        )

        if nota_sobre_10 >= 5:

            st.write(
                "👍 ¡Buen trabajo! "
                "Has aprobado el test."
            )

        else:

            st.write(
                "📚 Necesitas repasar un poco más. "
                "¡Inténtalo de nuevo!"
            )

        st.divider()

        # ----------------------------------------------------
        # REINICIAR
        # ----------------------------------------------------

        if st.button(
            "🔄 Reiniciar este test",
            type="secondary"
        ):

            reiniciar_test()

            st.rerun()
