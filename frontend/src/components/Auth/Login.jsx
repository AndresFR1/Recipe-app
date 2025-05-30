import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../Auth/Login.css";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/api/login", form);
      localStorage.setItem("token", res.data.token);
      navigate("/home");
    } catch (err) {
      setMessage(err.response?.data?.message || "Error al iniciar sesión");
    }
  };

  return (
    <div className="login-container" style={{ display: "flex", minHeight: "100vh" }}>
      <div className="left-image-container">
        <img
          src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80"
          alt="Comida"
          style={{
            width: "100%",
            height: "100vh",
            objectFit: "cover",
            objectPosition: "center",
            display: "block"
          }}
        />
      </div>
      <div className="right-form-container"
        style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center" }}>
        <div style={{ width: "100%", maxWidth: "350px", borderRadius: "8px", color: "rgba(2, 2, 2, 0.77)" }}>
          <h1 className="login">Iniciar sesión</h1>
          <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "28px" }} autoComplete="off">
            <input className="input-username"
              name="username"
              placeholder="Usuario"
              value={form.username}
              onChange={handleChange}              
              autoComplete="new-username"
            />
            <input className="input-password"
              name="password"
              type="password"
              placeholder="Contraseña"
              value={form.password}
              onChange={handleChange}
              autoComplete="new-password"
            />
            <button className="login-btn" type="submit" style={{ fontSize: "1.1rem", padding: "12px" }}>
              Ingresar
            </button>
          </form>
          <p style={{ textAlign: "center", marginTop: "16px", color: "#d32f2f", fontSize: "1rem" }}>{message}</p>
        </div>
      </div>
    </div>
  );
}
