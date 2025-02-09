import styles from "./ParticipantsSection.module.css";

interface Props {
    children: React.ReactNode;
}

const ParticipantsSection = ({ children }: Props) => {
    return (
        <div className={styles.section}>
            <h2 className={styles.title}>Participant Stances</h2>
            {children}
        </div>
    );
};

export default ParticipantsSection;
