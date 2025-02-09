import DetailHeader from "../DetailHeader/DetailHeader";
import ParticipantsCard from "../ParticipantsCard/ParticipantsCard";
import ParticipantsSection from "../ParticipantsSection/ParticipantsSection";
import styles from "./DebateDetail.module.css";

export interface DebateDetails {
    title: string;
    description: string;
    userStances: UserStance[];
}

export interface UserStance {
    username: string;
    confidence: string;
    argument: string;
    stance: string;
}

const DebateDetail = ({ title, description, userStances }: DebateDetails) => {
    return (
        <div className={styles.con}>
            <DetailHeader
                title={title}
                description={description}
            ></DetailHeader>
            <ParticipantsSection>
                {userStances.map((us) => (
                    <ParticipantsCard
                        username={us.username}
                        confidence={us.confidence}
                        argument={us.argument}
                        stance={us.stance}
                    ></ParticipantsCard>
                ))}
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
