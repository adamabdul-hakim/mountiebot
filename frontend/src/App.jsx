import Header from "./components/Header";
import ChatBox from "./components/ChatBox";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div
      className="flex flex-col min-h-screen bg-white text-black dark:bg-gray-900 dark:text-white transition-colors duration-300 bg-cover bg-center bg-fixed"
      style={{ backgroundImage: "url('/images/berea-campus.jpg')" }}
    >
      <Header />
      <main className="flex-grow flex items-center justify-center p-4">
        <ChatBox />
      </main>
      <Footer />
    </div>
  );
}
