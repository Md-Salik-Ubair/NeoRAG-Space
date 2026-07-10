/*====================================================
NeoRAG Space Enterprise Frontend
main.js
====================================================*/

const chatScroller = document.getElementById("chat-scroller");
const queryField = document.getElementById("query-field");
const submitButton = document.getElementById("submit-trigger");
const loader = document.getElementById("loader");
const clearButton = document.getElementById("clear-btn");
const vectorCounter = document.getElementById("vector-count-display");

/*====================================================
INITIALIZATION
====================================================*/

document.addEventListener("DOMContentLoaded", () => {

    loadVectorCount();

    queryField.focus();

    queryField.addEventListener("keypress", function(e){

        if(e.key==="Enter"){

            sendQuery();

        }

    });

    submitButton.addEventListener("click",sendQuery);

    clearButton.addEventListener("click",clearConversation);

});

/*====================================================
VECTOR COUNT
====================================================*/

async function loadVectorCount(){

    try{

        const response=await fetch("/api/get_vector_count");

        const data=await response.json();

        vectorCounter.innerHTML=`<i class="fa-solid fa-database"></i> ${Number(data.count).toLocaleString()} Indexed Chunks`;

    }

    catch(error){

        vectorCounter.innerHTML=`<i class="fa-solid fa-circle-exclamation"></i> Unable to Load`;

    }

}

/*====================================================
SCROLL
====================================================*/

function scrollBottom(){

    chatScroller.scrollTop=chatScroller.scrollHeight;

}

/*====================================================
LOADER
====================================================*/

function showLoader(){

    loader.style.display="flex";

}

function hideLoader(){

    loader.style.display="none";

}

/*====================================================
MESSAGE CREATOR
====================================================*/

function createMessage(role,text,references=[]){

    const wrapper=document.createElement("div");

    wrapper.className=role==="user" ? "user-message" : "assistant-message";

    const card=document.createElement("div");

    card.className="message-card fade-in";

    card.innerHTML=`<p>${escapeHTML(text).replace(/\n/g,"<br>")}</p>`;

    if(role==="assistant" && references.length>0){

        const ref=document.createElement("div");

        ref.className="reference-box";

        references.forEach(item=>{

            const chip=document.createElement("div");

            chip.className="reference-chip";

            const score=(item.score*100).toFixed(1);

            chip.innerHTML=`
            <i class="fa-solid fa-file"></i>
            ${item.source}
            ${item.page ? "| Page "+item.page : ""}
            |
            <span>${score}%</span>
            `;

            ref.appendChild(chip);

        });

        card.appendChild(ref);

    }

    wrapper.appendChild(card);

    chatScroller.appendChild(wrapper);

    scrollBottom();

}
/*====================================================
SEND QUERY
====================================================*/

async function sendQuery(){

    const question=queryField.value.trim();

    if(question==="") return;

    createMessage("user",question);

    queryField.value="";

    showLoader();

    submitButton.disabled=true;

    try{

        const response=await fetch("/api/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                question:question
            })

        });

        const data=await response.json();

        hideLoader();

        submitButton.disabled=false;

        createMessage(
            "assistant",
            data.answer || "No response generated.",
            data.references || []
        );

    }

    catch(error){

        hideLoader();

        submitButton.disabled=false;

        createMessage(
            "assistant",
            "Unable to communicate with NeoRAG server. Please verify that the backend service is running."
        );

        console.error(error);

    }

}

/*====================================================
CLEAR CHAT
====================================================*/

function clearConversation(){

    const confirmClear=confirm(
        "Clear the current conversation?"
    );

    if(!confirmClear) return;

    chatScroller.innerHTML=`

    <div class="assistant-message">

        <div class="message-card">

            <h3>Conversation Cleared</h3>

            <p>

            Welcome back.

            Ask anything from your indexed private knowledge base.

            </p>

        </div>

    </div>

    `;

    scrollBottom();

}

/*====================================================
HTML SAFE OUTPUT
====================================================*/

function escapeHTML(text){

    const div=document.createElement("div");

    div.innerText=text;

    return div.innerHTML;

}

/*====================================================
AUTO FOCUS
====================================================*/

window.addEventListener("load",()=>{

    queryField.focus();

});

/*====================================================
OPTIONAL SHORTCUT
Ctrl + /
Focus Search Box
====================================================*/

document.addEventListener("keydown",(e)=>{

    if(e.ctrlKey && e.key==="/"){

        e.preventDefault();

        queryField.focus();

    }

});

/*====================================================
END OF FILE
====================================================*/