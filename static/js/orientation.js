
const body = document.querySelector('body');
const warner = document.createElement('div');

warner.innerHTML = `
    <div class="warner">
        <h2 class="warner__title">Переверни телефон вертикально по-братски ._.</h2>
        
        <svg class="warner__icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="mdi-phone-rotate-landscape" viewBox="0 0 24 24"><path d="M9,1H3A2,2 0 0,0 1,3V16A2,2 0 0,0 3,18H9A2,2 0 0,0 11,16V3A2,2 0 0,0 9,1M9,15H3V3H9V15M21,13H13V15H21V21H9V20H6V21A2,2 0 0,0 8,23H21A2,2 0 0,0 23,21V15A2,2 0 0,0 21,13M23,10L19,8L20.91,7.09C19.74,4.31 17,2.5 14,2.5V1A9,9 0 0,1 23,10Z" /></svg>
    </div>
`


function checkOrientation(orientation) {
    if(orientation == 'landscape-primary') warner.remove()
    else {
        body.append(warner)
    }
}

checkOrientation(window.screen.orientation.type)

window.screen.orientation.onchange = () => {
    checkOrientation(this.screen.orientation.type)
}