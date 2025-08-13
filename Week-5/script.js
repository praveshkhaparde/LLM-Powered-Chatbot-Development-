const msgs = document.getElementById("msgs");
const input = document.getElementById("q");
const send = document.getElementById("send");
// converter = new showdown.Converter();
send.addEventListener("click", askBot);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") askBot();
});

async function askBot() {
  const text = input.value.trim();
  if (!text) return;
  append("user", text);
  input.value = "";
  input.disabled = true;
  send.disabled = true;

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: text }),
    });
    const { answer } = await res.json();
    // const html = converter.makeHtml(answer);
    append("bot", answer);
  } catch (err) {
    append("bot", "❌ Error: Could not contact server.");
    console.error(err);
  } finally {
    input.disabled = false;
    send.disabled = false;
    input.focus();
  }
}

function append(role, htmlContent, isHtml = false) {
  const el = document.createElement("div");
  el.className = "msg " + role;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  if (isHtml) bubble.innerHTML = htmlContent;
  else bubble.innerText = htmlContent;
  el.appendChild(bubble);
  msgs.appendChild(el);
  msgs.scrollTop = msgs.scrollHeight;
}
