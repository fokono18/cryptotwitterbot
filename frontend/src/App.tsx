import { Route, Routes } from "react-router-dom";
import DebateDetail, {
    UserStance,
} from "./components/DebateDetail/DebateDetail";
import HomePage from "./components/HomePage/HomePage";
import useDetails from "./useDetails";

function App() {
    const { loadDebates, debateDetails } = useDetails();

    return (
        <>
            <Routes>
                <Route
                    path="/"
                    element={<HomePage loadDebates={loadDebates} />}
                ></Route>
                <Route
                    path="/detail"
                    element={
                        <DebateDetail
                            title={debateDetails?.title as string}
                            description={debateDetails?.description as string}
                            userStances={
                                debateDetails?.userStances as UserStance[]
                            }
                        />
                    }
                ></Route>
            </Routes>
        </>
    );
}

export default App;
