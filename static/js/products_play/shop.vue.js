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


const Shop = {
    delimiters: ['[[', ']]'],
    data: () => ({
        products: [],
        money: 0,
        currentMoney: 0
    }),
    created() {
        getMoney().then(res => {
            const money = res.data.money
            this.money = money
            this.currentMoney = money
        })
    },
    watch: {
        products(current, old) {
            const fullCost = current.map(product => costs[product]).reduce( (sum, cost) => sum + cost, )
            this.currentMoney = this.money - fullCost
        }
    },
    methods: {}
}

Vue.createApp(Shop).mount('#app')