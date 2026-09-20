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
# CONFIGURACIÓN DEL TEMARIO
# ============================================================
# AQUÍ PUEDES AÑADIR, QUITAR O CAMBIAR TEMAS
#
# "Nombre que verá el usuario": "archivo.json"
#
# El archivo JSON debe estar en la misma carpeta que app.py.
# ============================================================

opciones_temario = {

    "Tema 1: Constitución Española":
        "tema1.json",

    "Tema 2: Igualdad, discriminación y violencia de género":
        "tema2.json",

    "Tema 3: Prevención de Riesgos Laborales":
        "tema3.json",

    "Tema 4: Atención al ciudadano":
        "tema4.json",

    "Tema 5: La notificación administrativa ":
        "tema5.json",

    "Tema 6: El Ayuntamiento de Cádiz":
        "tema6.json",

    "Tema 7: El archivo":
        "tema7.json",

    "Tema 8: Aritmética y lenguaje administrativo":
        "tema8.json",

    "Tema 9: Ofimática":
        "tema9.json",

    "Tema 10: La ciudad de Cádiz":
        "tema10.json",

}


# ============================================================
# CONFIGURACIÓN DE LOS TESTS
# ============================================================
# AQUÍ PUEDES AÑADIR, QUITAR O CAMBIAR TESTS
#
# "Nombre que verá el usuario": "archivo.json"
# ============================================================

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
        "test5.json",

    "Test 6: Igualdad, discriminación y violencia de género (20 preguntas)":
        "test6.json",
    
    "Test 7: Igualdad, discriminación y violencia de género (20 preguntas)":
        "test7.json",
    
    "Test 8: Igualdad, discriminación y violencia de género (20 preguntas)":
        "test8.json",
    
    "Test 9: Igualdad, discriminación y violencia de género (20 preguntas)":
        "test9.json",
    
    "Test 10: Igualdad, discriminación y violencia de género (20 preguntas)":
        "test10.json",

    "Test 11: Prevención de riesgos laborales (20 preguntas)":
        "test11.json",        

    "Test 12: Prevención de riesgos laborales (20 preguntas)":
        "test12.json",

    "Test 13: Prevención de riesgos laborales (20 preguntas)":
        "test13.json",

    "Test 14: Prevención de riesgos laborales (20 preguntas)":
        "test14.json",

    "Test 15: Prevención de riesgos laborales (20 preguntas)":
        "test15.json",          

    "Test 16: Atención al ciudadano (20 preguntas)":
        "test16.json",

"Test 17: Atención al ciudadano (20 preguntas)":
        "test17.json", 

"Test 18: Atención al ciudadano (20 preguntas)":
        "test18.json", 

"Test 19: Atención al ciudadano (20 preguntas)":
        "test19.json", 

"Test 20: Atención al ciudadano (20 preguntas)":
        "test20.json",

"Test 21: La notificación administrativa (20 preguntas)":
        "test21.json", 

"Test 22: La notificación administrativa (20 preguntas)":
        "test22.json",

"Test 23: La notificación administrativa (20 preguntas)":
        "test23.json",

"Test 24: La notificación administrativa (20 preguntas)":
        "test24.json",

"Test 25: La notificación administrativa (20 preguntas)":
        "test25.json", 

"Test 26: El Ayuntamiento de Cádiz (20 preguntas)":
        "test26.json",

"Test 27: El Ayuntamiento de Cádiz (20 preguntas)":
        "test27.json",

"Test 28: El Ayuntamiento de Cádiz (20 preguntas)":
        "test28.json",

"Test 29: El Ayuntamiento de Cádiz (20 preguntas)":
        "test29.json",

"Test 30: El Ayuntamiento de Cádiz (20 preguntas)":
        "test30.json",

"Test 31: El archivo (20 preguntas)":
        "test31.json", 

"Test 32: El archivo (20 preguntas)":
        "test32.json", 

"Test 33: El archivo (20 preguntas)":
        "test33.json", 

"Test 34: El archivo (20 preguntas)":
        "test34.json", 

"Test 35: El archivo (20 preguntas)":
        "test35.json", 

"Test 36: Aritmética y lenguaje administrativo (20 preguntas)":
        "test36.json",

"Test 37: Aritmética y lenguaje administrativo (20 preguntas)":
        "test37.json",

"Test 38: Aritmética y lenguaje administrativo (20 preguntas)":
        "test38.json",

