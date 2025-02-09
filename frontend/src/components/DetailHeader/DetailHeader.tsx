import styles from "./DetailHeader.module.css";

interface Props {
    title: string;
    description: string;
}
const DetailHeader = ({ title, description }: Props) => {
    return (
        <div className={styles.debateHeader}>
            <h1 className={styles.debateTitle}>{title}</h1>
            <p className={styles.debateSummary}>{description}</p>
        </div>
    );
};

export default DetailHeader;
