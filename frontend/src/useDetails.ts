import { useState } from "react";
import { DebateDetails } from "./components/DebateDetail/DebateDetail";

const useDetails = () => {
    const [loading, setLoading] = useState(false);
    const [debateDetails, setDebateDetails] = useState<DebateDetails>();

    const loadDebates = async (entry: string) => {
        try {
            // Set loading state to true
            setLoading(true);

            // Make a POST request to the API
            const response = await fetch(" http://127.0.0.1:5000/api", {
                method: "POST", // HTTP method
                headers: {
                    "Content-Type": "application/json", // Specify JSON content
                },
                body: JSON.stringify({ query: entry }), // Data to send in the body
            });

            // Check if the response is OK
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Parse the response JSON
            const data = await response.json();

            // Set the response data to state
            setDebateDetails(data);
        } catch (error) {
            console.error("Error posting to API:", error);
        } finally {
            // Set loading state to false
            setLoading(false);
        }
    };

    return { loadDebates, loading, debateDetails };
};

export default useDetails;
