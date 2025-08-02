import { useEffect, useState } from "react";

export default function ThemeToggle() {
  const getInitialTheme = () => {
    if (typeof localStorage !== "undefined" && localStorage.getItem("theme")) {
      return localStorage.getItem("theme") === "dark";
    }
    // Fallback: use system preference
    return window.matchMedia("(prefers-color-scheme: dark)").matches;
  };

  const [isDark, setIsDark] = useState(getInitialTheme);

  useEffect(() => {
    const root = document.documentElement;
    if (isDark) {
      root.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      root.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [isDark]);

  return (
    <button
      onClick={() => setIsDark((prev) => !prev)}
      className="bg-white dark:bg-gray-700 dark:text-white text-gray-800 border border-gray-300 dark:border-gray-600 px-3 py-1 rounded hover:opacity-80 transition"
    >
      {isDark ? "☀️ Light" : "🌙 Dark"}
    </button>
  );
}
