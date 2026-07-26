let lastSR = null;

async function updateOverlay(){

    const response = await fetch("overlay_data.json?"+Date.now());

    const data = await response.json();

    if(lastSR !== null){

    const diff = data.current_sr - lastSR;

    if(diff !== 0){

        const popup = document.getElementById("srPopup");

        popup.innerText =
            (diff > 0 ? "+" : "") + diff + " SR";

        popup.style.color =
            diff > 0 ? "#34ff7b" : "#ff4b4b";

        popup.classList.add("popupShow");

        setTimeout(()=>{

            popup.classList.remove("popupShow");

        },1500);

    }

}

lastSR = data.current_sr;

    document.getElementById("rankName").innerText=data.rank;

    const color = getRankColor(data.rank);

    document.getElementById("rankName").style.color = color;
    document.getElementById("progressFill").style.background = color;

    document.getElementById("sr").innerText=data.current_sr+" SR";

    document.getElementById("session").innerText=(data.session_sr>=0?"+":"")+data.session_sr+" SR";

    document.getElementById("streak").innerText="x"+data.winstreak;

    const games=data.wins+data.losses;

    const wr=games>0?(data.wins/games*100).toFixed(1):0;

    document.getElementById("wr").innerText=wr+"%";

    const progress=Math.min(data.current_sr/data.goal*100,100);

    document.getElementById("progressFill").style.width=progress+"%";

    const rank=data.rank.toLowerCase().replace(/ /g,"");

    document.getElementById("rankImage").src="ranks/"+rank+".png";

}

function getRankColor(rank){

    switch(rank.toLowerCase()){

        case "bronze":
            return "#9b6b43";

        case "argent":
            return "#d8d8d8";

        case "or":
            return "#ffcc33";

        case "platinium":
            return "#44ffd4";

        case "diams":
            return "#42a5ff";

        case "crimson":
            return "#d32f2f";

        case "iridescent":
            return "#a64dff";

        case "top250":
            return "#ff8c00";

        default:
            return "#ffffff";
    }

}

function showEvent(message){

    const popup = document.getElementById("eventPopup");

    popup.innerText = message;

    popup.classList.add("eventShow");

    setTimeout(()=>{

        popup.classList.remove("eventShow");

    },2000);

}

updateOverlay();
setInterval(updateOverlay,500);