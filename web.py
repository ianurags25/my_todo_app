import streamlit
import functions
def add_todo():
    todo = streamlit.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)
todos = functions.get_todos()
streamlit.title("My Todo App")
streamlit.subheader("This is my todo app.")
streamlit.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()
streamlit.text_input(label="Enter a ToDo",placeholder="Add the New One..",
                     on_change=add_todo, key ='new_todo')
streamlit.session_state