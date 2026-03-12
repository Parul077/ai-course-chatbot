let sessionId = localStorage.getItem("session_id");

function handleKeyPress(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
}

async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const typing = document.getElementById("typing");

    const message = input.value.trim();

    if (!message) return;

    /* 1️⃣ Add user message */

    chatBox.innerHTML += `
         <div class="message-row user-row">
         <div class="message user">${message}</div>
         <div class="avatar user-avatar">👤</div>
    </div>
    `;

    input.value = "";

    /* Scroll down */

    chatBox.scrollTop = chatBox.scrollHeight;

    /* 2️⃣ Show typing indicator */

    typing.style.display = "block";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        const data = await response.json();

        /* Hide typing */

        typing.style.display = "none";

        /* Save session id */

        if (data.session_id && data.session_id !== sessionId) {
            sessionId = data.session_id;
            localStorage.setItem("session_id", sessionId);
        }

        /* 3️⃣ Show bot response */

        if (response.ok) {

            chatBox.innerHTML += `
                <div class="message-row bot-row">
                <div class="avatar bot-avatar">🤖</div>
                <div class="message bot">${data.reply}</div>
            </div>
            `;

        } else {

            const errorMsg = data.message || data.error || "AI service unavailable.";

            chatBox.innerHTML += `
                <div class="message bot" style="color:orange;">
                    ${errorMsg}
                </div>
            `;
        }

    } catch (error) {

        typing.style.display = "none";

        chatBox.innerHTML += `
            <div class="message bot" style="color:red;">
                Connection lost.
            </div>
        `;
    }

    /* Scroll to newest message */

    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: "smooth"
    });

    /* Update analytics */

    loadAnalytics();

}

function animateCounter(elementId, newValue){

    const element = document.getElementById(elementId);
    const currentValue = parseInt(element.innerText) || 0;

    const increment = Math.ceil((newValue - currentValue) / 10);

    let value = currentValue;

    const counter = setInterval(() => {

        value += increment;

        if(value >= newValue){
            value = newValue;
            clearInterval(counter);
        }

        element.innerText = value;

    }, 30);

}

async function loadAnalytics(){

    try{

        const response = await fetch("/analytics");

        const data = await response.json();

        animateCounter("totalMessages", data.total_messages);
        animateCounter("cacheHits", data.cache_hits);
        animateCounter("llmCalls", data.llm_calls);

    }catch(error){
        console.log("Analytics error", error);
    }

}

//Load Analytics on Page Start

window.onload = loadAnalytics;