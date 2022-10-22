const sliderLine = document.querySelector('#line');
const slide = sliderLine.querySelector('.stage');
const desc = document.querySelector('#desc');
const texts = document.querySelectorAll('#desc__text');
const btn = document.querySelector('.btn-area');

btn.style.display = 'none';

const rooms = document.querySelectorAll('#room')

function showRoom(textIndex) {
    rooms.forEach(text => text.style.display = 'none');
    rooms[textIndex].style.display = 'block';
}

function showDesc(textIndex) {
    texts.forEach(text => text.style.display = 'none');
    texts[textIndex].style.display = 'block';
}

function openDesc (time) {
    desc.style.height = '20px';
    desc.style.transition = `all ${time}s`;
    desc.style.height = '100%';
}

showRoom(0);

showDesc(0);
openDesc(20);

setTimeout(() => {
    sliderLine.style.transition = 'all 7s';
    sliderLine.style.left = '-200vw';
}, 1000)

setTimeout(() => {
    sliderLine.style.transition = 'all 1s';
    sliderLine.style.top = `-${slide.offsetHeight}px`;
    desc.style.transition = `all 0s`;
}, 7000)

setTimeout(() => {
    showDesc(1);
}, 7500)

setTimeout(() => {
    showRoom(1)
    showDesc(2)
}, 15000)

setTimeout(() => {
    showRoom(2)
    showDesc(3)
}, 24000)

setTimeout(() => {
    showRoom(3)
    showDesc(4)
}, 29000)

setTimeout(() => {
    btn.style.display = 'flex';    
}, 32000)

