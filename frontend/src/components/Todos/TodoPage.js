import { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import TodosActions from './TodosActions';
import TodoForm from './TodoForm';
import TodoList from './TodoList';
import styles from './TodoPage.module.css';

export default function TodoPage() {
  // const TODOS_API = 'http://127.0.0.1:5000/todos';
  // const TODOS_API_INSERT = 'http://127.0.0.1:5000/todos_insert';
  // useEffect(() => {
  //   fetch(TODOS_API)
  //     .then((response) => response.json())
  //     .then((json) => {
  //       setTodos(json);
  //     })
  //     .catch((error) => console.log(error));
  // }, []);
  // const addTodoHandler = (todoText) => {
  //   const headers = {
  //     'Content-type': 'application/json',
  //   };
  //   fetch(TODOS_API_INSERT, {
  //     method: 'POST',
  //     body: JSON.stringify(todoText),
  //     headers: headers,
  //   });
  //   console.log();
  // };

  const [todos, setTodos] = useState([]);

  const addTodoHandler = (todoText) => {
    const newTodo = {
      todoText,
      isComplited: false,
      id: uuidv4(),
    };
    setTodos([...todos, newTodo]);
  };

  const toggleTodoHandler = (index) => {
    setTodos(
      todos.map((todo) =>
        index === todo.id
          ? { ...todo, isComplited: !todo.isComplited }
          : { ...todo }
      )
    );
  };

  const deleteTodoHandler = (index) => {
    setTodos(todos.filter((todo) => todo.id !== index));
  };

  const resetTodoHandler = () => {
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
      {!!todos.length && (
        <TodosActions
          completedTodosExists={!!completedTodosCount}
          resetTodo={resetTodoHandler}
          deleteCompletedTodos={deleteCompletedTodosHandler}
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
