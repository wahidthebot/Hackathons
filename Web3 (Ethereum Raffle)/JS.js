const formContainer = document.getElementById("formContainer");
const participantList = document.getElementById("participantList");
const walletForm = document.getElementById("walletForm");
const duplicateMessage = document.getElementById("duplicateMessage");
const generateWinnerButton = document.getElementById("generateWinnerButton");
const enteredWalletAddresses = new Set();

const participants = [];

walletForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const userNameInput = document.getElementById("userName");
    const walletAddressInput = document.getElementById("walletAddress");

    const userName = userNameInput.value;
    const walletAddress = walletAddressInput.value;

    if (userName && walletAddress) {
        if (enteredWalletAddresses.has(walletAddress)) {
            duplicateMessage.textContent = "This wallet is already in the raffle.";
            setTimeout(() => {
                duplicateMessage.textContent = "";
            }, 3000);
        } else {
            enteredWalletAddresses.add(walletAddress);

            participants.push({
                name: userName,
                wallet: walletAddress
            });

            const participantEntry = document.createElement("div");
            participantEntry.className = "participant-box";

            const participantContent = document.createElement("div");
            participantContent.className = "participant-entry";

            const nameLabel = document.createElement("span");
            nameLabel.className = "participant-label";
            nameLabel.textContent = "Name:";
            participantContent.appendChild(nameLabel);

            const nameValue = document.createElement("span");
            nameValue.className = "participant-value";
            nameValue.textContent = userName;
            participantContent.appendChild(nameValue);

            const walletLabel = document.createElement("span");
            walletLabel.className = "participant-label";
            walletLabel.textContent = "Wallet#:";
            participantContent.appendChild(walletLabel);

            const walletValue = document.createElement("span");
            walletValue.className = "participant-value";
            walletValue.textContent = walletAddress;
            participantContent.appendChild(walletValue);

            participantEntry.appendChild(participantContent);
            participantList.appendChild(participantEntry);

            if (enteredWalletAddresses.size >= 2) {
                generateWinnerButton.style.display = "block";
            }

            const successMessage = document.createElement("p");
            successMessage.textContent = "Submission successful!";
            formContainer.appendChild(successMessage);

            setTimeout(() => {
                formContainer.removeChild(successMessage);
            }, 2000);

            userNameInput.value = "";
            walletAddressInput.value = "";
        }
    }
});

generateWinnerButton.addEventListener("click", function() {
    if (participants.length >= 2) {
        const randomIndex = Math.floor(Math.random() * participants.length);
        const winner = participants[randomIndex];
        const numberOfParticipants = participants.length;
        const winnings = numberOfParticipants + ".00 Ethereum";

        const winnerBox = document.createElement("div");
        winnerBox.className = "winner-box";
        winnerBox.innerHTML = `
            <h2>Winner</h2>
            <p>Name: ${winner.name}</p>
            <p>Wallet#: ${winner.wallet}</p>
            <p>Winnings: ${winnings}</p>
        `;
        formContainer.appendChild(winnerBox);
    }
});
