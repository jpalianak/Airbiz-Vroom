import streamlit as st

# Definimos la clase para los nodos de decisión
class DecisionNode:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

# Función para construir el árbol de decisión del modelo Vroom-Yetton-Yago
def build_tree():
    # Nodos finales con estilos de liderazgo
    estilo_AI = "Autocrático I (AI)"
    estilo_AII = "Autocrático II (AII)"
    estilo_CI = "Consultivo I (CI)"
    estilo_CII = "Consultivo II (CII)"
    estilo_GII = "Grupo II (GII)"

    # Construyendo el árbol de decisión
    Q7B = DecisionNode("¿Es posible que haya conflictos entre los colaboradores respecto de diversas soluciones?", estilo_CI, estilo_CII)
    Q7A = DecisionNode("¿Es posible que haya conflictos entre los colaboradores respecto de diversas soluciones?", estilo_CII, estilo_GII)
    Q6B = DecisionNode("¿Están los miembros del equipo alineados con las metas a alcanzar?", estilo_GII, Q7B)
    Q6A = DecisionNode("¿Están los miembros del equipo alineados con las metas a alcanzar?", estilo_CII, Q7A)
    Q5C = DecisionNode("¿Si el líder toma la decisión, ¿está seguro que el equipo la aceptará?", estilo_AI, estilo_GII)
    Q5B = DecisionNode("¿Si el líder toma la decisión, ¿está seguro que el equipo la aceptará?", estilo_AI, Q6B)
    Q5A = DecisionNode("Si el líder toma la decisión, ¿está seguro que el equipo la aceptará?", estilo_AII, Q6B)
    Q4D = DecisionNode("¿Los miembros del equipo deben aceptar la decisión para que funcione?", Q5C, estilo_AI)
    Q4C = DecisionNode("¿Los miembros del equipo deben aceptar la decisión para que funcione?", Q5B, estilo_AI)
    Q4B = DecisionNode("¿Los miembros del equipo deben aceptar la decisión para que funcione?", Q5A, estilo_AII)
    Q4A = DecisionNode("¿Los miembros del equipo deben aceptar la decisión para que funcione?", Q6A, estilo_CII)
    Q3 = DecisionNode("¿Está el problema estructurado de forma que está claramente definido y organizado?", Q4B, Q4A)
    Q2 = DecisionNode("¿El líder tiene suficiente información para tomar una buena decisión por sí mismo?", Q4C, Q3)
    Q1 = DecisionNode("¿Es importante una alta calidad o es absolutamente crítica una buena solución?", Q2, Q4C)
    return Q1

# Función para manejar la navegación por el árbol de decisiones
def navigate_tree(node, response):
    if response == "Sí":
        return node.yes
    else:
        return node.no

# Configuración de la aplicación Streamlit
def main():
    st.title("Árbol de decisión de Vroom-Yetton-Yago")
    
    # Inicialización del estado de la sesión
    if 'node' not in st.session_state:
        st.session_state.node = build_tree()
        st.session_state.final_result = None
        st.session_state.next_question = st.session_state.node.question
        st.session_state.show_question = True
    
    if st.session_state.final_result:
        st.write(f"Estilo de liderazgo recomendado: {st.session_state.final_result}")
        st.session_state.show_question = False
    elif st.session_state.show_question:
        # Mostrar la pregunta actual
        st.write(f"Pregunta actual: {st.session_state.next_question}")
        
        # Opciones de respuesta
        response = st.radio("Selecciona una opción:", ["Sí", "No"], key="response")
        
        if st.button("Enviar"):
            st.write(f"Respuesta seleccionada: {response}")  # Mensaje de depuración
            # Actualizar el nodo actual basado en la respuesta
            next_node = navigate_tree(st.session_state.node, response)
            
            if isinstance(next_node, DecisionNode):
                st.session_state.node = next_node
                st.session_state.next_question = next_node.question
                st.session_state.show_question = True
            else:
                st.session_state.final_result = next_node
                st.session_state.node = None  # Reset node to end
                st.session_state.next_question = None
                st.session_state.show_question = False

if __name__ == "__main__":
    main()
