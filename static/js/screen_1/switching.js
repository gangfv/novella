const sliderLine = document.querySelector('#line');
const slide = sliderLine.querySelector('.stage');
const desc = document.querySelector('#desc');
const texts = document.querySelectorAll('#desc__text');


function showDesc(textIndex) {
    texts.forEach(text => text.style.display = 'none');
    texts[textIndex].style.display = 'block';
}

function openDesc (time) {
    desc.style.height = '20px';
    desc.style.transition = `all ${time}s`;
    desc.style.height = '100%';
}

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