import { useState } from 'react';
import styles from './TodoForm.module.css';
import isEmpty from '../../utils/checkEmptyString';
import Button from '../../UI/Button';

export default function TodoForm({ addTodo }) {
  const [todoInput, setTodoInput] = useState('');

  const updateTodo = () => {
    addTodo(todoInput);
    setTodoInput('');
  };

  const onSubmitHandler = (event) => {
    event.preventDefault();
    isEmpty(todoInput) ? updateTodo() : console.log('Error: Empty string');
  };

  return (
    <div className={styles.todoFormContainer}>
      <form onSubmit={onSubmitHandler}>
        <input
          placeholder="Enter new todo"
          value={todoInput}
          onChange={(event) => {
            setTodoInput(event.target.value);
          }}
        ></input>
        <Button type="submit" title="Submit">
          Submit
        </Button>
      </form>
    </div>
  );
}
