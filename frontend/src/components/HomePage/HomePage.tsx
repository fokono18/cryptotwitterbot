import { useState } from "react";
import styles from "./HomePage.module.css";
import { useNavigate } from "react-router-dom";

type FormData = { description: string };

const HomePage = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState<FormData>({ description: "" });

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log("Form submitted");
        console.log(formData);
        navigate("/detail");
    };

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <h1 className={styles.title}>Crypto Debate Analysis</h1>
                <p className={styles.description}>
                    Enter your search query to analyze cryptocurrency debates
                    and discussions
                </p>
            </div>
            <form className={styles.searchForm} onSubmit={handleSubmit}>
                <div className={styles.inputGroup}>
                    <input
                        type="text"
                        className={styles.searchInput}
                        placeholder="Describe what you're looking for..."
                        required
                        onChange={handleInputChange}
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
