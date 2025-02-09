import styles from "./ParticipantsCard.module.css";

interface Props {
    username: string;
    confidence: string;
    argument: string;
    stance: string;
}

const ParticipantsCard = ({
    username,
    confidence,
    argument,
    stance,
}: Props) => {
    return (
        <div className={styles.participantCard}>
            <div className={styles.participantHeader}>
                <div className={styles.participantInfo}>
                    <span className={styles.username}>{username}</span>
                    <span className={`${styles.stance} ${styles.pro}`}>
                        {stance}
                    </span>
                </div>
                <span
                    className={styles.confidence}
                >{`${confidence}% confidence`}</span>
            </div>
            <p className={styles.argument}>{argument}</p>
        </div>
    );
};

export default ParticipantsCard;
