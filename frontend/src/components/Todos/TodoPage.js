import { useEffect, useState } from 'react';
import TodosActions from './TodosActions';
import TodoForm from './TodoForm';
import TodoList from './TodoList';
import styles from './TodoPage.module.css';
import ClearAllConfirmation from './ClearAllConfirmation';

export default function TodoPage() {
  const [todos, setTodos] = useState([]);
  const [modalActive, setModalActive] = useState(false);

  const GET_API = 'http://127.0.0.1:5000/todos';
  const INSERT_API = 'http://127.0.0.1:5000/todo_insert';
  const DELETE_API = 'http://127.0.0.1:5000/todo_delete';
  const CLEAR_API = 'http://127.0.0.1:5000/todo_clear';
  const UPDATE_STATUS_API = 'http://127.0.0.1:5000/todo_update_status';

  useEffect(() => {
    fetch(GET_API)
      .then((response) => response.json())
      .then((json) => setTodos(json));
  }, []);

  const insertTodo = (todo) => {
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(todo),
    };
    fetch(INSERT_API, requestOptions)
      .then((response) => response.json())
      .then((data) => setTodos([...todos, data[0]]));
  };

  const deleteTodo = (id) => {
    const dataToSend = { id };
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    };
    fetch(DELETE_API, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setTodos(todos.filter((todo) => todo.id !== data[0].id));
      }); // data[0] == object like {id: 1, user_id: 1}
  };

  const clearTodos = () => {
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    };
    fetch(CLEAR_API, requestOptions)
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  const addTodoHandler = (todoText) => {
    const newTodo = {
      todoText,
      isComplited: false,
    };
    insertTodo(newTodo);
  };

  const toggleTodoHandler = (todo) => {
    const id = todo.id;
    const isComplited = todo.isComplited;

    const dataToSend = { id, isComplited };

    const requestOptions = {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    };
    fetch(UPDATE_STATUS_API, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setTodos(
          todos.map((todo) =>
            data[0].id === todo.id
              ? { ...todo, isComplited: !todo.isComplited }
              : { ...todo }
          )
        );
      });
  };

  const deleteTodoHandler = (index) => {
    deleteTodo(index);
  };

  //delete all todos from db
  const resetTodoHandler = () => {
    clearTodos();
    setTodos([]);
  };

  const deleteCompletedTodosHandler = () => {
    setTodos(todos.filter((todo) => !todo.isComplited));
  };

  const completedTodosCount = todos.filter((todo) => todo.isComplited).length;

  return (
    <div className={styles.todoPageContainer}>
      <h1>Todo App</h1>
      <TodoForm addTodo={addTodoHandler} />
      <ClearAllConfirmation
        active={modalActive}
        setActive={setModalActive}
        resetTodo={resetTodoHandler}
      />
      {!!todos.length && (
        <TodosActions
          completedTodosExists={!!completedTodosCount}
          resetTodo={resetTodoHandler}
          deleteCompletedTodos={deleteCompletedTodosHandler}
          setActive={setModalActive}
        />
      )}
      <TodoList
        todos={todos}
        deleteTodo={deleteTodoHandler}
        toggleTodo={toggleTodoHandler}
      />
      {!!completedTodosCount && (
        <div>
          You have completed {completedTodosCount}{' '}
          {completedTodosCount === 1 ? 'todo' : 'todos'}
        </div>
      )}
    </div>
  );
}
