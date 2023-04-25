let xp = 0;
let health = 100;
let gold = 50;
let currentWeapon = 0;
let fighting;
let monterHealth;
let inventory = ["stick"];
let locations = [{
    name: "Town Square",
    "button_text": ["Go to store", "Go to cave", "Fight dragon"],
    "button_func": [goToStore, goToCave, fightDragon],
    text: "You are in Town Square"

},
{
    name: "Store",
    "button_text": ["Buy 10 health (10 gold)", "Buy weapon (30 Gold)", "Go to town square"],
    "button_func": [buyHealth, buyWeapon, goTown],
    text: "You are in store"
},
 {
    name: "Cave",
    "button_text": ["Fight Slime", "Fight Skeleton", "Go Back to Town Square"],
    "button_func": [fight, fight, goTown],
    text: "You are in Cave surrounded by monsters"
 }
]

const button1 = document.querySelector("#button1");
const button2 = document.querySelector("#button2");
const button3 = document.querySelector("#button3");
const text = document.querySelector("#text");
const xpText = document.querySelector("#xpText");
const healthText = document.querySelector("#healthText");
const goldText = document.querySelector("#goldText");
const monsterStats = document.querySelector("#monsterStats");
const monsterNameText = document.querySelector("#monsterName");
const monsterHealthText = document.querySelector("#monsterHealth");

button1.onclick = goToStore
button2.onclick = goToCave
button3.onclick = fightDragon

function update(location) {
    button1.innerText = location['button_text'][0]
    button1.onclick = location['button_func'][0]
    button2.innerText = location['button_text'][1]
    button2.onclick = location['button_func'][1]
    button3.innerText = location['button_text'][2]
    button3.onclick = location['button_func'][2]
    text.innerText = location.text
}

function goTown() {
    update(locations[0])
}

function goToStore() {
    update(locations[1])
}
function goToCave() {
    update(locations[2])
}
function fightDragon() {
    
}
function buyHealth() {

}
function buyWeapon() {

}
function fight() {

}