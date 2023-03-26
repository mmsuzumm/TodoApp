import { RiRefreshLine } from 'react-icons/ri';
import { FaRegTrashAlt } from 'react-icons/fa';
import styles from './TodosActions.module.css';
import Button from '../../UI/Button';
export default function TodosActions({
  resetTodo,
  deleteCompletedTodos,
  completedTodosExists,
}) {
  return (
    <div className={styles.todosActionsContainer}>
      <Button title="Reset todos" onClick={() => resetTodo()}>
        <RiRefreshLine />
      </Button>
      <Button
        title="Clear complited todos"
        onClick={() => deleteCompletedTodos()}
        disabled={!completedTodosExists}
      >
        <FaRegTrashAlt />
      </Button>
    </div>
  );
}
