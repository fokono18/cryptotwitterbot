import DetailHeader from "../DetailHeader/DetailHeader";
import ParticipantsCard from "../ParticipantsCard/ParticipantsCard";
import ParticipantsSection from "../ParticipantsSection/ParticipantsSection";
import styles from "./DebateDetail.module.css";

interface DebateDetails {
    title: string;
    description: string;
}

const DebateDetail = () => {
    return (
        <div className={styles.con}>
            <DetailHeader
                title={"hello"}
                description={
                    "he Fermi Paradox is the apparent contradiction between the high probability of extraterrestrial civilizations existing and the lack of evidence for their presence. Named after physicist Enrico Fermi, the paradox arises from the vastness of the universe—billions of galaxies, each containing billions of stars and potentially habitable planets—suggesting that intelligent life should be widespread."
                }
            ></DetailHeader>
            <ParticipantsSection>
                <ParticipantsCard
                    username={"Elonmusk"}
                    confidence={"70"}
                    argument={
                        "I think that we should slap the hell out of Femi"
                    }
                    stance={"Agree"}
                ></ParticipantsCard>
                <ParticipantsCard
                    username={"Elonmusk"}
                    confidence={"70"}
                    argument={
                        "I think that we should slap the hell out of Femi"
                    }
                    stance={"Agree"}
                ></ParticipantsCard>
                <ParticipantsCard
                    username={"Elonmusk"}
                    confidence={"70"}
                    argument={
                        "I think that we should slap the hell out of Femi"
                    }
                    stance={"Agree"}
                ></ParticipantsCard>
            </ParticipantsSection>
        </div>
    );
};

export default DebateDetail;
