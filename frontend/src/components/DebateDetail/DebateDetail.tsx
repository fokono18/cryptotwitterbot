import DetailHeader from "../DetailHeader/DetailHeader";
import ParticipantsCard from "../ParticipantsCard/ParticipantsCard";
import ParticipantsSection from "../ParticipantsSection/ParticipantsSection";
import Spinner from "../Spinner/Spinner";
import styles from "./DebateDetail.module.css";

export interface DebateDetails {
    title: string;
    description: string;
    userStances: UserStance[];
    loading: boolean;
}

export interface UserStance {
    username: string;
    confidence: string;
    argument: string;
    stance: string;
}

const DebateDetail = ({
    loading,
    title,
    description,
    userStances,
}: DebateDetails) => {
    const stanceTypes = ["Agree", "Disagree", "Neutral"];
    const getDefaultStance = (
        stance: string,
        stanceTypes: string[]
    ): string => {
        return stanceTypes.includes(stance) ? stance : "Neutral";
    };

    return (
        <div className={styles.con}>
            {!loading ? (
                <>
                    <DetailHeader
                        title={title}
                        description={description}
                    ></DetailHeader>
                    <ParticipantsSection>
                        {userStances
                            ? userStances.map((us) => (
                                  <ParticipantsCard
                                      username={us.username}
                                      confidence={us.confidence}
                                      argument={us.argument}
                                      stance={getDefaultStance(
                                          us.stance,
                                          stanceTypes
                                      )}
                                  ></ParticipantsCard>
                              ))
                            : ""}
                    </ParticipantsSection>
                </>
            ) : (
                <Spinner />
            )}
        </div>
    );
};

export default DebateDetail;
