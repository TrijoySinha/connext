import { useState } from "react";

export default function CommandBar() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const submitCommand = async () => {
    if (!input.trim()) return;

    setLoading(true);

    const res = await fetch("http://localhost:8000/command", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: input })
    });

    const data = await res.json();
    setResponse(data);
    setLoading(false);
  };

  return (
    <div style={styles.wrapper}>
      <input
        style={styles.input}
        placeholder="Type a command..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && submitCommand()}
      />

      {loading && <p>Thinking...</p>}

      {response && (
        <div style={styles.result}>
          <strong>{response.intent}</strong>
          <pre>{JSON.stringify(response.result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

const styles = {
  wrapper: {
    maxWidth: "600px",
    margin: "100px auto",
    textAlign: "center"
  },
  input: {
    width: "100%",
    padding: "12px",
    fontSize: "18px"
  },
  result: {
    marginTop: "20px",
    textAlign: "left",
    background: "#f4f4f4",
    padding: "10px"
  }
};