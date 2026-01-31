let timeout = null;

const smsInput = document.getElementById("smsInput");
const verdictEl = document.getElementById("verdict");
const reasonsEl = document.getElementById("reasons");
const statusEl = document.getElementById("status");

smsInput.addEventListener("input", () => {
    statusEl.innerText = "🟠 Message received, analyzing...";
    
    // debounce (simulate real-time event processing)
    clearTimeout(timeout);

    timeout = setTimeout(() => {
        analyzeMessage(smsInput.value);
    }, 800);
});

function analyzeMessage(message) {
    if (!message.trim()) {
        statusEl.innerText = "🟡 Waiting for message...";
        verdictEl.innerText = "—";
        reasonsEl.innerHTML = "";
        return;
    }

    fetch("http://127.0.0.1:8000/event/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        statusEl.innerText = "🟢 Analysis complete";

        verdictEl.innerText = data.verdict;
        reasonsEl.innerHTML = "";

        data.reasons.forEach(r => {
            const li = document.createElement("li");
            li.innerText = r;
            reasonsEl.appendChild(li);
        });
    })
    .catch(() => {
        statusEl.innerText = "🔴 Agent unavailable";
    });
}
