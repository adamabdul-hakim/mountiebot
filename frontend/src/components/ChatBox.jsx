import { useState, useRef, useEffect } from "react";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const scrollRef = useRef(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await res.json();
      const botMessage = { sender: "bot", text: data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error("Error:", err);
    }

    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex flex-col h-full max-w-2xl w-full mx-auto bg-white/70 dark:bg-gray-900/70 backdrop-blur-md rounded shadow-lg p-4">
      {/* Message area */}
      <div className="flex-1 overflow-y-auto space-y-2 pr-1">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`mb-2 p-2 rounded break-words ${
              msg.sender === "user"
                ? "bg-blue-100 text-right text-black dark:bg-blue-300 dark:text-black"
                : "bg-gray-100 text-left text-black dark:bg-gray-800 dark:text-white"
            }`}
          >
            {msg.text}
          </div>
        ))}
        <div ref={scrollRef} />
      </div>

      {/* Input area */}
      <div className="mt-4 flex">
        <input
          type="text"
          className="flex-1 p-2 border border-gray-300 rounded-l dark:bg-gray-700 dark:text-white outline-none"
          placeholder="Ask me anything..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-r"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
}
