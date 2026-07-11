import streamlit as st
from PROGRAM import dijkstra, reconstruct_path
st.set_page_config(
    page_title="Implementation of Dijkstra's Algorithm",
    page_icon="📍"
)
st.title("Implementation of Single Source Shortest Path Algorithm (Dijkstra's)")
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}
source = st.number_input(
    "Enter Source Vertex",
    min_value=0,
    max_value=5,
    value=0
)
if st.button("Find Shortest Paths"):
    dist, prev = dijkstra(graph, source)
    st.subheader("Results")
    for v in range(len(graph)):
        path = reconstruct_path(prev, source, v)
        path_str = " -> ".join(map(str, path)) if path else "No Path"
        d = dist[v] if dist[v] != float('inf') else "INF"
        st.write(f"Vertex {v}")
        st.write(f"Distance: {d}")
        st.write(f"Path: {path_str}")
        st.write("---")
