import styles from './ClearAllConfirmation.module.css';
import Button from '../../UI/Button';
export default function ClearAllConfirmation({ active, setActive, resetTodo }) {
  const clear = () => {
    resetTodo();
    setActive(false);
  };

  return (
    <div
      className={
        active ? `${styles.modal} ${styles.active}` : `${styles.modal}`
      }
      onClick={() => {
        setActive(false);
      }}
    >
      <div
        className={styles.modalContent}
        onClick={(e) => {
          e.stopPropagation();
        }}
      >
        Are you sure you want to delete all todos?
        <div className={styles.modalButtons}>
          <Button onClick={() => setActive(false)}>No</Button>
          <Button onClick={() => clear()}>Yes</Button>
        </div>
      </div>
    </div>
  );
}
