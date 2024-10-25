let flashcards = [];
let currentIndex;
let score = 0;

function fetchFlashcards(level) {
    fetch('hsk_flashcards.json')
        .then(response => response.json())
        .then(data => {
            flashcards = data[level];
            displayCard();
        });
}

function displayCard() {
    document.getElementById('next-button').style.display = 'none';
    document.getElementById('score').innerText = `Score: ${score}`;
    document.getElementById('options').innerHTML = '';
    document.getElementById('feedback').innerText = '';

    currentIndex = Math.floor(Math.random() * flashcards.length);
    const card = flashcards[currentIndex];
    document.getElementById('chinese').innerText = card.chinese;
    document.getElementById('english').innerText = card.english.split(';')[0];
    loadOptions(card.english);
}

function loadOptions(correctAnswer) {
    const options = [correctAnswer.split(';')[0]];
    while (options.length < 3) {
        const randomCard = flashcards[Math.floor(Math.random() * flashcards.length)];
        const option = randomCard.english.split(';')[0];
        if (!options.includes(option)) {
            options.push(option);
        }
    }
    options.sort(() => Math.random() - 0.5);

    const optionsDiv = document.getElementById('options');
    options.forEach(option => {
        const button = document.createElement('button');
        button.innerText = option;
        button.onclick = () => checkAnswer(option, correctAnswer.split(';')[0]);
        optionsDiv.appendChild(button);
    });
}

function checkAnswer(selected, correct) {
    const flashcard = document.getElementById('flashcard');
    const feedback = document.getElementById('feedback');
    flashcard.classList.add('flipped');
    document.getElementById('next-button').style.display = 'block';

    if (selected === correct) {
        score++;
        feedback.innerText = "Correct!";
        feedback.className = "feedback correct";
    } else {
        score--;
        feedback.innerText = "Wrong!";
        feedback.className = "feedback wrong";
    }
}

function nextFlashcard() {
    const flashcard = document.getElementById('flashcard');
    flashcard.classList.remove('flipped');
    displayCard();
}

// Fetch the level from URL parameters and load flashcards
const urlParams = new URLSearchParams(window.location.search);
const level = urlParams.get('level');
if (level) {
    fetchFlashcards(level);
}