"Test 39: Aritmética y lenguaje administrativo (20 preguntas)":
        "test39.json",

"Test 40: Aritmética y lenguaje administrativo (20 preguntas)":
        "test40.json",

"Test 41: Ofimática (20 preguntas)":
        "test41.json",

"Test 42: Ofimática (20 preguntas)":
        "test42.json",

"Test 43: Ofimática (20 preguntas)":
        "test43.json",

"Test 44: Ofimática (20 preguntas)":
        "test44.json",

"Test 45: Ofimática (20 preguntas)":
        "test45.json",

"Test 46: La ciudad de Cádiz (20 preguntas)":
        "test46.json",  

"Test 47: La ciudad de Cádiz (20 preguntas)":
        "test47.json",

"Test 48: La ciudad de Cádiz (20 preguntas)":
        "test48.json",

"Test 49: La ciudad de Cádiz (20 preguntas)":
        "test49.json",

"Test 50: La ciudad de Cádiz (20 preguntas)":
        "test50.json",                                      
}


# ============================================================
# FUNCIÓN PARA CARGAR JSON
# ============================================================

def cargar_json(ruta):

    if os.path.exists(ruta):

        try:

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except json.JSONDecodeError:

            st.error(
                f"❌ El archivo '{ruta}' "
                f"no tiene un JSON válido."
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
# ============================================================
#                         TEMARIO
# ============================================================
# ============================================================

if seccion == "📖 TEMARIO":

    st.header("📖 Temario")

    st.write(
        "Selecciona el tema que quieres estudiar."
    )

    # --------------------------------------------------------
    # COMPROBAR SI HAY TEMAS
    # --------------------------------------------------------

    if not opciones_temario:

        st.warning(
            "⚠️ No hay temas configurados."
        )

        st.info(
            "Añade los temas en la variable "
            "'opciones_temario' al principio del programa."
        )

    else:

        # ----------------------------------------------------
        # SELECTOR DE TEMAS
        # ----------------------------------------------------

        tema_seleccionado = st.selectbox(
            "Selecciona un tema:",
            options=list(
                opciones_temario.keys()
            ),
            key="selector_temario"
        )

        # ----------------------------------------------------
        # OBTENER ARCHIVO DEL TEMA
        # ----------------------------------------------------

        archivo_tema = opciones_temario[
            tema_seleccionado
        ]

        # ----------------------------------------------------
        # RUTA COMPLETA
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # SI NO SE ENCUENTRA EL ARCHIVO
        # ----------------------------------------------------

        if contenido_tema is None:

            st.error(
                f"❌ No se encontró el archivo "
                f"'{archivo_tema}'."
            )

            st.info(
                "Comprueba que el archivo esté en la "
                "misma carpeta que app.py."
            )

        else:

            st.divider()

            # =================================================
            # SI EL JSON ES UN OBJETO
            # =================================================

            if isinstance(
                contenido_tema,
                dict
            ):

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

            else:

                st.error(
                    "❌ El formato del archivo JSON "
                    "no es válido."
                )


# ============================================================
# ============================================================
#                          TESTS
# ============================================================
# ============================================================

else:

    st.header("📝 Tests")

    st.write(
        "Selecciona un examen y responde las preguntas."
    )

    # --------------------------------------------------------
    # COMPROBAR SI HAY TESTS
    # --------------------------------------------------------

    if not opciones_test:

        st.warning(
            "⚠️ No hay tests configurados."
        )

        st.info(
            "Añade los tests en la variable "
            "'opciones_test' al principio del programa."
        )

        st.stop()

    # --------------------------------------------------------
    # SELECTOR DE TEST
    # --------------------------------------------------------

    test_seleccionado = st.selectbox(
        "¿Qué examen quieres hacer?",
        options=list(
            opciones_test.keys()
        ),
        key="selector_global_test"
    )

    # --------------------------------------------------------
    # ARCHIVO DEL TEST
    # --------------------------------------------------------

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
            "Los archivos de los tests deben estar "
            "en la misma carpeta que app.py."
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
    # INFORMACIÓN DEL TEST
    # --------------------------------------------------------

    st.info(
        f"📋 Cargadas {len(cuestionario)} preguntas"
    )

    st.divider()

    # --------------------------------------------------------
    # MOSTRAR PREGUNTAS
    # --------------------------------------------------------

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