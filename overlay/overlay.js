let lastSession = null;
let lastEventId = null;
let lastRank = null;

async function updateOverlay() {

    try {

        const response = await fetch("/data/overlay_data.json?ts=" + Date.now());

        if (!response.ok) {
            return;
        }

        const data = await response.json();

        const rankName = document.getElementById("rank-name");
        const srText = document.getElementById("sr");
        const session = document.getElementById("session");

        const popup = document.getElementById("result-popup");
        const popupTitle = document.getElementById("result-title");
        const popupSR = document.getElementById("result-sr");

        const rankPopup = document.getElementById("rank-popup");
        const rankTitle = document.getElementById("rank-title");
        const newRank = document.getElementById("new-rank");

        if (lastRank !== null && lastRank !== data.rank) {

            rankTitle.textContent = "RANK UP";

            newRank.textContent = data.rank;


            rankPopup.classList.remove("show");

            void rankPopup.offsetWidth;

            rankPopup.classList.add("show");

        }

        lastRank = data.rank;

        rankName.textContent = data.rank;

        srText.textContent =
            `${data.sr} SR`;

        const value = Number(data.session);

        if (lastEventId !== data.event_id) {

           if (data.last_result === "Victory") {

                popupTitle.textContent = "VICTORY";

                popupSR.textContent = `▲ +${Math.abs(data.session)}`;

            }
            else {

                popupTitle.textContent = "DEFEAT";

                popupSR.textContent = `▼ ${Math.abs(data.session)}`;

            }


            popup.classList.remove("show");

            void popup.offsetWidth;

            popup.classList.add("show");


            lastEventId = data.event_id;

        }
        if (value >= 0) {

            session.textContent = `▲ +${value}`;

            session.className = "session positive";


            if (lastSession !== value) {

                session.classList.remove("session-update");

                void session.offsetWidth;

                session.classList.add("session-update");

            }

            lastSession = value;

        } else {

            session.textContent = `▼ ${Math.abs(value)}`;

            session.className = "session negative";


            if (lastSession !== value) {

                session.classList.remove("session-update");

                void session.offsetWidth;

                session.classList.add("session-update");

            }

            lastSession = value;

        }

        document.getElementById("rank-icon").src =
            "/" + data.rank_icon;

    }

    catch (err) {

        console.log("Overlay :", err);

    }

}

updateOverlay();

setInterval(updateOverlay, 1000);