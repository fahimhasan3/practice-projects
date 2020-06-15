let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget(){]
    //generate ramdom number from 0 to 9
    return Math.floor(Math.random() * 10); 
}

function compareGuesses(userGuess, computerGuess, secretNumber) {
    /*Determines which player (human or computer) wins based on which guess is closest 
    to the target. If both players are tied, the human user wins*/
    let humanDistance = getAbsoluteDistance(userGuess, secretNumber);
    let computerDistance = getAbsoluteDistance(computerGuess, secretNumber);
    if(humanDistance == computerDistance || humanDistance < computerDistance) {
        return true;
    } else {
        return false;
    }
}

function updateScore(winner){
    if(winner.toLowerCase() === 'human') {
        humanScore++;
    } else if(winner.toLowerCase() === 'computer'){
        computerScore++;
    }
}

function advanceRound(){
    currentRoundNumber++;
}

function getAbsoluteDistance(point1, point2){
    return Math.abs(point1 - point2);
}