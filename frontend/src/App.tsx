import { Route, Routes } from "react-router-dom";
import DebateDetail from "./components/DebateDetail/DebateDetail";
import HomePage from "./components/HomePage/HomePage";

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<HomePage />}></Route>
                <Route path="/detail" element={<DebateDetail />}></Route>
            </Routes>
        </>
    );
}

export default App;
