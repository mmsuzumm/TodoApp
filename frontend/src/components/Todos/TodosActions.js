import { RiRefreshLine } from 'react-icons/ri';
import { FaRegTrashAlt } from 'react-icons/fa';
import styles from './TodosActions.module.css';
import Button from '../../UI/Button';
export default function TodosActions({
  deleteCompletedTodos,
  completedTodosExists,
  setActive,
}) {
  return (
    <div className={styles.todosActionsContainer}>
      <Button title="Reset todos" onClick={() => setActive(true)}>
        <RiRefreshLine />
      </Button>
      <Button
        title="Clear completed todos"
        onClick={() => deleteCompletedTodos()}
        disabled={!completedTodosExists}
      >
        <FaRegTrashAlt />
      </Button>
    </div>
  );
}
