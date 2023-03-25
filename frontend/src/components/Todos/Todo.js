import { RiTodoLine, RiDeleteBin2Line } from 'react-icons/ri';
import { FaCheck } from 'react-icons/fa';
import styles from './Todo.module.css';

console.log(styles);

export default function Todo({ todo, deleteTodo }) {
  return (
    <div className={styles.todoContainer}>
      <RiTodoLine className={styles.todoIcon} />
      <div className={styles.todoTextContainer}>{todo.text}</div>
      <RiDeleteBin2Line
        className={styles.deleteIcon}
        onClick={() => {
          deleteTodo(todo.id);
        }}
      />
      <FaCheck className={styles.checkIcon} />
    </div>
  );
}
