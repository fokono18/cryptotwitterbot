import styles from "./HomePage.module.css";

const HomePage = () => {
    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <h1 className={styles.title}>Crypto Debate Analysis</h1>
                <p className={styles.description}>
                    Enter your search query to analyze cryptocurrency debates
                    and discussions
                </p>
            </div>
            <form className={styles.searchForm}>
                <div className={styles.inputGroup}>
                    <input
                        type="text"
                        className={styles.searchInput}
                        placeholder="Describe what you're looking for..."
                        required
                    />
                </div>
                <button type="submit" className={styles.searchButton}>
                    Search
                </button>
            </form>
        </div>
    );
};

export default HomePage;
