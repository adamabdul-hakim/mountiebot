import ThemeToggle from "./ThemeToggle";

export default function Header() {
  return (
    <header className="bg-blue-600 text-white p-4 shadow flex justify-between items-center">
      <h1 className="text-xl font-semibold tracking-wide">mountieBot 🤖</h1>
      <ThemeToggle />
    </header>
  );
}
