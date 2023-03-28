import { RiTodoLine, RiDeleteBin2Line } from 'react-icons/ri';
import { FaCheck } from 'react-icons/fa';
import styles from './Todo.module.css';

export default function Todo({ todo, deleteTodo, toggleTodo }) {
  return (
    <div
      className={`${styles.todoContainer} ${
        todo.isComplited ? styles.completedTodo : ''
      }`}
    >
      <RiTodoLine className={styles.todoIcon} />
      <div className={styles.todoTextContainer}>{todo.todoText}</div>
      <RiDeleteBin2Line
        className={styles.deleteIcon}
        onClick={() => {
          deleteTodo(todo.id);
        }}
      />
      <FaCheck
        className={styles.checkIcon}
        onClick={() => {
          toggleTodo(todo.id);
        }}
      />
    </div>
  );
}
