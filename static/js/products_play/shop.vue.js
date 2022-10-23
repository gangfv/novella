const nextBtn = document.querySelector('.next-btn')


function FormDataCreator(data) {
    const formObj = {...data}

    const formData = new FormData()
    for (const key in formObj) {
        formData.append(key, formObj[key])
    }

    return formData
}

const getMoney = () => {
    const {csrftoken} = Cookies.getCookies()
    return axios.get('./money', {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    })
}

const postBuy = (buy, cost) => {
    const {csrftoken} = Cookies.getCookies()

    return axios.post('./buy', {
        buy: [...buy],
        cost
    }, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
}

const costs = {
    bread: 30,
    nike: 15000,
    choco: 100,
    shoos: 3000,
    sweets: 300,
    chick: 250,
    socks: 200,
    gucci: 5000,
    medicine: 1000,
    dino: 500,
    dish: 400,
    watch: 10000,
    jacket: 7000,
    grechka: 150,
    sigi: 500,
    water: 500,
    gold: 3000,
    ticket: 700
}

const marks = {
    bread: 0,
    nike: 2,
    choco: 1,
    shoos: 0,
    sweets: 2,
    chick: 0,
    socks: 1,
    gucci: 2,
    medicine: 0,
    dino: 1,
    dish: 1,
    watch: 2,
    jacket: 0,
    grechka: 0,
    sigi: 2,
    water: 0,
    gold: 2,
    ticket: 1
}


const Shop = {
    delimiters: ['[[', ']]'],
    data: () => ({
        products: [],
        money: 0,
        currentMoney: 0,
        basketMark: 'good'
    }),
    created() {
        getMoney().then(res => {
            const money = res.data.money
            this.money = money
            this.currentMoney = money
        })
    },
    updated() {

        if (this.currentMoney < 0) nextBtn.style.display = 'none';
        else nextBtn.style.display = 'inline-block'
    },
    watch: {
        products(current, old) {
            const fullCost = current.map(product => costs[product]).reduce((sum, cost) => sum + cost,)
            this.currentMoney = this.money - fullCost

            function countMarks(values, mark) {
                return values.filter(val => val === mark).length
            }

            const values = current.map(product => marks[product])

            if (countMarks(values, 2 || this.currentMoney < 0) >= 1) {
                this.basketMark = 'bad'
            } else if (countMarks(values, 1) > 2) {
                this.basketMark = 'norm'
            } else {
                this.basketMark = 'good'
            }
        }
    },
    computed: {
        isDisabled() {
            return this.currentMoney < 0
        },
    },
    methods: {
        nextPage() {
            //window.location.href = document.URL + 'invest_easy'
            postBuy(this.products, (this.money - this.currentMoney))
        }
    }
}

Vue.createApp(Shop).mount('#app')