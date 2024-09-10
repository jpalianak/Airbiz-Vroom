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

# Función para hacer preguntas y navegar por el árbol de decisiones usando Streamlit
def ask_question(node):
    if isinstance(node.yes, DecisionNode):
        response = st.radio(node.question, ["Sí", "No"], key=node.question)
        if response == "Sí":
            ask_question(node.yes)
        else:
            ask_question(node.no)
    else:
        st.write(f"Estilo de liderazgo recomendado: {node.yes}")

# Configuración de la aplicación Streamlit
def main():
    st.title("Árbol de decisión de Vroom-Yetton-Yago")
    root = build_tree()
    st.write("Responde a las preguntas para obtener el estilo de liderazgo recomendado:")
    ask_question(root)

# Llamada a la función principal para iniciar la aplicación Streamlit
if __name__ == "__main__":
    main()
