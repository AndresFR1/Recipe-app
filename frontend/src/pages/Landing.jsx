import React from "react";
import "./Landing.css"; 
import { useNavigate } from "react-router-dom";
import "../pages/Landing.css"; 

export default function Landing() {
    const navigate = useNavigate();
    return (
        <div className="landing-background">
            <div className="landing-container">
                <div className="landing-content">
                    <h1 className="landing-title">Bienvenido a Recipe App</h1>
                    <p className="landing-subtitle">
                            Descubre, busca y guarda tus recetas favoritas de manera sencilla.
                    </p>
                    <div className="landing-actions">
                        <button className="landing-btn" onClick={()=> navigate("/register")}>Explorar recetas</button>
                    </div>
                </div>
            </div>
        </div>
    );
}