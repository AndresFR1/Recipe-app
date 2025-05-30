import { useState } from "react";
import SearchBar from "../components/SearchBar";
import RecipeCard from "../components/RecipeCard";
import axios from "axios";

export default function Home() {
  const [recipes, setRecipes] = useState([]);

  const search = async (query) => {
    const res = await axios.get(`http://localhost:5000/api/search?q=${query}`);
    setRecipes(res.data.meals || []);
  };

  return (
    <div>
      <h1>Welcome to Recipe App</h1>
      <SearchBar onSearch={search} />
      <div className="recipes-grid">
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.idMeal} recipe={recipe} />
        ))}
      </div>
    </div>
  );
}
