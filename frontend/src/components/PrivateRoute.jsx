import { Navigate } from "react-router-dom";
import { isLoggedIn } from "../Utils/auth";

export default function PrivateRoute({ children }) {
  return isLoggedIn() ? children : <Navigate to="/" />;
}
